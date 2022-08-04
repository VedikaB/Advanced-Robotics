#!/usr/bin/env python

import rospy
from ar_week5_test.srv import compute_cubic_traj,compute_cubic_trajRequest
from ar_week5_test.msg import cubic_traj_params,cubic_traj_coeffs

def callback(data):
    #rospy.loginfo(data.p0, data.pf,data.v0,data.vf,data.t0,data.tf)
    compute_coeffs_service=rospy.ServiceProxy('get_params',compute_cubic_traj)
    response=compute_coeffs_service(compute_cubic_trajRequest(data.p0, data.pf,data.v0,data.vf,data.t0,data.tf))
    pub2=rospy.Publisher('topic2',cubic_traj_coeffs,queue_size=10)
    pub2.publish(response.a0,response.a1,response.a2,response.a3,data.t0,data.tf)
    print (response.a0)
def listener():

    rospy.init_node('custom_listener', anonymous=True)
    rospy.Subscriber("topic1", cubic_traj_params, callback)
    
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()

