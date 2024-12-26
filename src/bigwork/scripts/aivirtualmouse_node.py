#!/usr/bin/env python

import rospy
import cv2
import mediapipe as mp
import time
import numpy as np
from std_msgs.msg import String
from geometry_msgs.msg import Twist, PoseStamped
from visualization_msgs.msg import Marker
from nav_msgs.msg import Path

# Camera settings
wCam, hCam = 640, 480  # Resolution
frameR = 100  # Frame reduction for smoother tracking
smoothening = 5  # Not used but can be implemented for smoothing

# Initialize Mediapipe
cap = cv2.VideoCapture(0)  # Use 0 for internal camera, 1 for external
cap.set(3, wCam)
cap.set(4, hCam)

mpHands = mp.solutions.hands
hands = mpHands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
mpDraw = mp.solutions.drawing_utils

# Initialize ROS node and publishers
rospy.init_node('aivirtualmouse_node', anonymous=True)
command_pub = rospy.Publisher('/aivirtualmouse_command', String, queue_size=10)
position_pub = rospy.Publisher('/aivirtualmouse_position', Twist, queue_size=10)
marker_pub = rospy.Publisher('/aivirtualmouse_marker', Marker, queue_size=10)
path_pub = rospy.Publisher('/path', Path, queue_size=10)  # 新增路径发布器

rate = rospy.Rate(30)  # Loop at 30 Hz
marker_id = 0  # Global variable for unique marker IDs
path = Path()  # 初始化路径消息
path.header.frame_id = "world"  # 确保和 RViz 的全局框架一致

def publish_command(command):
    msg = String()
    msg.data = command
    command_pub.publish(msg)
    rospy.loginfo(f"Published command: {command}")

def publish_position(x, y):
    msg = Twist()
    msg.linear.x = x / 100.0  # Convert pixel to position
    msg.linear.y = y / 100.0  # Convert pixel to position
    position_pub.publish(msg)
    rospy.loginfo(f"Published position: x={msg.linear.x}, y={msg.linear.y}")

def publish_marker(x, y, z=0.0):
    marker = Marker()
    marker.header.frame_id = "world"  # 确保和 RViz 的全局框架一致
    marker.header.stamp = rospy.Time.now()
    marker.ns = "aivirtualmouse"
    marker.id = 0  # Marker 的唯一 ID
    marker.type = Marker.SPHERE  # 设置为球形
    marker.action = Marker.ADD  # 确保是添加操作

    # 设置位置
    marker.pose.position.x = x / 100.0
    marker.pose.position.y = y / 100.0
    marker.pose.position.z = z
    marker.pose.orientation.x = 0.0
    marker.pose.orientation.y = 0.0
    marker.pose.orientation.z = 0.0
    marker.pose.orientation.w = 1.0

    # 设置 Marker 的尺寸
    marker.scale.x = 0.1  # 确保尺寸大于零
    marker.scale.y = 0.1
    marker.scale.z = 0.1

    # 设置 Marker 的颜色
    marker.color.a = 1.0  # 透明度 (1.0 为不透明)
    marker.color.r = 1.0  # 红色
    marker.color.g = 0.0  # 绿色
    marker.color.b = 0.0  # 蓝色

    # 发布 Marker
    marker_pub.publish(marker)
    print(f"Published Marker: x={x / 100.0}, y={y / 100.0}, z={z}")

def publish_path(x, y, z=0.0):
    global path
    path.header.stamp = rospy.Time.now()
    pose_stamped = PoseStamped()
    pose_stamped.header.frame_id = "world"
    pose_stamped.header.stamp = rospy.Time.now()
    pose_stamped.pose.position.x = x / 100.0
    pose_stamped.pose.position.y = y / 100.0
    pose_stamped.pose.position.z = z
    pose_stamped.pose.orientation.w = 1.0
    path.poses.append(pose_stamped)
    path_pub.publish(path)
    print(f"Published Path: x={x / 100.0}, y={y / 100.0}, z={z}")

def draw_hands(img, handLms):
    """ Draw hands and connections on the frame """
    for id, lm in enumerate(handLms.landmark):
        h, w, c = img.shape
        cx, cy = int(lm.x * w), int(lm.y * h)
        cv2.circle(img, (cx, cy), 5, (255, 255, 255), cv2.FILLED)
    mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS,
                          mpDraw.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
                          mpDraw.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2))

def fingers_up(handLms):
    """ Check which fingers are up """
    fingers = [False] * 5
    ids = [4, 8, 12, 16, 20]
    for i, id in enumerate(ids):
        if id == 4:  # Thumb
            if handLms.landmark[id].x < handLms.landmark[id - 1].x:
                fingers[i] = True
        else:  # Other fingers
            if handLms.landmark[id].y < handLms.landmark[id - 2].y:
                fingers[i] = True
    return fingers

def main():
    global marker_id
    pTime = 0  # For FPS calculation
    while not rospy.is_shutdown():
        ret, frame = cap.read()
        if not ret:
            rospy.logerr("Failed to capture frame from camera")
            continue

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        rgb_frame.flags.writeable = False

        results = hands.process(rgb_frame)

        rgb_frame.flags.writeable = True
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for hand_id, handLms in enumerate(results.multi_hand_landmarks):
                fingers = fingers_up(handLms)
                rospy.loginfo(f"Fingers up: {fingers}")

                if fingers == [True, False, False, False, False]:  # Thumb up
                    publish_command("hover")
                elif fingers == [False, True, False, False, False]:  # Index finger
                    publish_command("forward")
                    x = handLms.landmark[8].x * wCam
                    y = handLms.landmark[8].y * hCam
                    publish_position(x, y)
                    publish_marker(x, y)
                    publish_path(x, y)  # 添加路径发布
                elif fingers == [False, False, True, False, False]:  # Middle finger
                    publish_command("left")
                elif fingers == [False, False, False, True, False]:  # Ring finger
                    publish_command("right")
                elif fingers == [False, False, False, False, True]:  # Pinky finger
                    publish_command("backward")
                else:
                    publish_command("hover")

                draw_hands(frame, handLms)
        else:
            rospy.loginfo("No hand detected")
            publish_command("hover")

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(frame, f'FPS: {int(fps)}', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('Hand Tracking', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        rate.sleep()

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass