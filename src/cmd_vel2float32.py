#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32
from geometry_msgs.msg import Twist

class conv_node():
    def __init__(self):
        rospy.init_node("cmdvel2float32", anonymous=True)
        self.sub = rospy.Subscriber("/cmd_vel", Twist, self.callback)
        self.pub = rospy.Publisher("for_piechart", Float32, queue_size=1)
        self.cmd_vel = 0
        self.pub_data = Float32()
    
    def callback(self, data):
        self.cmd_vel = data.angular.z

    def loop(self):
        self.pub_data = self.cmd_vel
        self.pub.publish(self.pub_data)

if __name__ == "__main__":
    rg = conv_node()
    DURATION = 0.2
    r = rospy.Rate(1 / DURATION)
    while not rospy.is_shutdown():
        rg.loop()
        r.sleep()