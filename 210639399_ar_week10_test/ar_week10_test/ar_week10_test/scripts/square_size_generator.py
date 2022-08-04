#!/usr/bin/env python

import rospy
import random
from ar_week10_test.msg import side_of_square
def talker():
    pub = rospy.Publisher('squareside',side_of_square,queue_size=10)
    rospy.init_node('side_of_square_generator', anonymous=True)
    rate = rospy.Rate(0.05)
    #rate = rospy.Rate(1)
    msg=side_of_square()  
    
    while not rospy.is_shutdown():
        msg.sqrsize=random.uniform(0.05,0.20)
        print (msg.sqrsize)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    print('inside point')
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

