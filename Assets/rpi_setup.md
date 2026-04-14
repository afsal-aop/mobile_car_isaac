# 🍓 Raspberry Pi Setup (Ubuntu + ROS 2)

To run ROS 2 on the physical robot, you need to install Ubuntu OS on the Raspberry Pi and set up the environment.

## 💿 Flash Ubuntu (Using Raspberry Pi Imager)

### 1. Install and open Raspberry Pi Imager

![imager app icon](./imager_icon.png)

### 2. Choose Device → Raspberry pi4

![choose device section](./imager_device.png)

### 3. Choose OS → Other general-purpose OS

![choose os section](./imager_other_os.png)

### 4. Select Ubuntu

![other general-purpose os](./imager_os.png)

### 5. Select Ubuntu Version → Ubuntu Desktop 22.04...(64-bit)

![ubuntu versions](./imager_ubuntu.png)

### 6. Choose Storage → Select your SD Card

![storage section](./imager_storage.png)

### 7. Click Write and wait until the process completes

![write section](./imager_write.png)

### ⚙️ Initial Setup

### 1.Insert the SD card into the Raspberry Pi

![alt text](insert_memory.png)

### 2.Power ON the device

![alt text](rpi_interface.DNG)

### 3.Complete basic Ubuntu setup

### 4.Connect to the same Wi-Fi network as your PC

### 🔗 Connect via SSH

```bash
    ssh username@<your_ip_address>
```

- Replace with your actual username and IP address

- Example:
  `ssh raspi@192.168.247.85`

### 📦 Install ROS 2

```bash
    sudo apt update
    sudo apt install ros-humble-desktop
    source /opt/ros/humble/setup.bash
```

### ✅ Outcome

- Ubuntu successfully installed on Raspberry Pi
- ROS 2 environment ready
- Raspberry Pi accessible remotely via SSH

---

## ⚡ What to Do Next

- Assemble all hardware components and complete wiring
- Verify circuit connections using the diagram
- Power the system and check basic motor response
- Proceed with Raspberry Pi control and ROS 2 integration

### [⬅️ Previous](./ros2_joystick.md) | [Next ➡️](./bot_hardware.md)
