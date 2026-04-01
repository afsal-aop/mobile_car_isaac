# Digital Twin Mobile Robot using Isaac Sim + ROS 2

## 📌 Overview
This project is a Digital Twin of a Two-Wheeled Mobile Robot built using NVIDIA Isaac Sim and integrated with ROS 2 (Humble).

### This project is designed in such a way that:
- A beginner can understand and run it
- A developer can extend it
- A robotics learner can build their own robot
---
## 🧠 Project Architecture
The project consists of 3 main parts:
### 1. 🖥️ Simulation (Isaac Sim)
- 3D robot model
- Physics simulation
- Sensors (Camera, LiDAR)
- Action Graph for control
### 2. 🔗 Middleware (ROS 2)
- Communication bridge
- Topic-based control (/cmd_vel)
- Keyboard + Joystick input
### 3. ⚙️ Hardware (Real Robot)
- Raspberry Pi (Ubuntu + ROS 2)
- Arduino Nano (Motor control)
- Buck Converter
- DC Motors + Motor Driver

---
## ⚙️ Requirements
### 🖥️ Software
Install the following:
- Ubuntu 22.04
- ROS 2 Humble
- NVIDIA Isaac Sim
- Python 3.10
---
## 🚀 Launching Isaac Sim
After successfully installing all the required software, the next step is to launch NVIDIA Isaac Sim with the ROS 2 environment properly configured.

### 📌 Step 1: Source ROS 2 Environment
Before opening Isaac Sim, you must source the ROS 2 setup file. This ensures that all ROS 2 commands and packages are available in your terminal session.

`source /opt/ros/humble/setup.bash`

*⚠️ Important:*
This step must be performed every time you open a new terminal before working with ROS 2 or Isaac Sim.

### 📌 Step 2: Launch Isaac Sim
Navigate to your Isaac Sim installation directory and run the startup script.

`/home/tiger/isaac-sim/isaac-sim.sh`

🔁 Replace /home/tiger/isaac-sim/ with the actual path where Isaac Sim is installed on your system.

### ✅ Expected Result
- Isaac Sim application will launch
- You will see the main interface with viewport, stage, and tool panels
- The environment is now ready for simulation and ROS 2 integration
---
## 🏗️ Robot Setup Options

### Option 1: Use Pre-Built Model (Recommended)

If you want to quickly run the project:
- Open Isaac Sim
- Load the provided file:  
 [Download USD Model](./abc.usd)
- Continue with ROS 2 integration steps

✅ This is the fastest way to get started



### 🏗️ Option 2: Build the Robot from Scratch (Using Python Scripts)

If you want to understand how the robot is designed programmatically, you can build it using the Python scripts provided in this repository.
- All component-level scripts are available inside:  
`digital_twin_isaac/`  
*Each file is responsible for creating a specific part of the robot (wheels, base, motors, etc.), and the complete robot can be generated using the main script.*  
![Script_Editor](./Images/script_editor.jpg)
- Copy the Python code (e.g., wheel.py or any component file)
- Open Isaac Sim
- Go to:
`Window → Script Editor`
- Select the Python tab
- Paste the code
- Click Run ▶️

### Option 3: Want to build the robot from scratch? (Manually)

Check the detailed guide here:  
👉 [Build_from_scratch](./build_from_scratch.md)

---

## 🎮 Controlling the Robot using ROS 2 (Keyboard)

After building the robot, the next step is to connect it with ROS 2 and control it using the keyboard.  
**🔗 Enable ROS 2 Bridge**  
ros2_bridge_library img ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Open Isaac Sim
- Go to: `Window → Extensions`
- Search ROS 2
- Enable: Omni.isaac.ros2_bridge

### 🧩 Setup Action Graph
action graph image ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Go to:
  `Window → Visual Scripting → Action Graph`
- Create a new graph  
**Add nodes:**
- On Playback Tick
- ROS2 Subscribe Twist
- Differential Controller
- Articulation Controller

👉 Connect them as shown in the image


### ⚙️ Node Configuration (Important)

Configure each node as follows:
-  ROS2 Subscribe Twist
   - Set Topic Name → /cmd_vel
   - (Node ID can be left as default)  
👉 This receives movement commands from ROS 2  

-  Differential Controller
   - Set Wheel Distance → distance between left & right wheels (e.g., 0.15)
   - Set Wheel Radius → radius of wheel (e.g., 0.033)  
👉 These values control how accurately the robot moves and turns  

-  Articulation Controller
   - Enable Use Path ✅
   - Set Robot Path → select your robot (e.g., /World/TCE_Bot)
   - Set Joint Names:  
 `["left_wheel_joint", "right_wheel_joint"]`  
👉 Make sure names exactly match your wheel joints

**⚠️ Note**  
Wrong wheel values → incorrect turning  
Wrong joint names → robot will not move


### ▶️ Run & Control
- Click Play ▶️ in Isaac Sim
- Open terminal:  
`source /opt/ros/humble/setup.bash`  
`ros2 run teleop_twist_keyboard teleop_twist_keyboard`  
- Use keys:  
  - i → forward  
  - j / l → turn  
  - k → stop
    
*✅ Result*  
Robot responds to keyboard input  
Moves forward, turns, and stops in simulation  

---
