#!/usr/bin/env python

import rospy
import cv2
import mediapipe as mp
import time
import numpy as np  # 确保导入 numpy

from std_msgs.msg import String  # 修正导入
from geometry_msgs.msg import Twist  # 修正导入

wCam, hCam = 640, 480  # 调整分辨率以适配笔记本摄像头
frameR = 100
smoothening = 5

cap = cv2.VideoCapture(0)  # 若使用笔记本自带摄像头则编号为0  若使用外接摄像头 则更改为1或其他编号
cap.set(3, wCam)
cap.set(4, hCam)

mpHands = mp.solutions.hands
hands = mpHands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
mpDraw = mp.solutions.drawing_utils

# 初始化ROS节点
rospy.init_node('aivirtualmouse_node', anonymous=True)
command_pub = rospy.Publisher('/aivirtualmouse_command', String, queue_size=10)
position_pub = rospy.Publisher('/aivirtualmouse_position', Twist, queue_size=10)
rate = rospy.Rate(30)  # 30 Hz

def publish_command(command):
    msg = String()
    msg.data = command
    command_pub.publish(msg)
    print(f"Published command: {command}")

def publish_position(x, y):
    msg = Twist()
    msg.linear.x = x / 100.0  # 将像素值转换为位置值
    msg.linear.y = y / 100.0  # 将像素值转换为位置值
    position_pub.publish(msg)
    print(f"Published position: x={msg.linear.x}, y={msg.linear.y}")

def draw_hands(img, handLms):
    for id, lm in enumerate(handLms.landmark):
        h, w, c = img.shape
        cx, cy = int(lm.x * w), int(lm.y * h)
        cv2.circle(img, (cx, cy), 5, (255, 255, 255), cv2.FILLED)
    mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS, 
                          mpDraw.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
                          mpDraw.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2))

def fingers_up(handLms):
    fingers = [False] * 5
    ids = [4, 8, 12, 16, 20]  # 手指关键点的 id
    for i, id in enumerate(ids):
        if id == 4:  # 拇指
            if handLms.landmark[id].x < handLms.landmark[id - 1].x:
                fingers[i] = True
        else:  # 食指、中指、无名指、小指
            if handLms.landmark[id].y < handLms.landmark[id - 2].y:
                fingers[i] = True
    return fingers

def find_distance(p1, p2, handLms, img, draw=True):
    x1, y1 = int(handLms.landmark[p1].x * wCam), int(handLms.landmark[p1].y * hCam)
    x2, y2 = int(handLms.landmark[p2].x * wCam), int(handLms.landmark[p2].y * hCam)
    cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
    length = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    if draw:
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
        cv2.circle(img, (x1, y1), 10, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (cx, cy), 10, (0, 0, 255), cv2.FILLED)
    return length, img, [x1, y1, x2, y2, cx, cy]

def is_finger_in_air(fingers):
    return all(fingers[1:4])

def main():
    pTime = 0  # 初始化 pTime 变量
    while not rospy.is_shutdown():
        ret, frame = cap.read()
        if not ret:
            rospy.logerr("Failed to capture frame from camera")
            continue

        # 将图像从 BGR 转换为 RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        rgb_frame.flags.writeable = False

        # 处理图像以检测手部
        results = hands.process(rgb_frame)

        rgb_frame.flags.writeable = True
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for hand_id, handLms in enumerate(results.multi_hand_landmarks):
                fingers = fingers_up(handLms)
                print(f"Fingers up: {fingers}")

                # 根据手指的状态发布命令
                if fingers == [True, False, False, False, False]:  # 伸出拇指
                    publish_command("hover")
                elif fingers == [False, True, False, False, False]:  # 伸出食指
                    publish_command("forward")
                    x = handLms.landmark[8].x * wCam
                    y = handLms.landmark[8].y * hCam
                    publish_position(x, y)
                elif fingers == [False, False, True, False, False]:  # 伸出中指
                    publish_command("left")
                elif fingers == [False, False, False, True, False]:  # 伸出无名指
                    publish_command("right")
                elif fingers == [False, False, False, False, True]:  # 伸出小拇指
                    publish_command("backward")
                else:
                    publish_command("hover")

                # 绘制手部关键点
                draw_hands(frame, handLms)
        else:
            print("No hand detected")
            publish_command("hover")

        # 显示图像
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(frame, f'FPS: {int(fps)}', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('Hand Tracking', frame)

        # 检查是否按下 'q' 键退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        rate.sleep()

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()