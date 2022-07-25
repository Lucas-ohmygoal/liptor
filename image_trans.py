#!/usr/bin/env python 

import rospy
from std_msgs.msg import *
from geometry_msgs.msg import *
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
from niryo_robot_control.msg import CvImage


class TransferImage():

    def callback_raw_image(self, data):
        
        bridge = CvBridge()
        cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
        cv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)

        size = cv_image.shape[0] * cv_image.shape[1] * cv_image.shape[2]
        data = list(cv_image.reshape(size))

        
        self.cvImage.data = data
        self.cvImage.size = list(cv_image.shape)
        self.cvImage.time = rospy.get_time()
        self.pub.publish(self.cvImage)

        # cv2.imshow("image window", cv_image)
        # cv2.waitKey(0)


    def __init__(self):

        rospy.init_node('niryo_image_node', anonymous=True) 
        self.cvImage = CvImage()
        self.pub = rospy.Publisher('/camera_image', CvImage, queue_size=10)
        rospy.Subscriber('/gazebo_camera/image_raw', Image, self.callback_raw_image)
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            self.pub.publish(self.cvImage)
            rate.sleep()
        rospy.spin()



if __name__ == "__main__":
    TransferImage()
