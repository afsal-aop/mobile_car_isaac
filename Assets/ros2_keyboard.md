
# 🎮 Controlling the Robot using ROS 2 (Keyboard)

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
## ⚡ What to Do Next
- Once loaded, proceed with:
- ROS 2 connection
- Control setup (keyboard / joystick)
### [⬅️ Previous](../index.md) | [Next ➡️](../index.md)
