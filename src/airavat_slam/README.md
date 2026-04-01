# airavat_slam

The `airavat_slam` package provides configuration and launch files for performing Simultaneous Localization and Mapping (SLAM) using the Airavat 1.0 rover.

It enables the robot to build a map of an unknown environment while estimating its own pose.

---

## Overview

This package includes:

* SLAM configuration (e.g., for `slam_toolbox`)
* Launch files for mapping workflows
* Parameters tuned for the Airavat platform

---

## Package Structure

```
airavat_slam/
├── config/
│   └── slam_params.yaml
│
├── launch/
│   └── slam.launch.py
│
└── package.xml
```

---

## Usage

```bash
ros2 launch airavat_slam slam.launch.py
```

---

## Design Considerations

* Designed for 2D LiDAR-based SLAM
* Compatible with Nav2 and TF tree
* Parameter tuning focused on simulation environment

---

## Future Improvements

* Map saving and loading workflows
* Multi-session mapping support
* Improved parameter tuning for real-world deployment

---

## Maintainer

**Harshvardhan Shah**
Airavat 1.0 — Autonomous Rover

