#!/usr/bin/env python3

import rospy
import cv2
import numpy as np
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from std_msgs.msg import String

# 摄像头参数
wCam, hCam = 640, 480  # 摄像头分辨率
turtle_sim_size = 11.0  # Turtlesim的坐标范围是(0, 0)到(11, 11)

# 初始化ROS节点
rospy.init_node('turtle_follow_finger', anonymous=True)
turtle_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
rate = rospy.Rate(30)  # 30 Hz

# 小乌龟的当前位置
turtle_pose = Pose()

# 初始化平滑化的手部位置
smoothed_x, smoothed_y = 0, 0
alpha = 0.25  # EWA平滑系数

# 限制速度的最大值
max_linear_speed = 2.0
max_angular_speed = 2.5


def pose_callback(msg):
    """接收小乌龟的当前位置"""
    global turtle_pose
    turtle_pose = msg


# 订阅小乌龟的位置
rospy.Subscriber('/turtle1/pose', Pose, pose_callback)


def follow_finger(finger_x, finger_y):
    """根据手指的位置控制小乌龟"""
    global turtle_pose, smoothed_x, smoothed_y

    # 平滑手部位置
    smoothed_x = smooth_value(smoothed_x, finger_x, alpha)
    smoothed_y = smooth_value(smoothed_y, finger_y, alpha)

    # 将屏幕坐标映射到 Turtlesim 的坐标系
    target_x = max(0, min((smoothed_x / wCam) * turtle_sim_size, turtle_sim_size))
    target_y = max(0, min((smoothed_y / hCam) * turtle_sim_size, turtle_sim_size))

    # 计算小乌龟需要移动的方向
    vel_msg = Twist()

    # 计算小乌龟与目标位置的距离
    distance_x = target_x - turtle_pose.x
    distance_y = target_y - turtle_pose.y

    # 计算线速度和角速度
    linear_speed_gain = 0.3
    angular_speed_gain = 1.0

    vel_msg.linear.x = min(max_linear_speed, linear_speed_gain * np.sqrt(distance_x**2 + distance_y**2))
    vel_msg.angular.z = min(
        max_angular_speed,
        angular_speed_gain * (np.arctan2(distance_y, distance_x) - turtle_pose.theta),
    )

    # 发布速度命令
    turtle_pub.publish(vel_msg)


def smooth_value(smoothed_val, val, alpha):
    """平滑位置计算函数"""
    return alpha * val + (1 - alpha) * smoothed_val


def handle_command(command):
    """处理接收到的指令"""
    rospy.loginfo(f"Received command: {command}")
    if command == "draw":
        rospy.loginfo("Drawing mode activated.")
        # 在这里实现画图逻辑
    elif command == "erase":
        rospy.loginfo("Erasing mode activated.")
        # 在这里实现擦除逻辑
    elif command == "hover":
        rospy.loginfo("Hovering mode activated.")
        # 停止乌龟移动
        turtle_pub.publish(Twist())  # 发布一个空的速度命令


def handle_position(msg):
    """处理接收到的手指位置"""
    x = msg.linear.x
    y = msg.linear.y
    rospy.loginfo(f"Received position: ({x}, {y})")
    follow_finger(x, y)


# 订阅命令和位置
command_sub = rospy.Subscriber('/aivirtualmouse_command', String, handle_command)
position_sub = rospy.Subscriber('/aivirtualmouse_position', Twist, handle_position)

# 主循环
while not rospy.is_shutdown():
    rate.sleep()
