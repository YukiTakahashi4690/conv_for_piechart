#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32
from geometry_msgs.msg import PoseWithCovarianceStamped

class alpha_conv_node():
    def __init__(self):
        rospy.init_node("alphafloat32", anonymous=True)
        # self.sub = rospy.Subscriber("/amcl_pose", PoseWithCovarianceStamped, self.callback)
        self.sub = rospy.Subscriber("/alpha", Float32, self.callback)
        self.pub = rospy.Publisher("alpha_for_piechart", Float32, queue_size=1)
        self.alpha = 0
        self.pub_data = Float32()

    def callback(self, data):
        self.alpha = data

    def loop(self):
        self.pub_data = self.alpha
        self.pub.publish(self.pub_data)

if __name__ == "__main__":
    rg = alpha_conv_node()
    DUARATION = 0.2
    r = rospy.Rate(1 / DUARATION)
    while not rospy.is_shutdown():
        rg.loop()
        r.sleep()