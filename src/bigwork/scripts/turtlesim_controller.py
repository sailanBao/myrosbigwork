#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String

class TurtlesimController:
    def __init__(self):
        rospy.init_node('turtlesim_controller', anonymous=True)
        self.cmd_vel_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        rospy.Subscriber('/aivirtualmouse_command', String, self.command_callback)
        rospy.Subscriber('/aivirtualmouse_position', Twist, self.position_callback)
        self.rate = rospy.Rate(30)  # 30 Hz

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

    def run(self):
        while not rospy.is_shutdown():
            self.rate.sleep()

if __name__ == "__main__":
    controller = TurtlesimController()
    controller.run()