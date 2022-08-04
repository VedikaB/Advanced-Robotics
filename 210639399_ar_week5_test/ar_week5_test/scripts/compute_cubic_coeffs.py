#!/usr/bin/env python

import rospy
import numpy
from ar_week5_test.srv import (compute_cubic_traj,compute_cubic_trajResponse)
def get_params(req):
    #rospy.loginfo('get_params')
    A=numpy.array([[1,req.t0,pow(req.t0,2),pow(req.t0,3)],
		   [0,1,2*req.t0,3*pow(req.t0,2)],
                   [1,req.tf,pow(req.tf,2),pow(req.tf,3)],
                   [0,1,2*req.tf,3*pow(req.tf,2)]])
    B=numpy.array([[req.p0],[req.v0],[req.pf],[req.vf]])
    C=numpy.matmul((numpy.linalg.inv(A)),B)
    response = compute_cubic_trajResponse(C[0][0],C[1][0],C[2][0],C[3][0])
    return response

def main():
    rospy.init_node('landmark_server')
    get_params_service = rospy.Service('get_params',compute_cubic_traj,get_params)
    rospy.spin()

if __name__ == '__main__':
    main()

