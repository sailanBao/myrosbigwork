#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist, Pose
from std_msgs.msg import String
from nav_msgs.msg import Path

class TurtlesimController:
    def __init__(self):
        rospy.init_node('turtlesim_controller', anonymous=True)
        self.cmd_vel_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.pose_pub = rospy.Publisher('/turtle1/pose', Pose, queue_size=10)  # 添加位姿发布器
        rospy.Subscriber('/aivirtualmouse_command', String, self.command_callback)
        rospy.Subscriber('/aivirtualmouse_position', Twist, self.position_callback)
        rospy.Subscriber('/path', Path, self.path_callback)  # 订阅路径话题
        self.rate = rospy.Rate(30)  # 30 Hz
        self.current_pose = Pose()  # 初始化当前位姿
        self.path = None  # 初始化路径

    def command_callback(self, data):
        command = data.data
        twist = Twist()
        if command == "hover":
            twist.linear.x = 0.0
            twist.angular.z = 0.0
        elif command == "forward":
            twist.linear.x = 2.0  # 增加线速度
            twist.angular.z = 0.0
        elif command == "left":
            twist.linear.x = 0.0
            twist.angular.z = 4.0  # 增加角速度
        elif command == "right":
            twist.linear.x = 0.0
            twist.angular.z = -4.0  # 减少角速度
        elif command == "backward":
            twist.linear.x = -2.0  # 减少线速度
            twist.angular.z = 0.0
        else:
            twist.linear.x = 0.0
            twist.angular.z = 0.0
        self.cmd_vel_pub.publish(twist)
        print(f"Executed {command} command with linear.x={twist.linear.x} and angular.z={twist.angular.z}")

    def position_callback(self, data):
        x = data.linear.x * 100  # 将位置值转换为像素值
        y = data.linear.y * 100  # 将位置值转换为像素值
        print(f"Received position: x={x}, y={y}")
        self.current_pose.position.x = x
        self.current_pose.position.y = y
        self.pose_pub.publish(self.current_pose)  # 发布当前位姿

    def path_callback(self, data):
        self.path = data
        print(f"Received path with {len(data.poses)} poses")
        for pose_stamped in data.poses:
            print(f"Pose at time {pose_stamped.header.stamp}:")
            print(f"  Position: x={pose_stamped.pose.position.x}, y={pose_stamped.pose.position.y}, z={pose_stamped.pose.position.z}")
            print(f"  Orientation: x={pose_stamped.pose.orientation.x}, y={pose_stamped.pose.orientation.y}, z={pose_stamped.pose.orientation.z}, w={pose_stamped.pose.orientation.w}")

    def run(self):
        while not rospy.is_shutdown():
            if self.path:
                # 处理路径逻辑，例如跟随路径
                pass
            self.rate.sleep()

if __name__ == "__main__":
    controller = TurtlesimController()
    controller.run()