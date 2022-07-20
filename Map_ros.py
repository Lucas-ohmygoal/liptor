# Developer : Lucas Liu
# Date: 7/4/2022 Time: 11:17 PM

import numpy as np
from PyQt5.Qt import *
import cv2
import roslibpy
import pybase64


class MapRosNode(QThread):
    map_image_signal = pyqtSignal(np.ndarray)

    def __init__(self):
        QThread.__init__(self)
        self.client = None
        self.listener = None

    def connect_master(self, ip, port, message, message_type):
        self.client = roslibpy.Ros(host=ip, port=port)
        self.listener = roslibpy.Topic(self.client, message, message_type)
        self.client.run()

    def connect_ros(self):
        self.client.connect()
        # print('Is ROS connected?', self.client.is_connected)
        self.listener.subscribe(self.callback_map_image)

    def disconnect_ros(self):
        self.client.close()

    @pyqtSlot()
    def callback_map_image(self, map_msg):
        image_bytes = pybase64.b64decode(map_msg['data'])
        image = np.fromstring(image_bytes, np.uint8)
        # sec = map_msg['time']
        image_scaled = image.reshape(map_msg['size'])
        # cv2.imshow("Map window", image_scaled)
        # cv2.waitKey(3)
        self.map_image_signal.emit(image_scaled)