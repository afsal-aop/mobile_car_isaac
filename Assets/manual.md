# Option 3: Want to build the robot from scratch? (Manually)

- 🛠️ Build a Simple Mobile Robot (Manual – Learning Purpose)
- ⚠️ This is a basic model for learning Isaac Sim.
- 👉 It is not an accurate or realistic robot, just to understand fundamentals.

## 🧱 Create Basic Structure

### 1.Create → Physics → Physics Scene

![alt text](./create_phy_scene.png)  
_Initializes a physics simulation environment to enable realistic physical interactions within the scene._

### 2.Create → Physics → Ground Plane

![alt text](./create_gnd_plane.png)  
_Adds a ground surface to the scene to provide a stable reference and enable collision interactions with objects._

### Add body: Create → Shape → Cube

![alt text](./create_cube.png)  
_Creates a cube primitive to serve as the main body structure of the mobile robot within the simulation._

### Set: Translate Z = 1.0, Scale = (2,1,0.5)

![alt text](./cube_property.png)  
_Adjusts the body’s position and dimensions to elevate it above the ground and define the desired size and proportions of the mobile robot._

### Add wheel: Create → Shape → Cylinder

![alt text](./create_wheel.png)  
_Creates a cylindrical primitive to represent the wheel component of the mobile robot for movement simulation._
**Set:**
![alt text](./wheel_property.png)
Height = 0.5  
Translate = (0, 0.75, 1.0)
Rotate = (90, 0, 0)
Scale = (1,3,1)
Rename → left_wheel

### 🔁 Duplicate Wheel do the same steps

![alt text](./wheel_duplicate.png)  
Duplicate left_wheel
Change: Translate Y = -0.75
Rename → right_wheel

### ⚙️ Add Physics

![alt text](./adding_collider_preset.png)

1. Select: body + wheels
2. Add: Physics → Rigid Body with Colliders

### 🔗 Add Wheel Joints

![alt text](./wheel_joint.png)

1. Select body + wheel
2. Create: Physics → Joint → Revolute Joint
3. Repeat for both wheels

![alt text](./wheel_joint_created.png)  
_Creates a revolute joint to enable rotational motion between connected components, allowing the wheels to spin relative to the robot body._

### ⚙️ Configure Joints

![alt text](./joint_axis.png)  
_Set: Axis → Y_

![alt text](./joint_rotation.png)  
_Local Rotation0 = 0 | Local Rotation1 X = -90_

### ▶️ Test Physics

Car falling on ground
Click Play ▶️
👉 Robot should fall onto ground
![alt text](./car_falling.gif)

### ⚡ Add Movement

![alt text](./enable_angular_drive.png)

1. Select both joints
2. Add: Physics → Angular Drive

![alt text](./set_velocity.png)  
_Set: Damping = 10000 | Target Velocity = 100_
![alt text](./car_velocity.gif)

### ✅ Outcome

- Simple 2-wheel robot created
- Basic movement working
- Ready for further control integration

---

## ⚡ What to Do Next

- Enable ROS 2 Bridge in Isaac Sim
- Setup Action Graph with required nodes
- Configure /cmd_vel, wheel values & joints
- Run teleop and control using keyboard 🚗

### [⬅️ Previous](../README.md) | [Next ➡️](./ros2_keyboard.md)
