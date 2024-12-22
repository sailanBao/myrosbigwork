import cv2
import rospy
from std_msgs.msg import Float32MultiArray  # 发布手势坐标

def hand_tracker():
    rospy.init_node('hand_tracker', anonymous=True)
    pub = rospy.Publisher('/hand_position', Float32MultiArray, queue_size=10)
    cap = cv2.VideoCapture(0)

    while not rospy.is_shutdown():
        ret, frame = cap.read()
        if not ret:
            break

        # 假设手指是红色，用颜色检测找到手指位置
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_red = (0, 100, 100)
        upper_red = (10, 255, 255)
        mask = cv2.inRange(hsv, lower_red, upper_red)
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            # 找到最大的红色区域
            largest_contour = max(contours, key=cv2.contourArea)
            (x, y), radius = cv2.minEnclosingCircle(largest_contour)

            if radius > 5:  # 如果手指足够大，认为有效
                # 映射到 Turtlesim 的坐标系 (11x11 的网格)
                x_mapped = x / frame.shape[1] * 11.0
                y_mapped = (frame.shape[0] - y) / frame.shape[0] * 11.0
                position_msg = Float32MultiArray(data=[x_mapped, y_mapped])
                pub.publish(position_msg)

        # 显示图像
        cv2.imshow("Hand Tracking", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
