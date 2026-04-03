# Airavat 1.0 — Autonomous Rover (ROS 2 Simulation)

Airavat 1.0 is a mobile rover platform for which a complete autonomy stack has been developed and validated in simulation using ROS 2 and Gazebo.

This repository demonstrates the integration of perception, state estimation, mapping, localization, and navigation into a coherent and modular system. The primary objective is to establish a simulation-validated autonomy pipeline that can be transferred to a physical rover.

---

## System Description

Airavat 1.0 is modeled as a differential-drive ground rover operating in a 2D planar environment.

### Sensors

* 2D LiDAR — environment perception
* IMU — inertial measurements
* Wheel Odometry
* Camera — visual input (optional / extensible)

### Capabilities

* Mapping of unknown environments
* Localization in a known map
* Autonomous navigation to user-defined goals

---

## Autonomy Stack

The system is built using standard ROS 2 components:

* **Robot Model** — URDF/Xacro (`airavat_description`)
* **Simulation** — Gazebo (`airavat_bringup`)
* **State Estimation** — EKF via `robot_localization` (`airavat_ekf`)
* **Mapping** — `slam_toolbox` (`airavat_slam`)
* **Localization & Navigation** — Nav2 (`airavat_nav2`)

---

## Architecture

```id="arch-main"
Gazebo Simulation
   │
   ├── Airavat 1.0 (URDF Model)
   │
   ├── Sensor Streams
   │     ├── /scan   (LiDAR)
   │     ├── /imu    (IMU)
   │     └── /image  (Camera)
   │
   ├── State Estimation
   │     └── EKF → /odometry/filtered
   │
   ├── Mapping / Localization
   │     ├── SLAM (map generation)
   │     └── AMCL (pose estimation)
   │
   └── Navigation (Nav2)
         └── /cmd_vel → robot motion
```

---

## Repository Structure

```id="struct-main"
airavat_1.0_ros2_simulation/
│
├── airavat_bringup/       # Simulation launch and system entry point
├── airavat_description/   # Robot model and sensor definitions
├── airavat_ekf/           # State estimation (EKF)
├── airavat_slam/          # Mapping (SLAM Toolbox)
├── airavat_nav2/          # Localization and navigation (Nav2)
```

---

## Build Instructions

```bash id="build-main"
git clone https://github.com/<your-username>/airavat_1.0_ros2_simulation.git
cd airavat_1.0_ros2_simulation

colcon build
source install/setup.bash
```

---

## Execution

### 1. Launch Simulation

```bash id="run-main1"
ros2 launch airavat_bringup gazebo_launch.py
```

---

### 2. Mapping Mode (SLAM)

```bash id="run-main2"
ros2 launch airavat_slam slam_toolbox_launch.py
```

Save the generated map:

```bash id="run-main3"
ros2 service call /slam_toolbox/save_map slam_toolbox/srv/SaveMap "{name: {data: 'my_map2'}}"
```

---

### 3. Navigation Mode

```bash id="run-main4"
ros2 launch airavat_nav2 navigation.launch.py
```

Navigation goals can be set via RViz.

---

## Coordinate Frames

```id="tf-main"
map → odom → base_link → sensor frames
```

---

## Interfaces

### Subscribed Topics

* `/scan` — LiDAR data
* `/imu` — IMU data
* `/cmd_vel` — velocity commands

### Published Topics

* `/odom` — raw wheel odometry
* `/odometry/filtered` — EKF output
* `/tf` — coordinate transforms
* `/map` — occupancy grid

---

## Motion Model

The rover is modeled as a **differential-drive system**, with velocity commands applied through `/cmd_vel`.
Motion execution is handled within the simulation via Gazebo plugins.

---

## Key Outcome

This project demonstrates that Airavat 1.0 can autonomously:

* Construct a map of an unknown environment
* Estimate its pose within that environment
* Plan and execute collision-free paths to target goals

---

## Design Considerations

* Modular package structure for independent development
* Standard ROS 2 interfaces and TF conventions
* Separation of mapping, localization, and navigation pipelines
* Simulation-first approach for validation

---

## Limitations

* Designed for planar (2D) navigation
* Sensor noise models are simplified
* Performance depends on simulation configuration and system resources
* Real-world deployment will require calibration and tuning

---

## Future Work

* Deployment on physical Airavat rover
* Integration of vision-based perception
* Custom planning algorithms (A*, RRT*, MPC)
* Improved robustness under uncertainty

---

## Author

Harshvardhan Shah
Team Kaizen, PDEU

---

