from connector import Connector
from control_center import ControlCenter
from setting_ip import SettingIp
from mysql_database import MySqlDatabase
from ip_port_inputs import IPAndPortInputs
from tool import QSSTool
from PyQt5.Qt import *
import sys
import roslibpy
from error_display import Error
import time


def import_ip_port(ip_list):
    data = []
    for i in ip_list:
        d = dict({"id": i.get_id(), "name": i.get_obj_name(), "ip": i.get_ip(), "port": i.get_port()})
        data.append(d)
    sql = MySqlDatabase('app_ip', data)
    sql.import_data()


class ViewController:

    def __init__(self):
        self.ip_and_port = []
        self.load_ip_port()
        self.arm_ip = None
        self.arm_port = None
        self.car_ip = None
        self.car_port = None
        self.cam_ip = None
        self.cam_port = None
        self.previousWindow = None
        self.client = None
        self.err = None
        self.viewConnector = Connector()
        self.viewMainWindow = ControlCenter()
        self.viewSettingWindow = SettingIp(data=self.ip_and_port)
        self.viewConnector.connect_signal.connect(self.show_control_center)
        self.viewConnector.setting_signal.connect(self.show_setting_window)
        self.viewMainWindow.setting_but_signal.connect(self.show_setting_window)
        self.viewMainWindow.arm_control_signal.connect(self.manipulate_arm)
        self.viewMainWindow.pepper_arm_control_signal.connect(self.control_car)
        self.viewSettingWindow.save_signal.connect(self.show_connection_window)
        self.viewSettingWindow.return_signal.connect(self.show_previous_window)

    def load_ip_port(self):
        sql = MySqlDatabase("app_ip")
        data = sql.export_data()
        if len(data) != 0:
            for index, row in data.iterrows():
                self.ip_and_port.append(IPAndPortInputs(row[0], row[1], row[2], row[3]))

        if len(self.ip_and_port) != 0:
            for item in self.ip_and_port:
                if item.get_obj_name() == 'arm':
                    self.arm_ip = item.get_ip()
                    self.arm_port = item.get_port()
                if item.get_obj_name() == 'rover':
                    self.car_ip = item.get_ip()
                    self.car_port = item.get_port()
                if item.get_obj_name() == 'camera':
                    self.cam_ip = item.get_ip()
                    self.cam_port = item.get_port()

    def load_connect_view(self):
        self.previousWindow = self.viewConnector
        self.viewConnector.show()

    def load_main_window_view(self):
        self.previousWindow = self.viewMainWindow
        self.viewMainWindow.show()

    def load_ip_setting_view(self):
        self.viewSettingWindow.show()

    def control_arms(self, ori):
        service = roslibpy.Service(self.client, '/arm_manipulate', 'pepper_control/ArmControl')
        request = roslibpy.ServiceRequest(dict(ori=ori, which_arm='L'))
        print('Calling service...')
        service.call(request, self.success_callback, lambda result: print("Response: {0}".format(result)),
                     self.viewMainWindow.show_error(1, "E0004", "Service does not exist"))

    def control_car(self, dir):
        service = roslibpy.Service(self.client, '/mrobot_drive', 'mrobot_teleop/Drive')
        request = roslibpy.ServiceRequest(dict(dir=dir))
        print('Calling service...')
        service.call(request, self.success_callback, lambda result: print("Response: {0}".format(result)),
                     self.viewMainWindow.show_error(1, "E0003", "Service does not exist"))

    def manipulate_arm(self, ori):
        service = roslibpy.Service(self.client, '/niryo_control', 'niryo_robot_control/ArmControl')
        request = roslibpy.ServiceRequest({'ori': ori})
        print('Calling service...')
        service.call(request, self.success_callback, lambda result: print("Response: {0}".format(result)),
                     self.viewMainWindow.show_error(2, "E0002", "Service does not exist"))

    def success_callback(self, result):
        print("Service response: {0}".format(result))

    def connect_to_robot(self):
        print(self.arm_ip, " ", self.arm_port)
        try:
            self.client = roslibpy.Ros(host=self.arm_ip, port=int(self.arm_port))
            self.client.run()
            self.viewMainWindow.connect_to_robot(self.arm_ip, int(self.arm_port))
        except Exception as e:
            print(e)
            self.viewConnector.show_error("E0001", "Failed to connect to ROS")

        print('Is ROS connected?', self.client.is_connected)
        return self.client.is_connected

    def show_control_center(self):
        self.load_ip_port()
        if self.connect_to_robot():
            self.load_main_window_view()

            if self.viewConnector.isFullScreen():
                self.viewMainWindow.show_full_screen()
            else:
                self.viewMainWindow.show_normal_screen()
            self.viewMainWindow.move(self.viewConnector.x(), self.viewConnector.y())
            self.viewConnector.hide()

    def show_setting_window(self):
        self.load_ip_setting_view()
        if self.previousWindow.isFullScreen():
            self.viewSettingWindow.show_full_screen()
        else:
            self.viewSettingWindow.show_normal_screen()
        self.viewSettingWindow.move(self.previousWindow.x(), self.previousWindow.y())
        self.previousWindow.hide()

    def show_previous_window(self):
        if self.previousWindow == self.viewConnector:
            self.load_connect_view()
        else:
            self.load_main_window_view()

        if self.viewSettingWindow.isFullScreen():
            self.previousWindow.show_full_screen()
        else:
            self.previousWindow.show_normal_screen()
        self.previousWindow.move(self.viewSettingWindow.x(), self.viewSettingWindow.y())
        self.viewSettingWindow.hide()

    def show_connection_window(self, ip_list):
        import_ip_port(ip_list)
        self.load_connect_view()
        if self.viewSettingWindow.isFullScreen():
            self.viewConnector.show_full_screen()
        else:
            self.viewConnector.show_normal_screen()
        self.viewSettingWindow.update_ip_port(self.ip_and_port)
        self.viewConnector.move(self.viewSettingWindow.x(), self.viewSettingWindow.y())
        self.viewSettingWindow.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = ViewController()
    view.load_connect_view()
    QSSTool.setQssTool('resource/qss/style.qss', app)
    sys.exit(app.exec_())
