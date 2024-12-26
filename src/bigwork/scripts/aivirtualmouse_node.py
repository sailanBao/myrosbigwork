import rospy
import mediapipe as mp
from geometry_msgs.msg import Twist
import cv2  # 用于捕获摄像头图像

# 初始化 ROS 节点
rospy.init_node('aivirtualmouse_node', anonymous=True)

# 创建 MediaPipe 手部模型
mpHands = mp.solutions.hands
hands = mpHands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
mpDraw = mp.solutions.drawing_utils

# 创建 Twist 发布者
cmd_vel_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

# 定义手指抬起的函数
def fingers_up(handLms):
    fingers = []
    for i in range(5):  # 5 个手指
        if len(handLms.landmark) >= mpHands.HandLandmark.INDEX_FINGER_TIP + i * 4 + 1:
            if handLms.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP + i * 4].y < handLms.landmark[mpHands.HandLandmark.INDEX_FINGER_PIP + i * 4].y:
                fingers.append(1)  # 手指抬起
            else:
                fingers.append(0)  # 手指放下
        else:
            fingers.append(0)  # 如果索引超出范围，假设手指放下
    return fingers

# 定义发布命令的函数
def publish_command(command):
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
        twist.angular.z = -4.0  # 增加角速度
    elif command == "backward":
        twist.linear.x = -2.0  # 减少线速度
        twist.angular.z = 0.0
    else:
        twist.linear.x = 0.0
        twist.angular.z = 0.0
    cmd_vel_pub.publish(twist)
    print(f"Published {command} command with linear.x={twist.linear.x} and angular.z={twist.angular.z}")

# 定义主函数
def main():
    cap = cv2.VideoCapture(0)  # 打开摄像头

    if not cap.isOpened():
        rospy.logerr("Failed to open camera")
        return

    rate = rospy.Rate(30)  # 提高发布频率到 30 Hz

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
                if fingers == [1, 0, 0, 0, 0]:  # 伸出食指
                    publish_command("forward")
                elif fingers == [0, 1, 0, 0, 0]:  # 伸出中指
                    publish_command("left")
                elif fingers == [0, 0, 1, 0, 0]:  # 伸出无名指
                    publish_command("right")
                elif fingers == [0, 0, 0, 1, 0]:  # 伸出小拇指
                    publish_command("backward")
                else:
                    publish_command("hover")

                # 绘制手部关键点
                mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)
        else:
            print("No hand detected")

        # 显示图像
        cv2.imshow('Hand Tracking', frame)

        # 检查是否按下 'q' 键退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        rate.sleep()

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()