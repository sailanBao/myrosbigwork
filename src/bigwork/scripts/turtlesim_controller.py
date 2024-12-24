#!/usr/bin/env python

import rospy
import cv2
import mediapipe as mp
import numpy as np
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from std_msgs.msg import String

# 摄像头参数
wCam, hCam = 640, 480  # 调整分辨率以适配笔记本摄像头
frameR = 100
smoothening = 5

# 初始化摄像头
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

# Mediapipe 手部检测初始化
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

# 初始化ROS节点
rospy.init_node('turtle_follow_finger', anonymous=True)
turtle_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
rate = rospy.Rate(30)  # 30 Hz

# 小乌龟的当前位置
turtle_pose = Pose()

def pose_callback(msg):
    global turtle_pose
    turtle_pose = msg

# 订阅小乌龟的位置
rospy.Subscriber('/turtle1/pose', Pose, pose_callback)

def draw_hands(img, handLms):
    for id, lm in enumerate(handLms.landmark):
        h, w, c = img.shape
        cx, cy = int(lm.x * w), int(lm.y * h)
        cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
    mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

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

def publish_velocity(x, y):
    cmd = Twist()
    cmd.linear.x = x / 100.0  # 将像素值转换为速度值
    cmd.angular.z = y / 100.0  # 将像素值转换为角速度值
    turtle_pub.publish(cmd)

def follow_finger(finger_x, finger_y):
    global turtle_pose

    # 将屏幕坐标映射到 turtlesim 的坐标系
    # turtlesim 的坐标系是 (0, 0) 到 (11, 11)
    target_x = (finger_x / wCam) * 11
    target_y = (finger_y / hCam) * 11

    # 计算小乌龟需要移动的方向
    vel_msg = Twist()

    # 计算小乌龟与目标位置的距离
    distance_x = target_x - turtle_pose.x
    distance_y = target_y - turtle_pose.y

    # 设置线速度和角速度
    vel_msg.linear.x = 1.5 * np.sqrt(distance_x ** 2 + distance_y ** 2)
    vel_msg.angular.z = -4 * (np.arctan2(distance_y, distance_x) - turtle_pose.theta)

    # 发布速度命令
    turtle_pub.publish(vel_msg)

command_sub = rospy.Subscriber('/aivirtualmouse_command', String, lambda msg: handle_command(msg.data))
position_sub = rospy.Subscriber('/aivirtualmouse_position', Twist, lambda msg: handle_position(msg.linear.x, msg.linear.y))

def handle_command(command):
    rospy.loginfo(f"Received command: {command}")
    if command == "draw":
        rospy.loginfo("Drawing mode")
    elif command == "erase":
        rospy.loginfo("Erasing mode")
    elif command == "hover":
        rospy.loginfo("Hovering mode")

def handle_position(x, y):
    rospy.loginfo(f"Received position: ({x}, {y})")
    follow_finger(x, y)

while not rospy.is_shutdown():
    success, img = cap.read()
    if not success:
        rospy.logerr("Error: 无法读取摄像头帧")
        continue

    img = cv2.flip(img, 1)  # 水平翻转，使图像更自然

    # 确保 img 的大小与 wCam, hCam 一致
    img = cv2.resize(img, (wCam, hCam))

    # 1. 检测手部 得到手指关键点坐标
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            draw_hands(img, handLms)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'fps:{int(fps)}', (15, 25), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)

    # 调整窗口大小和位置
    cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Image", wCam, hCam)
    cv2.moveWindow("Image", 0, 0)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()