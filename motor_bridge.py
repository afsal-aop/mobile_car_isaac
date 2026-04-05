import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import serial

class MotorBridge(Node):
    def __init__(self):
        super().__init__('motor_bridge')

        # Connect to the Arduino via USB
        try:
            self.arduino = serial.Serial('/dev/ttyUSB0', 115200, timeout=0.1)
            self.get_logger().info("Connected to Arduino Nano!")
        except Exception as e:
            self.get_logger().error(f"Failed to connect: {e}")

        # Listen to the /cmd_vel topic
        self.subscription = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.cmd_vel_callback,
            10)

    def cmd_vel_callback(self, msg):
        linear_x = msg.linear.x
        angular_z = msg.angular.z

        # Convert forward speed to PWM base (0 to 255)
        base_speed = linear_x * 255

        # SMART MIXING LOGIC
        if linear_x == 0.0:
            # IN-PLACE ROTATION ('j' or 'l')
            # If we are not moving forward, give it strong power to spin in place.
            # angular_z is usually 1.0 or -1.0. We multiply by 150 to give it good torque.
            left_wheel = -angular_z * 150
            right_wheel = angular_z * 150
        else:
            # CURVED TURNING ('u', 'o', 'm', '.')
            # We only subtract a small amount (35) from the inner wheel.
            # This ensures the PWM stays high enough to defeat the motor "deadband"
            # so the wheel keeps rolling, creating a smooth, sweeping curve.
            turn_power = angular_z * 35 
            
            left_wheel = base_speed - turn_power
            right_wheel = base_speed + turn_power

        # Cap the max speeds between -255 and 255
        left_wheel = max(min(int(left_wheel), 255), -255)
        right_wheel = max(min(int(right_wheel), 255), -255)

        # Format the string exactly how the Arduino expects it: "Left,Right\n"
        command = f"{left_wheel},{right_wheel}\n"

        # Send it over USB!
        if hasattr(self, 'arduino') and self.arduino.is_open:
            self.arduino.write(command.encode('utf-8'))
            self.get_logger().info(f"Sent to Arduino: {command.strip()}")

def main(args=None):
    rclpy.init(args=args)
    node = MotorBridge()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()