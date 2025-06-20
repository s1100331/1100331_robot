#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64

def move_arm():
    rospy.init_node('arm_control_node')
    shoulder_pub = rospy.Publisher('/shoulder_joint_position_controller/command', Float64, queue_size=10)
    elbow_pub = rospy.Publisher('/elbow_joint_position_controller/command', Float64, queue_size=10)
    rate = rospy.Rate(1)

    angle = 0.5
    while not rospy.is_shutdown():
        shoulder_pub.publish(angle)
        elbow_pub.publish(-angle)
        angle = -angle
        rate.sleep()

if __name__ == '__main__':
    try:
        move_arm()
    except rospy.ROSInterruptException:
        pass
