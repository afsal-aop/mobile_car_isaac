# 🎮 Joystick Control (Optional)

- You can control the robot using a joystick/game controller.
- If keyboard control is already working, no changes are required in the Action Graph.

### ⚙️ Install & Launch Joystick

**Open a new terminal:**

```bash
    sudo apt update
    sudo apt install ros-humble-joy ros-humble-teleop-twist-joy
    source /opt/ros/humble/setup.bash
    ros2 launch teleop_twist_joy teleop-launch.py
```

### 🔍 Verify Joystick Input

**Open another terminal:**

```bash
    source /opt/ros/humble/setup.bash
    ros2 topic echo /joy
```

- Press buttons on your controller
- Observe the buttons: values changing

### 🎯 Identify Deadman Switch

- Press buttons one by one (R1, R2, A, B, etc.)
- Find the button where value changes from 0 → 1 (typically index 8)
- This button acts as the Deadman Switch
  8th value changing image~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### 🚗 Control the Robot

- Press and hold the Deadman Switch
- Move the left joystick forward
- The robot will start moving in Isaac Sim

## ✅ Outcome

- Robot responds to joystick input
- Smoother and more natural control compared to keyboard

---

## ⚡ What to Do Next

- Once loaded, proceed with:
- ROS 2 connection
- Control setup (keyboard / joystick)

### [⬅️ Previous](./ros2_keyboard.md) | [Next ➡️](./rpi_setup.md)
