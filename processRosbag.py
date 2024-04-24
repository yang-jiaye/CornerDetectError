#!/usr/bin/env python

import rospy
import rosbag
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2, os


def extract_image(bag_path, output_folder):
    bag = rosbag.Bag(bag_path, 'r')
    bridge = CvBridge()

    i=0
    for topic, msg, t in bag.read_messages(topics=['/device_0/sensor_1/Color_0/image/data']):
        cv_image = bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
        cv2.imwrite(os.path.join(output_folder, 'image_{0}.png'.format(str(i).zfill(4))), cv_image)
        i += 1

    bag.close()

if __name__ == '__main__':

    path_list = ["20240319_161440.bag",   "20240319_221112.bag",   "20240319_221918.bag"  , "20240319_222613.bag", "20240319_220350.bag" ,  "20240319_221454.bag", "20240319_222129.bag"  ,"20240319_223023.bag"]

    for i in range(8):
        bag_path = "/home/ackerman/Documents/" + path_list[i]
        output_folder = '/home/ackerman/Data/Chessboard/test' + str(i)
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        extract_image(bag_path, output_folder)