# airavat_bringup

The `airavat_bringup` package provides the launch and configuration files required to initialize the complete Airavat 1.0 system in ROS 2.

It acts as the entry point for running the robot by orchestrating core nodes such as state publishing, localization, mapping, and navigation.

---

## Overview

This package is responsible for:

* Launching the robot description and TF tree
* Starting simulation or real-world interfaces
* Initializing SLAM or localization pipelines
* Bringing up navigation components
* Managing system-level configurations

It serves as the integration layer that connects all individual packages into a working system.

---

## Package Structure

```
airavat_bringup/
├── launch/
│   └── gazebo_launch.py        # Launches the simulation setup
│
└── package.xml
```

airavat_bringup/
├── launch/
│   ├── bringup.launch.py        # Main system launch file
│   ├── simulation.launch.py     # Launch for Gazebo simulation
│   ├── navigation.launch.py     # Navigation stack
│   └── slam.launch.py           # SLAM setup
│
├── config/
│   ├── nav2_params.yaml         # Navigation parameters
│   ├── slam_params.yaml         # SLAM configuration
│   └── robot_params.yaml        # General robot parameters
│
└── package.xml

````

---

## System Bringup

The bringup process in this package is currently focused on simulation.

- Launches the simulation environment
- Loads the robot model and TF tree
- Starts required nodes for visualization and interaction

---

## Usage

### Launch Simulation

```bash
ros2 launch airavat_bringup gazebo_launch.py
````

This launches the Gazebo simulation along with the required robot description and supporting nodes.

---

## Design Considerations

* **Modular launch files** for different operation modes
* **Clear separation of configuration and execution**
* **Scalable structure** for adding new subsystems
* **Consistent parameter management** using YAML files

---

## Integration

This package integrates:

* `airavat_description` for robot model
* Simulation environment (Gazebo)
* Navigation stack (Nav2)
* SLAM tools (e.g., slam_toolbox)

---

## Future Improvements

* Add hardware bringup support
* Improve launch parameter flexibility
* Introduce lifecycle management for nodes
* Add diagnostics and logging integration

---

## Maintainer

**Harshvardhan Shah**
Airavat 1.0 — Autonomous Rover

