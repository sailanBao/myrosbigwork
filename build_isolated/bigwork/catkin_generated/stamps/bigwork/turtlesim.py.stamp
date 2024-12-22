import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32MultiArray
from turtlesim.msg import Pose
import math

# 全局变量
current_pose = None

def pose_callback(data):
    global current_pose
    current_pose = data

def hand_position_callback(data):
    global current_pose
    if current_pose is None:
        return

    target_x, target_y = data.data

    # 计算目标方向和距离
    dx = target_x - current_pose.x
    dy = target_y - current_pose.y
    distance = math.sqrt(dx**2 + dy**2)
    angle = math.atan2(dy, dx)

    # 控制海龟的运动
    cmd = Twist()
    if distance > 0.1:  # 如果距离足够大，移动海龟
        cmd.linear.x = 1.5 * distance  # 线速度与距离成比例
        cmd.angular.z = 4.0 * (angle - current_pose.theta)  # 角速度与方向误差成比例
        cmd_pub.publish(cmd)

def main():
    global cmd_pub
    rospy.init_node('turtlesim_controller', anonymous=True)

    # 订阅 Turtlesim 的位置和手势坐标
    rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
    rospy.Subscriber('/hand_position', Float32MultiArray, hand_position_callback)

    # 发布运动控制指令
    cmd_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
