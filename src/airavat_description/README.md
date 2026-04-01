# airavat_description

The `airavat_description` package contains the robot model of **Airavat 1.0**, including its URDF/Xacro definitions, meshes, and visualization setup.

It provides the structural and kinematic representation of the rover, and acts as the foundation for simulation, visualization, and integration with the rest of the ROS 2 stack.

---

## Overview

This package defines:

* Robot link-joint structure (kinematics)
* Visual and collision geometry
* Inertial properties for simulation
* Sensor mounting frames
* Mesh assets for visualization

It is used by:

* RViz (visualization)
* Gazebo (simulation)
* Navigation and SLAM components (via TF)

---

## Package Structure

```
airavat_description/
├── urdf/
│   ├── airavat.urdf.xacro      # Main robot model
│   ├── base.xacro             # Chassis definition
│   ├── wheels.xacro           # Wheel joints and geometry
│   └── sensors.xacro          # Sensor frames
│
├── meshes/
│   ├── base/
│   ├── wheels/
│   └── sensors/
│
├── config/
│   └── rviz/
│       └── display.rviz
│
├── launch/
│   └── display.launch.py
│
└── package.xml
```

---

## Modeling Approach

The robot model is built using **Xacro** to keep the design modular and easy to modify.

* **Base**: Defines `base_link`, chassis geometry, and inertia
* **Wheels**: Differential drive configuration with continuous joints
* **Sensors**: Fixed frames for LiDAR, camera, and IMU

This structure allows individual components to be updated without affecting the full model.

---

## Coordinate Frames

The following standard frames are used:

* `base_link` — robot body frame
* `odom` — local reference frame
* `map` — global reference frame

All sensor frames are defined relative to `base_link` to ensure consistency across perception and navigation modules.

---

## Usage

### Visualize the Robot

```bash
ros2 launch airavat_description display.launch.py
```

This launches:

* `robot_state_publisher`
* RViz with a preconfigured view

---

### Validate URDF

```bash
check_urdf <generated_urdf_file>
```

---

### View TF Tree

```bash
ros2 run tf2_tools view_frames
```

---

## Design Considerations

* **Modular Xacro structure** for flexibility
* **Clear frame hierarchy** for compatibility with navigation stack
* **Balanced collision geometry** for efficient simulation
* **Basic inertial modeling** for stable behavior in Gazebo

---

## Future Improvements

* Add transmission interfaces for hardware integration
* Improve inertial accuracy from CAD models
* Extend sensor definitions for simulation plugins
* Parameterize dimensions for multiple rover variants

---

## Maintainer

**Harshvardhan Shah**
Airavat 1.0 — Autonomous Rover

