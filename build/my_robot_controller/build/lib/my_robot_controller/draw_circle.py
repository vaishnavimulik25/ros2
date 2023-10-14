#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class DrawCircleNode(Node): #created a node
    def __init__(self):
        super().__init__("draw_circle") #node name
        self.cmd_vel_pub = self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        #attribute ie msg_type,topic name,bufferlength
        self.timer = self.create_timer(0.5,self.send_velocity_command)
        self.get_logger().info('Draw circle node has been started')
    
    #how to send data to topic
    def send_velocity_command(self):
        msg = Twist()       #create msg 
        msg.linear.x = 2.0  #filled msg
        msg.angular.z = 1.0
        self.cmd_vel_pub.publish(msg)   #self.publisher_name.publish

def main(args=None):
    rclpy.init(args=args)
    node = DrawCircleNode()
    rclpy.spin(node)
    rclpy.shutdown()
