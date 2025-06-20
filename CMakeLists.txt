cmake_minimum_required(VERSION 3.0.2)
project(1100331_robot)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  sensor_msgs
  geometry_msgs
  nav_msgs
  tf
  xacro
  urdf
  robot_state_publisher
  joint_state_publisher
  teleop_twist_keyboard
  gmapping
)

catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)


catkin_install_python(PROGRAMS
  scripts/arm_control.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
