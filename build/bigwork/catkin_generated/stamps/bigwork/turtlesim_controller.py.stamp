#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String

def command_callback(data):
    global command
    command = data.data

def velocity_callback(data):
    global velocity
    velocity = data

def control_turtle():
    global command, velocity
    rospy.init_node('turtlesim_controller', anonymous=True)
    rospy.Subscriber('/aivirtualmouse_command', String, command_callback)
    rospy.Subscriber('/aivirtualmouse_velocity', Twist, velocity_callback)
    turtle_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(30)  # 30 Hz

    while not rospy.is_shutdown():
        if command == "draw":
            turtle_pub.publish(velocity)
        elif command == "erase":
            turtle_pub.publish(velocity)
        elif command == "hover":
            # 悬空时停止海龟
            cmd = Twist()
            cmd.linear.x = 0.0
            cmd.angular.z = 0.0
            turtle_pub.publish(cmd)
        rate.sleep()

if __name__ == '__main__':
    global command, velocity
    command = ""
    velocity = Twist()
    try:
        control_turtle()
    except rospy.ROSInterruptException:
        pass