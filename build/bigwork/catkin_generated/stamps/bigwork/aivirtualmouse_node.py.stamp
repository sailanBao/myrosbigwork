#!/usr/bin/env python

import rospy
import cv2
import mediapipe as mp
import numpy as np
import time
from geometry_msgs.msg import Twist
from std_msgs.msg import String

wCam, hCam = 1080, 720
frameR = 100
smoothening = 5

cap = cv2.VideoCapture(0)  # 若使用笔记本自带摄像头则编号为0  若使用外接摄像头 则更改为1或其他编号
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector()
canvas = np.zeros((hCam, wCam, 3), np.uint8)

# 初始化ROS节点
rospy.init_node('aivirtualmouse_node', anonymous=True)
turtle_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
command_pub = rospy.Publisher('/aivirtualmouse_command', String, queue_size=10)
rate = rospy.Rate(30)  # 30 Hz

def publish_command(command):
    msg = String()
    msg.data = command
    command_pub.publish(msg)

def publish_velocity(x, y):
    cmd = Twist()
    cmd.linear.x = x / 100.0  # 将像素值转换为速度值
    cmd.angular.z = y / 100.0  # 将像素值转换为角速度值
    turtle_pub.publish(cmd)

while not rospy.is_shutdown():
    success, img = cap.read()
    if not success:
        rospy.logerr("Error: 无法读取摄像头帧")
        continue

    img = cv2.flip(img, 1)  # 水平翻转，使图像更自然

    # 确保 img 的大小与 wCam, hCam 一致
    img = cv2.resize(img, (wCam, hCam))

    # 1. 检测手部 得到手指关键点坐标
    img = detector.findHands(img)
    cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (0, 255, 0), 2)
    lmList = detector.findPosition(img, draw=False)

    # 2. 判断食指和中指是否伸出
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        fingers = detector.fingersUp()

        # 3. 若只有食指伸出 则进入绘画模式
        if fingers[1] and not fingers[2] and not fingers[3]:
            # 绘制圆心
            cv2.circle(canvas, (x1, y1), 10, (255, 0, 255), -1)
            publish_command("draw")
            publish_velocity(x1, y1)

        # 4. 若是食指和中指都伸出 则检测指头距离 距离够短则对应橡皮擦
        if fingers[1] and fingers[2]:
            length, img, pointInfo = detector.findDistance(8, 12, img)
            if length < 40:
                # 绘制方形图标作为橡皮擦
                cv2.rectangle(canvas, (pointInfo[4] - 20, pointInfo[5] - 20), (pointInfo[4] + 20, pointInfo[5] + 20), (0, 0, 0), -1)
                publish_command("erase")
                publish_velocity(pointInfo[4], pointInfo[5])

        # 5. 若是食指、中指和无名指都伸出 则检测指头悬空
        if detector.isFingerInAir(fingers):
            # 绘制三角形标记当前点
            cv2.drawMarker(img, (x1, y1), (0, 255, 0), cv2.MARKER_TRIANGLE_UP, 20, 2)
            publish_command("hover")
            publish_velocity(x1, y1)

    # 将画布叠加到原始图像上
    gray_canvas = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
    _, inv_canvas = cv2.threshold(gray_canvas, 1, 255, cv2.THRESH_BINARY_INV)
    inv_canvas = cv2.cvtColor(inv_canvas, cv2.COLOR_GRAY2BGR)

    # 确保 inv_canvas 的大小与 img 一致
    if inv_canvas.shape != img.shape:
        inv_canvas = cv2.resize(inv_canvas, (img.shape[1], img.shape[0]))
        canvas = cv2.resize(canvas, (img.shape[1], img.shape[0]))

    img = cv2.bitwise_and(img, inv_canvas)
    img = cv2.bitwise_or(img, canvas)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'fps:{int(fps)}', (15, 25), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)

    # 调整窗口大小和位置
    cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Image", wCam, hCam)
    cv2.moveWindow("Image", 0, 0)

    cv2.imshow("Image", img)
    cv2.imshow("Canvas", canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()