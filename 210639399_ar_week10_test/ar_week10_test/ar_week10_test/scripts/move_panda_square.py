#!/usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
import time
from math import pi
from std_msgs.msg import String
from ar_week10_test.msg import side_of_square
from moveit_commander.conversions import pose_to_list
## END_SUB_TUTORIAL





def initialiser():
    print('init')
    rospy.init_node('move_panda_square')
    rospy.Subscriber('squareside',side_of_square,movepanda)
    print('here')
    rospy.spin()

def movepanda(sqrside):
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    moveit_commander.roscpp_initialize(sys.argv)
    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()

    
    group_name = "panda_arm"
    move_group = moveit_commander.MoveGroupCommander(group_name)

    ## Create a `DisplayTrajectory`_ ROS publisher which is used to display
    ## trajectories in Rviz:
    display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                                   moveit_msgs.msg.DisplayTrajectory,
                                                   queue_size=20)

    
    joint_goal = move_group.get_current_joint_values()
    joint_goal[0] = 0
    joint_goal[1] = -pi/4
    joint_goal[2] = 0
    joint_goal[3] = -pi/2
    joint_goal[4] = 0
    joint_goal[5] = pi/3
    joint_goal[6] = 0

    # The go command can be called with joint values, poses, or without any
    # parameters if you have already set the pose or joint target for the group
    move_group.go(joint_goal, wait=True)

    # Calling ``stop()`` ensures that there is no residual movement
    move_group.stop()

    ## END_SUB_TUTORIAL

   

   
    waypoints = []

    wpose = move_group.get_current_pose().pose
    
    wpose.position.x += sqrside.sqrsize
    waypoints.append(copy.deepcopy(wpose))
    wpose.position.y += sqrside.sqrsize  # and sideways (y)
    waypoints.append(copy.deepcopy(wpose))
    wpose.position.x -= sqrside.sqrsize
    waypoints.append(copy.deepcopy(wpose))
    wpose.position.y -= sqrside.sqrsize
    waypoints.append(copy.deepcopy(wpose))
    

   


    # We want the Cartesian path to be interpolated at a resolution of 1 cm
    # which is why we will specify 0.01 as the eef_step in Cartesian
    # translation.  We will disable the jump threshold by setting it to 0.0,
    # ignoring the check for infeasible jumps in joint space, which is sufficient
    # for this tutorial.
    (plan, fraction) = move_group.compute_cartesian_path(
                                       waypoints,   # waypoints to follow
                                       0.01,        # eef_step
                                       0.0)         # jump_threshold

    display_trajectory = moveit_msgs.msg.DisplayTrajectory()
    display_trajectory.trajectory_start = robot.get_current_state()
    display_trajectory.trajectory.append(plan)
    # Publish
    display_trajectory_publisher.publish(display_trajectory)
    time.sleep(5)
    move_group.execute(plan, wait=True)
  
    
if __name__ == '__main__':
    try:
      initialiser()
      print "============ Python tutorial demo complete!"
    except rospy.ROSInterruptException:
      pass
    except KeyboardInterrupt:
      pass

