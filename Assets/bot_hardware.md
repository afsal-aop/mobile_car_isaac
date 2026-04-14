# ⚙️ Hardware Setup & Circuit Diagram

> _This section explains the physical robot components, wiring, and connections used in the project._

### 🔩 Components Used

- Raspberry Pi 4
- Arduino Nano
- Motor Driver (MDD10A)
- Encoder Motors (2x)
- Wheels + Chassis
- Battery / Power Supply
- Buck Converter
- Connecting Wires

![alt text](./components.png)

## 📌 Connections Overview:

### Raspberry Pi ↔ Arduino (USB)

![alt text](./Pi_Nano.png)

### Arduino Nano ↔ MDD10A Motor Driver

![alt text](./MD_Nano.png)

| Arduino Nano Pin | Motor Driver Pin |
| ---------------- | ---------------- |
| D6               | DIR1             |
| D10              | PWM1             |
| D5               | DIR2             |
| D9               | PWM2             |

### Left Encoder Motor ↔ Motor Driver & Arduino Nano

![alt text](./left_motor.png)

| Encoder Motor Wire | Connection         |
| ------------------ | ------------------ |
| 🔴M1               | M1B (Motor Driver) |
| ⚫M2               | M1A (Motor Driver) |
| 🟣G                | GND (Arduino Nano) |
| 🔵B                | D2 (Arduino Nano)  |
| 🟢A                | D3 (Arduino Nano)  |
| 🟡5V               | 5V (Arduino Nano)  |

### Right Encoder Motor ↔ Motor Driver & Arduino Nano

![alt text](./right_motor.png)
| Encoder Motor Wire | Connection |
|--------------------|-----------|
| 🔴M1 | M2A (Motor Driver) |
| ⚫M2 | M2B (Motor Driver) |
| 🟣G | GND (Arduino Nano) |
| 🔵B | A5 (Arduino Nano) |
| 🟢A | A4 (Arduino Nano) |
| 🟡5V | 5V (Arduino Nano) |

### Power Connections (Battery, Buck Converter, Raspberry Pi, Motor Driver)

![alt text](./power.png)

| From                  | To                   |
| --------------------- | -------------------- |
| Battery (+)           | B+ (Motor Driver)    |
| Battery (−)           | B− (Motor Driver)    |
| Battery (+)           | IN+ (Buck Converter) |
| Battery (−)           | IN− (Buck Converter) |
| OUT+ (Buck Converter) | 5V (Raspberry Pi)    |
| OUT− (Buck Converter) | GND (Raspberry Pi)   |

## 🧠 Connection Logic

1. Raspberry Pi sends commands (ROS 2)
2. Arduino receives commands via USB
3. Arduino controls motors via Motor Driver
4. Motors move the robot

### ⚠️ Important Notes

- Ensure correct voltage for Raspberry Pi (5V only)
- Double-check motor driver wiring before powering
- Loose connections may cause unstable movement

### ✅ Outcome

- All components connected correctly
- Robot hardware ready for control
- Communication between Pi and Arduino established

## ⚡ What to Do Next

- Upload motor control code to Arduino Nano
- Setup Raspberry Pi bridge with motor_bridge.py
- Run script and establish Arduino communication
- Control real robot and sync with simulation 🤖

### [⬅️ Previous](./rpi_setup.md) | [Next ➡️](./hardware_integration.md)
