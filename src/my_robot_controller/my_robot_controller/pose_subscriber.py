#get current position of robot through pose topic
#we need to get nam of the topic and msg type of topic


import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class PoseSubscriberNode(Node):
    def __init__(self):
        super().__init__("pose_subscriber")
        self.pose_subscriber = self.create_subscription(Pose,"/turtle1/pose",self.pose_callback,10)

    def pose_callback(self,msg:Pose):                               
        self.get_logger().info(str(msg))

def main(args=None):
    rclpy.init(args=args)
    node = PoseSubscriberNode()
    rclpy.spin(node)
    rclpy.shutdown()
