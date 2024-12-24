#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
import cv2
import numpy as np
import time
import HandTrackingModule as htm

# 手势识别配置
wCam, hCam = 1080, 720
frameR = 100

# 初始化全局变量
command = ""
velocity = Twist()

# 手势检测函数
def detect_hand_command(detector, img, canvas):
    global command, velocity

    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        fingers = detector.fingersUp()

        if fingers[1] and not fingers[2]:  # 食指伸出 -> 绘制模式
            cv2.circle(canvas, (x1, y1), 10, (255, 0, 255), -1)
            command = "draw"
            velocity.linear.x = 0.5  # 示例线速度
            velocity.angular.z = 0.0

        elif fingers[1] and fingers[2]:  # 食指和中指伸出 -> 橡皮擦
            command = "erase"
            velocity.linear.x = 0.0
            velocity.angular.z = 0.5  # 示例角速度

        elif fingers[1] and fingers[2] and fingers[3]:  # 悬空 -> 停止
            command = "hover"
            velocity.linear.x = 0.0
            velocity.angular.z = 0.0

    return img, canvas

# 主函数
def control_turtle_with_hand():
    global command, velocity
    rospy.init_node('turtlesim_hand_controller', anonymous=True)
    command_pub = rospy.Publisher('/aivirtualmouse_command', String, queue_size=10)
    velocity_pub = rospy.Publisher('/aivirtualmouse_velocity', Twist, queue_size=10)

    # 视频采集和手势检测初始化
    cap = cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)
    detector = htm.handDetector()
    canvas = np.zeros((hCam, wCam, 3), np.uint8)

    rate = rospy.Rate(30)  # 30 Hz
    while not rospy.is_shutdown():
        success, img = cap.read()
        if not success:
            print("Error: 无法读取摄像头帧")
            continue

        img = cv2.flip(img, 1)  # 水平翻转
        img = cv2.resize(img, (wCam, hCam))

        # 检测手势并生成指令
        img, canvas = detect_hand_command(detector, img, canvas)

        # 发布指令到 ROS
        command_pub.publish(command)
        velocity_pub.publish(velocity)

        # 显示图像
        cv2.imshow("Image", img)
        cv2.imshow("Canvas", canvas)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        rate.sleep()

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    try:
        control_turtle_with_hand()
    except rospy.ROSInterruptException:
        pass
