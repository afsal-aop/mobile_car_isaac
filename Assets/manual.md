### Option 3: Want to build the robot from scratch? (Manually)

Check the detailed guide here:  
👉 [Build_from_scratch](./build_from_scratch.md)

---

🛠️ Build a Simple Mobile Robot (Manual – Learning Purpose)

⚠️ This is a basic model for learning Isaac Sim.
👉 It is not an accurate or realistic robot, just to understand fundamentals.

🧱 Create Basic Structure

Steps

### 1.Create → Physics → Physics Scene

img~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### 2.Create → Physics → Ground Plane

img~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Add body:

### 1.Create → Shape → Cube

img~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Set: Translate Z = 1.0, Scale = (2,1,0.5)
img~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Add wheel:

### Create → Shape → Cylinder

img~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Set:
Height = 0.5 img~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Translate = (0, 0.75, 1.0)
Rotate = (90, 0, 0)
Scale = (1,3,1)
Rename → left_wheel img~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### 🔁 Duplicate Wheel do the same steps

img~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
📸 Image to add:

Two wheels on both sides
Duplicate left_wheel
Change: Translate Y = -0.75
Rename → right_wheel

### ⚙️ Add Physics

Physics properties panel
img~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Select: body + wheels
img~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Add: Physics → Rigid Body with Colliders
img~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### 🔗 Add Wheel Joints

Revolute joint connection
Select body + wheel
img~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Create:
Physics → Joint → Revolute Joint
img~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Repeat for both wheels

### ⚙️ Configure Joints

Joint settings panel
img~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Set:
Local Rotation:
0 = 0
1 = X = -90
Axis → Y
img~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### ▶️ Test Physics

Car falling on ground
Click Play ▶️
👉 Robot should fall onto ground
img~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### ⚡ Add Movement

Angular drive settings
Select both joints → Add:
img~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Physics → Angular Drive
img~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Set:
Damping = 10000
Target Velocity = 100
img~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### ✅ Outcome

- Simple 2-wheel robot created
- Basic movement working
- Ready for further control integration

---

## ⚡ What to Do Next

- Once loaded, proceed with:
- ROS 2 connection
- Control setup (keyboard / joystick)

### [⬅️ Previous](../index.md) | [Next ➡️](./ros2_keyboard.md)
