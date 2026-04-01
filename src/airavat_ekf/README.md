# airavat_ekf

The `airavat_ekf` package contains configuration and launch support for state estimation using an Extended Kalman Filter (EKF).

It is used to fuse sensor data (such as odometry and IMU) to produce a consistent estimate of the robot’s state.

---

## Overview

This package provides:

* EKF configuration for sensor fusion
* State estimation for position and orientation
* Filtered odometry for downstream modules

It improves robustness and accuracy compared to raw sensor data.

---

## Package Structure

```
airavat_ekf/
├── config/
│   └── ekf.yaml
│
├── launch/
│   └── ekf.launch.py
│
└── package.xml
```

---

## Usage

```bash
ros2 launch airavat_ekf ekf.launch.py
```

---

## Design Considerations

* Sensor fusion for improved localization
* Configurable noise and covariance parameters
* Compatible with navigation and SLAM pipelines

---

## Future Improvements

* Add more sensor inputs (GPS, wheel encoders refinement)
* Tune covariance parameters for better accuracy

---

## Maintainer

**Harshvardhan Shah**
Airavat 1.0 — Autonomous Rover

