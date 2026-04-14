import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, TransformStamped
from nav_msgs.msg import Odometry
from tf2_ros import TransformBroadcaster
from sensor_msgs.msg import JointState  # already there, good
import serial
import math

class MotorBridge(Node):
    def __init__(self):
        super().__init__('motor_bridge')

        # --- ROBOT PHYSICAL SPECS ---
        self.WHEEL_RADIUS = 0.0325
        self.TICKS_PER_REV = 440
        self.WHEEL_BASE = 0.18
        
        # --- ODOMETRY TRACKING VARIABLES ---
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0
        self.prev_left_ticks = 0
        self.prev_right_ticks = 0
        self.first_read = True


        
        # --- ROS 2 PUBLISHERS ---
        self.odom_pub = self.create_publisher(Odometry, '/odom', 10)
        self.tf_broadcaster = TransformBroadcaster(self)



        # Connect to the Arduino
        try:
            self.arduino = serial.Serial('/dev/ttyUSB0', 115200, timeout=0.01)
            self.get_logger().info("Connected to Arduino! Odometry Active.")
        except Exception as e:
            self.get_logger().error(f"Failed to connect: {e}")

        # Subscribe to Keyboard commands
        self.subscription = self.create_subscription(Twist, '/cmd_vel', self.cmd_vel_callback, 10)
        
        # Timer
        self.read_timer = self.create_timer(0.05, self.update_odometry)

    def cmd_vel_callback(self, msg):
        linear_x = msg.linear.x
        angular_z = msg.angular.z
        base_speed = linear_x * 255

        if linear_x == 0.0:
            left_wheel = -angular_z * 150
            right_wheel = angular_z * 150
        else:
            turn_power = angular_z * 35 
            left_wheel = base_speed - turn_power
            right_wheel = base_speed + turn_power

        left_wheel = max(min(int(left_wheel), 255), -255)
        right_wheel = max(min(int(right_wheel), 255), -255)
        command = f"{left_wheel},{right_wheel}\n"

        if hasattr(self, 'arduino') and self.arduino.is_open:
            self.arduino.write(command.encode('utf-8'))

    def update_odometry(self):
        if hasattr(self, 'arduino') and self.arduino.in_waiting > 0:
            try:
                data = self.arduino.readline().decode('utf-8').strip()
                if ',' in data:
                    left_ticks_str, right_ticks_str = data.split(',')
                    current_left_ticks = int(left_ticks_str)
                    current_right_ticks = int(right_ticks_str)

                    self.get_logger().info(f"TICKS -> Left: {current_left_ticks}, Right: {current_right_ticks}")

                    if self.first_read:
                        self.prev_left_ticks = current_left_ticks
                        self.prev_right_ticks = current_right_ticks
                        self.first_read = False
                        return
                    
                    delta_left_ticks = current_left_ticks - self.prev_left_ticks
                    delta_right_ticks = current_right_ticks - self.prev_right_ticks
                    
                    self.prev_left_ticks = current_left_ticks
                    self.prev_right_ticks = current_right_ticks

                    dist_left = (delta_left_ticks / self.TICKS_PER_REV) * (2 * math.pi * self.WHEEL_RADIUS)
                    dist_right = (delta_right_ticks / self.TICKS_PER_REV) * (2 * math.pi * self.WHEEL_RADIUS)
                    
                    dist_center = (dist_right + dist_left) / 2.0
                    delta_theta = -(dist_right - dist_left) / self.WHEEL_BASE
                    
                    self.x += dist_center * math.cos(self.theta + (delta_theta / 2.0))
                    self.y += dist_center * math.sin(self.theta + (delta_theta / 2.0))
                    self.theta += delta_theta


                    
                    self.publish_odometry_and_tf()


                    
            except Exception as e:
                pass



    def publish_odometry_and_tf(self):
        current_time = self.get_clock().now().to_msg()
        
        qz = math.sin(self.theta / 2.0)
        qw = math.cos(self.theta / 2.0)


        t = TransformStamped()
        t.header.stamp = current_time
        t.header.frame_id = 'odom'
        t.child_frame_id = 'base_link'
        t.transform.translation.x = self.x
        t.transform.translation.y = self.y
        t.transform.translation.z = 0.0
        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = qz
        t.transform.rotation.w = qw
        self.tf_broadcaster.sendTransform(t)

        odom = Odometry()
        odom.header.stamp = current_time
        odom.header.frame_id = 'odom'
        odom.child_frame_id = 'base_link'
        odom.pose.pose.position.x = self.x
        odom.pose.pose.position.y = self.y
        odom.pose.pose.position.z = 0.0
        odom.pose.pose.orientation.x = 0.0
        odom.pose.pose.orientation.y = 0.0
        odom.pose.pose.orientation.z = qz
        odom.pose.pose.orientation.w = qw
        self.odom_pub.publish(odom)

def main(args=None):
    rclpy.init(args=args)
    node = MotorBridge()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()