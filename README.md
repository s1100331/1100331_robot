# 1100331_robot 倉儲搬運機器人專案

##  專案簡介
專案為 倉儲搬運機器人模擬系統，包含：
- 差動輪移動控制
- 相機與雷達感測
- Gazebo 模擬環境
- SLAM 建圖與地圖儲存/載入

##  安裝方式
```bash
cd ~/catkin_ws/src
git clone https://github.com/YOUR_USERNAME/1100331_robot.git
cd ..
catkin_make
source devel/setup.bash
```

##  使用方式
```bash
roslaunch 1100331_robot gazebo_slam.launch
rosrun teleop_twist_keyboard teleop_twist_keyboard.py
```

##  建圖與地圖儲存
- 啟動 SLAM：
```bash
roslaunch 1100331_robot slam.launch
```
- 儲存地圖：
```bash
rosrun map_server map_saver -f ~/map
```
- 載入地圖：
```bash
roslaunch 1100331_robot map_nav.launch
```
