Code developed by Vedika Barde, QMUL
Student ID - 210639399

To create the package
1. catkin_create_pkg ar_week5_test std_msgs rospy (Only python file dependancy) and package is build using catkin_make command.
2. Inside this folder launch,msg,scripts,srv are created along with CMakeLists.txt and package.xml already created.
3. After respective files are created in the respective folder, added the dependancies in package.xml and added the respective lines in CMakeLists.txt
4. After creating .py files , chmod +x python_file_name.py this command is used to make python file executable.


To see to check whether the output is coming properly
1. To launch - roslaunch ar_week4_test cubic_traj_gen.launch command is used.
2. To get the graph of active nodes, rqt_graph command is used
3. To see the plot, rosrun rqt_plot rqt_plot command is uesd.

To run the package
1.unzip the folder ar_week5_test.zip
2. build catkin_workspace and run the launch file using roslaunch ar_week4_test cubic_traj_gen.launch command.
