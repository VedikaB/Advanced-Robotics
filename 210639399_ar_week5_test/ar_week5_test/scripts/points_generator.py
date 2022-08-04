#!/usr/bin/env python

import rospy
import random
from ar_week5_test.msg import cubic_traj_params
def talker():
    pub = rospy.Publisher('topic1',cubic_traj_params,queue_size=10)
    rospy.init_node('points_generator', anonymous=True)
    rate = rospy.Rate(0.05)
    #rate = rospy.Rate(1)
    msg=cubic_traj_params()  
    
    while not rospy.is_shutdown():
        p0=random.uniform(-10,10)
        pf=random.uniform(-10,10)
        v0=random.uniform(-10,10)
        vf=random.uniform(-10,10)
        t0 = 0
        tf = t0 + random.uniform(5,10)
        msg.p0=p0
        msg.pf=pf
        msg.v0=v0
        msg.vf=vf
        msg.t0=t0
        msg.tf=tf
        print "{p0}\n {v0}\n {t0}\n {pf}\n {vf}\n {tf}\n".format(p0=p0, v0=v0, t0=t0, pf=pf, vf=vf, tf=tf)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    print('inside point')
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
