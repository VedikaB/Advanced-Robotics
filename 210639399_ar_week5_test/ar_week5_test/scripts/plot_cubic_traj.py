#!/usr/bin/env python
import rospy
import numpy as np
from ar_week5_test.msg import cubic_traj_params,cubic_traj_coeffs
from std_msgs.msg import Float32

def callback(coeffsdata):
    a0=coeffsdata.a0
    a1=coeffsdata.a1
    a2=coeffsdata.a2
    a3=coeffsdata.a3
    t0=coeffsdata.t0
    tf=coeffsdata.tf
    t=t0
    rate=rospy.Rate(10)
    pos_pub=rospy.Publisher('PositionTrajectory', Float32 , queue_size=10)
    vel_pub=rospy.Publisher('VelocityTrajectory', Float32 , queue_size=10)
    acc_pub=rospy.Publisher('AcclerationTrajectory', Float32 , queue_size=10)
    while t<tf:
        t +=0.1
        PositionTrajectory = a0+a1*t+a2*(pow(t,2))+a3*(pow(t,3))
        VelocityTrajectory = a1*t+2*a2*t+3*a3*(pow(t,2))
        AcclerationTrajectory = 2*a2+6*a3*t
        pos_pub.publish(PositionTrajectory)
        vel_pub.publish(VelocityTrajectory)
        acc_pub.publish(AcclerationTrajectory)
        rate.sleep()

def plot_cubic_traj():
    rospy.init_node('plot_cubic_traj')
    rospy.Subscriber('topic2',cubic_traj_coeffs,callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        plot_cubic_traj()
    except rospy.ROSInterruptException:
        pass
