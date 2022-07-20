# Developer : Lucas Liu
# Date: 6/7/2022 Time: 10:18 PM
import string
import sys
from PyQt5.Qt import *
from Tool import QSSTool
from Camera_ros import CameraRosNode
from Map_ros import MapRosNode
import cv2
from ErrorDisplay import Error


class ControlCenter(QWidget):

    setting_but_signal = pyqtSignal()
    arm_control_signal = pyqtSignal(str)
    pepper_arm_control_signal = pyqtSignal(str)

    def __init__(self, parent=None, client=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setWindowIcon(QIcon("resource/images/logo_5.png"))
        self.setWindowTitle("LIPTOR")
        self.client = client
        self.resize(1900, 1300)
        self.menu = QWidget()
        self.arm_box = QWidget()
        self.car_box = QWidget()
        self.cam_box = QWidget()
        self.ing_box = QWidget()
        self.center_box = QWidget()
        self.top_box = QWidget()
        self.arm_button = QToolButton()
        self.car_button = QToolButton()
        self.cam_button = QToolButton()
        self.int_button = QToolButton()
        self.menu_but = QToolButton(self.menu)
        self.logo_label = QLabel()
        self.exit_button = QToolButton()
        self.maximize_button = QToolButton()
        self.minimize_button = QToolButton()
        self.normalize_icon = QIcon("resource/images/normalize_button.png")
        self.maximize_icon = QIcon("resource/images/maximize_button.png")
        self.move_x = 0
        self.move_y = 0
        self.origin_x = 0
        self.origin_y = 0
        self.setMouseTracking(True)
        self.drag_flag = False
        self.loading_gif = QMovie("resource/images/loading.gif")

        self.top_box_i = QWidget()
        self.bot_box_i = QWidget()
        self.cam_box_i = QLabel()
        self.map_box_i = QLabel()
        self.cam_img_i = CameraRosNode()
        self.map_img_i = MapRosNode()
        self.cam_img_i.raw_image_signal.connect(self.set_image)
        self.map_img_i.map_image_signal.connect(self.set_map)
        self.steer_box_i = QWidget()
        self.up_key_i = QToolButton()
        self.down_key_i = QToolButton()
        self.left_key_i = QToolButton()
        self.right_key_i = QToolButton()
        self.stop_key_i = QToolButton()
        self.prop_box_i = QWidget()
        self.speed_slider_i = QSlider()
        self.speed_label_i = QLabel()
        self.speed_term_i = QLabel()
        self.acl_slider_i = QSlider()
        self.acl_term_i = QLabel()
        self.auto_mode_i = QRadioButton()
        self.auto_term_i = QLabel()
        self.grip_box_i = QWidget()
        self.grip_button_i = QToolButton()
        self.grip_term_i = QLabel()
        self.grip_auto_i = QRadioButton()
        self.grip_auto_term_i = QLabel()
        self.grip_steer_box_i = QWidget()
        self.grip_up_key_i = QToolButton()
        self.grip_down_key_i = QToolButton()
        self.grip_left_key_i = QToolButton()
        self.grip_right_key_i = QToolButton()
        self.cam_control_box_i = QWidget()
        self.cam_button_i = QWidget()
        self.cam_up_i = QToolButton()
        self.cam_down_i = QToolButton()
        self.cam_left_i = QToolButton()
        self.cam_right_i = QToolButton()
        self.return_but_i = QToolButton()
        self.err_i = Error(self.bot_box_i)

        self.top_box_a = QWidget()
        self.bot_box_a = QWidget()
        self.cam_box_a = QLabel()
        self.map_box_a = QLabel()
        self.cam_img_a = CameraRosNode()
        self.cam_img_a.raw_image_signal.connect(self.set_arm_image)
        self.steer_box_a = QWidget()
        self.up_key_a = QToolButton()
        self.down_key_a = QToolButton()
        self.left_key_a = QToolButton()
        self.right_key_a = QToolButton()
        self.stop_key_a = QToolButton()
        self.prop_box_a = QWidget()
        self.speed_slider_a = QSlider()
        self.speed_label_a = QLabel()
        self.speed_term_a = QLabel()
        self.acl_slider_a = QSlider()
        self.acl_term_a = QLabel()
        self.auto_mode_a = QRadioButton()
        self.auto_term_a = QLabel()
        self.grip_box_a = QWidget()
        self.grip_button_a = QToolButton()
        self.grip_term_a = QLabel()
        self.grip_auto_a = QRadioButton()
        self.grip_auto_term_a = QLabel()
        self.grip_steer_box_a = QWidget()
        self.grip_up_key_a = QToolButton()
        self.grip_down_key_a = QToolButton()
        self.grip_left_key_a = QToolButton()
        self.grip_right_key_a = QToolButton()
        self.cam_control_box_a = QWidget()
        self.cam_button_a = QWidget()
        self.cam_up_a = QToolButton()
        self.cam_down_a = QToolButton()
        self.cam_left_a = QToolButton()
        self.cam_right_a = QToolButton()
        self.return_but_a = QToolButton()
        self.err_a = Error(self.bot_box_a)

        self.top_box_r = QWidget()
        self.bot_box_r = QWidget()
        self.cam_box_r = QLabel()
        self.map_box_r = QLabel()
        self.steer_box_r = QWidget()
        self.up_key_r = QToolButton()
        self.down_key_r = QToolButton()
        self.left_key_r = QToolButton()
        self.right_key_r = QToolButton()
        self.stop_key_r = QToolButton()
        self.prop_box_r = QWidget()
        self.speed_slider_r = QSlider()
        self.speed_label_r = QLabel()
        self.speed_term_r = QLabel()
        self.acl_slider_r = QSlider()
        self.acl_term_r = QLabel()
        self.auto_mode_r = QRadioButton()
        self.auto_term_r = QLabel()
        self.grip_box_r = QWidget()
        self.grip_button_r = QToolButton()
        self.grip_term_r = QLabel()
        self.grip_auto_r = QRadioButton()
        self.grip_auto_term_r = QLabel()
        self.grip_steer_box_r = QWidget()
        self.grip_up_key_r = QToolButton()
        self.grip_down_key_r = QToolButton()
        self.grip_left_key_r = QToolButton()
        self.grip_right_key_r = QToolButton()
        self.cam_control_box_r = QWidget()
        self.cam_button_r = QWidget()
        self.cam_up_r = QToolButton()
        self.cam_down_r = QToolButton()
        self.cam_left_r = QToolButton()
        self.cam_right_r = QToolButton()
        self.return_but_r = QToolButton()
        self.err_r = Error(self.bot_box_r)

        self.top_box_c = QWidget()
        self.bot_box_c = QWidget()
        self.cam_box_c = QLabel()
        self.prop_box_c = QWidget()
        self.view_slider_c = QSlider()
        self.view_label_c = QLabel()
        self.view_term_pc = QLabel()
        self.view_term_ac = QLabel()
        self.acl_slider_c = QSlider()
        self.acl_term_c = QLabel()
        self.auto_mode_c = QRadioButton()
        self.auto_term_c = QLabel()
        self.cam_control_box_c = QWidget()
        self.cam_button_c = QWidget()
        self.cam_up_c = QToolButton()
        self.cam_down_c = QToolButton()
        self.cam_left_c = QToolButton()
        self.cam_right_c = QToolButton()
        self.return_but_c = QToolButton()
        self.dir_combo_c = QComboBox()
        self.depth_combo_c = QComboBox()
        self.err_c = Error(self.cam_box)
        self.setup_ui()

    def mousePressEvent(self, evt):
        if self.menu.geometry().contains(evt.pos()):
            self.move_x = evt.globalX()
            self.move_y = evt.globalY()
            self.origin_x = self.x()
            self.origin_y = self.y()
            self.drag_flag = True
        else:
            self.drag_flag = False

    def mouseMoveEvent(self, evt):
        if self.drag_flag:
            move_x = evt.globalX() - self.move_x
            move_y = evt.globalY() - self.move_y
            destination_x = self.origin_x + move_x
            destination_y = self.origin_y + move_y
            self.move(destination_x, destination_y)

    def resizeEvent(self, evt):
        super().resizeEvent(evt)
        self.menu_but.move(5, self.menu.height() - 85)
        self.exit_button.move(5, self.menu.y() + 20)
        self.maximize_button.move(5, self.menu.y() + 100)
        self.maximize_button.move(5, self.menu.y() + 100)
        self.minimize_button.move(5, self.menu.y() + 180)
        self.logo_label.move(int(self.width() / 2) - 250, 60)
        self.prop_box_i.move(450, int(self.height() / 2) - 340)
        self.grip_box_i.move(int(self.width() / 2) - 80, int(self.height() / 2) - 440)
        self.grip_steer_box_i.move(int(self.width() / 2) + 230, int(self.height() / 2) - 305)
        if self.isFullScreen():
            self.cam_control_box_i.move(self.steer_box_i.x() + int(self.width() / 2) + 700,
                                        self.steer_box_i.y() + int(self.height() / 2) - 670)
        else:
            self.cam_control_box_i.move(self.steer_box_i.x() + int(self.width() / 2) + 380,
                                    self.steer_box_i.y() + int(self.height() / 2) - 610)

        self.return_but_i.move(int(self.width() / 2) - 80, 80)

        bitmap = QBitmap(self.size())
        bitmap.fill()
        painter = QPainter(bitmap)
        painter.begin(self)
        painter.setPen(Qt.NoPen)
        painter.setBrush(Qt.black)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.drawRoundedRect(bitmap.rect(), 8, 8)
        painter.end()
        self.setMask(bitmap)

    def exit_button_pressed(self):
        # self.cam_img_i.client.terminate()
        # self.map_img_i.client.terminate()
        # self.cam_img_a.client.terminate()
        self.close()

    def show_full_screen(self):
        self.showFullScreen()
        self.maximize_button.setIcon(self.normalize_icon)

    def show_normal_screen(self):
        self.showNormal()
        self.maximize_button.setIcon(self.maximize_icon)

    def maximize_button_pressed(self):
        if self.isFullScreen():
            self.showNormal()
            self.maximize_button.setIcon(self.maximize_icon)
        else:
            self.showFullScreen()
            self.maximize_button.setIcon(self.normalize_icon)

    def minimize_button_pressed(self):
        self.showMinimized()

    def menu_button_pressed(self):
        self.setting_but_signal.emit()

    def up_key_pressed(self):
        if self.ing_box.isVisible():
            up_key_pic = QIcon("resource/images/up-arrow-pr.png")
            self.up_key_i.setIcon(up_key_pic)
        if self.arm_box.isVisible():
            up_key_pic = QIcon("resource/images/up-arrow-pr.png")
            self.up_key_a.setIcon(up_key_pic)
        if self.car_box.isVisible():
            up_key_pic = QIcon("resource/images/up-arrow-pr.png")
            self.up_key_r.setIcon(up_key_pic)

    def up_key_released(self):
        if self.ing_box.isVisible():
            up_key_pic = QIcon("resource/images/up-arrow-p.png")
            self.up_key_i.setIcon(up_key_pic)
            # self.pepper_arm_control_signal.emit("W")
            self.pepper_arm_control_signal.emit("i")
        if self.arm_box.isVisible():
            up_key_pic = QIcon("resource/images/up-arrow-p.png")
            self.up_key_a.setIcon(up_key_pic)
            self.arm_control_signal.emit("F")
        if self.car_box.isVisible():
            up_key_pic = QIcon("resource/images/up-arrow-p.png")
            self.up_key_r.setIcon(up_key_pic)

    def down_key_pressed(self):
        if self.ing_box.isVisible():
            down_key_pic = QIcon("resource/images/down-arrow-pr.png")
            self.down_key_i.setIcon(down_key_pic)
        if self.arm_box.isVisible():
            down_key_pic = QIcon("resource/images/down-arrow-pr.png")
            self.down_key_a.setIcon(down_key_pic)
        if self.car_box.isVisible():
            down_key_pic = QIcon("resource/images/down-arrow-pr.png")
            self.down_key_r.setIcon(down_key_pic)

    def down_key_released(self):
        if self.ing_box.isVisible():
            down_key_pic = QIcon("resource/images/down-arrow-p.png")
            self.down_key_i.setIcon(down_key_pic)
            # self.pepper_arm_control_signal.emit("S")
            self.pepper_arm_control_signal.emit(",")
        if self.arm_box.isVisible():
            down_key_pic = QIcon("resource/images/down-arrow-p.png")
            self.down_key_a.setIcon(down_key_pic)
            self.arm_control_signal.emit("B")
        if self.car_box.isVisible():
            down_key_pic = QIcon("resource/images/down-arrow-p.png")
            self.down_key_r.setIcon(down_key_pic)

    def left_key_pressed(self):
        if self.ing_box.isVisible():
            left_key_pic = QIcon("resource/images/left-arrow-pr.png")
            self.left_key_i.setIcon(left_key_pic)
        if self.arm_box.isVisible():
            left_key_pic = QIcon("resource/images/left-arrow-pr.png")
            self.left_key_a.setIcon(left_key_pic)
        if self.car_box.isVisible():
            left_key_pic = QIcon("resource/images/left-arrow-pr.png")
            self.left_key_r.setIcon(left_key_pic)

    def left_key_released(self):
        if self.ing_box.isVisible():
            left_key_pic = QIcon("resource/images/left-arrow-p.png")
            self.left_key_i.setIcon(left_key_pic)
            # self.pepper_arm_control_signal.emit("A")
            self.pepper_arm_control_signal.emit("j")
        if self.arm_box.isVisible():
            left_key_pic = QIcon("resource/images/left-arrow-p.png")
            self.left_key_a.setIcon(left_key_pic)
            self.arm_control_signal.emit("L")
        if self.car_box.isVisible():
            left_key_pic = QIcon("resource/images/left-arrow-p.png")
            self.left_key_r.setIcon(left_key_pic)

    def right_key_pressed(self):
        if self.ing_box.isVisible():
            right_key_pic = QIcon("resource/images/right-arrow-pr.png")
            self.right_key_i.setIcon(right_key_pic)
        if self.arm_box.isVisible():
            right_key_pic = QIcon("resource/images/right-arrow-pr.png")
            self.right_key_a.setIcon(right_key_pic)
        if self.car_box.isVisible():
            right_key_pic = QIcon("resource/images/right-arrow-pr.png")
            self.right_key_r.setIcon(right_key_pic)

    def right_key_released(self):
        if self.ing_box.isVisible():
            right_key_pic = QIcon("resource/images/right-arrow-p.png")
            self.right_key_i.setIcon(right_key_pic)
            # self.pepper_arm_control_signal.emit("D")
            self.pepper_arm_control_signal.emit("l")
        if self.arm_box.isVisible():
            right_key_pic = QIcon("resource/images/right-arrow-p.png")
            self.right_key_a.setIcon(right_key_pic)
            self.arm_control_signal.emit("R")
        if self.car_box.isVisible():
            right_key_pic = QIcon("resource/images/right-arrow-p.png")
            self.right_key_r.setIcon(right_key_pic)

    def grip_up_pressed(self):
        if self.ing_box.isVisible():
            self.grip_up_key_i.setIconSize(QSize(80, 80))
        if self.arm_box.isVisible():
            self.grip_up_key_a.setIconSize(QSize(80, 80))
        if self.car_box.isVisible():
            self.grip_up_key_r.setIconSize(QSize(80, 80))

    def grip_up_released(self):
        if self.ing_box.isVisible():
            self.grip_up_key_i.setIconSize(QSize(90, 90))
            self.pepper_arm_control_signal.emit("I")
        if self.arm_box.isVisible():
            self.grip_up_key_a.setIconSize(QSize(90, 90))
        if self.car_box.isVisible():
            self.grip_up_key_r.setIconSize(QSize(90, 90))

    def grip_down_pressed(self):
        if self.ing_box.isVisible():
            self.grip_down_key_i.setIconSize(QSize(80, 80))
        if self.arm_box.isVisible():
            self.grip_down_key_a.setIconSize(QSize(80, 80))
        if self.car_box.isVisible():
            self.grip_down_key_r.setIconSize(QSize(80, 80))

    def grip_down_released(self):
        if self.ing_box.isVisible():
            self.grip_down_key_i.setIconSize(QSize(90, 90))
            self.pepper_arm_control_signal.emit("K")
        if self.arm_box.isVisible():
            self.grip_down_key_a.setIconSize(QSize(90, 90))
        if self.car_box.isVisible():
            self.grip_down_key_r.setIconSize(QSize(90, 90))

    def grip_left_pressed(self):
        if self.ing_box.isVisible():
            self.grip_left_key_i.setIconSize(QSize(80, 80))
        if self.arm_box.isVisible():
            self.grip_left_key_a.setIconSize(QSize(80, 80))
        if self.car_box.isVisible():
            self.grip_left_key_r.setIconSize(QSize(80, 80))

    def grip_left_released(self):
        if self.ing_box.isVisible():
            self.grip_left_key_i.setIconSize(QSize(90, 90))
            self.pepper_arm_control_signal.emit("J")
        if self.arm_box.isVisible():
            self.grip_left_key_a.setIconSize(QSize(90, 90))
        if self.car_box.isVisible():
            self.grip_left_key_r.setIconSize(QSize(90, 90))

    def grip_right_pressed(self):
        if self.ing_box.isVisible():
            self.grip_right_key_i.setIconSize(QSize(80, 80))
        if self.arm_box.isVisible():
            self.grip_right_key_a.setIconSize(QSize(80, 80))
        if self.car_box.isVisible():
            self.grip_right_key_r.setIconSize(QSize(80, 80))

    def grip_right_released(self):
        if self.ing_box.isVisible():
            self.grip_right_key_i.setIconSize(QSize(90, 90))
            self.pepper_arm_control_signal.emit("L")
        if self.arm_box.isVisible():
            self.grip_right_key_a.setIconSize(QSize(90, 90))
        if self.car_box.isVisible():
            self.grip_right_key_r.setIconSize(QSize(90, 90))

    def stop_key_click(self):
        if self.ing_box.isVisible():
            self.stop_key_i.animateClick()

        if self.arm_box.isVisible():
            self.stop_key_a.animateClick()

        if self.car_box.isVisible():
            self.stop_key_r.animateClick()

    def stop_key_released(self):
        # self.stop_key_i.setStyleSheet("padding: 0px 0px 0px 0px;")
        pass

    def cam_up_pressed(self):
        if self.ing_box.isVisible():
            cam_up = QIcon("resource/images/arrow-up.png")
            self.cam_up_i.setIcon(cam_up)
            self.cam_up_i.setIconSize(QSize(50, 50))

        if self.cam_box.isVisible():
            cam_up = QIcon("resource/images/arrow-up.png")
            self.cam_up_c.setIcon(cam_up)
            self.cam_up_c.setIconSize(QSize(110, 110))

    def cam_down_pressed(self):
        if self.ing_box.isVisible():
            cam_down = QIcon("resource/images/arrow-down.png")
            self.cam_down_i.setIcon(cam_down)
            self.cam_down_i.setIconSize(QSize(50, 50))

        if self.cam_box.isVisible():
            cam_down = QIcon("resource/images/arrow-down.png")
            self.cam_down_c.setIcon(cam_down)
            self.cam_down_c.setIconSize(QSize(110, 110))

    def cam_left_pressed(self):
        if self.ing_box.isVisible():
            cam_left = QIcon("resource/images/arrow-left.png")
            self.cam_left_i.setIcon(cam_left)
            self.cam_left_i.setIconSize(QSize(50, 50))

        if self.cam_box.isVisible():
            cam_left = QIcon("resource/images/arrow-left.png")
            self.cam_left_c.setIcon(cam_left)
            self.cam_left_c.setIconSize(QSize(110, 110))

    def cam_right_pressed(self):
        if self.ing_box.isVisible():
            cam_right = QIcon("resource/images/arrow-right.png")
            self.cam_right_i.setIcon(cam_right)
            self.cam_right_i.setIconSize(QSize(50, 50))

        if self.cam_box.isVisible():
            cam_right = QIcon("resource/images/arrow-right.png")
            self.cam_right_c.setIcon(cam_right)
            self.cam_right_c.setIconSize(QSize(110, 110))

    def cam_up_released(self):
        if self.ing_box.isVisible():
            cam_up = QIcon("resource/images/arrow_up.png")
            self.cam_up_i.setIcon(cam_up)
            self.cam_up_i.setIconSize(QSize(60, 60))

        if self.cam_box.isVisible():
            cam_up = QIcon("resource/images/arrow_up.png")
            self.cam_up_c.setIcon(cam_up)
            self.cam_up_c.setIconSize(QSize(120, 120))

    def cam_down_released(self):
        if self.ing_box.isVisible():
            cam_down = QIcon("resource/images/arrow_down.png")
            self.cam_down_i.setIcon(cam_down)
            self.cam_down_i.setIconSize(QSize(60, 60))

        if self.cam_box.isVisible():
            cam_down = QIcon("resource/images/arrow_down.png")
            self.cam_down_c.setIcon(cam_down)
            self.cam_down_c.setIconSize(QSize(120, 120))

    def cam_left_released(self):
        if self.ing_box.isVisible():
            cam_left = QIcon("resource/images/arrow_left.png")
            self.cam_left_i.setIcon(cam_left)
            self.cam_left_i.setIconSize(QSize(60, 60))

        if self.cam_box.isVisible():
            cam_left = QIcon("resource/images/arrow_left.png")
            self.cam_left_c.setIcon(cam_left)
            self.cam_left_c.setIconSize(QSize(120, 120))

    def cam_right_released(self):
        if self.ing_box.isVisible():
            cam_right = QIcon("resource/images/arrow_right.png")
            self.cam_right_i.setIcon(cam_right)
            self.cam_right_i.setIconSize(QSize(60, 60))

        if self.cam_box.isVisible():
            cam_right = QIcon("resource/images/arrow_right.png")
            self.cam_right_c.setIcon(cam_right)
            self.cam_right_c.setIconSize(QSize(120, 120))

    def keyPressEvent(self, evt):
        if evt.key() == Qt.Key_W:
            self.up_key_pressed()

        if evt.key() == Qt.Key_S:
            self.down_key_pressed()

        if evt.key() == Qt.Key_A:
            self.left_key_pressed()

        if evt.key() == Qt.Key_D:
            self.right_key_pressed()

        if evt.key() == Qt.Key_F:
            self.stop_key_click()

        if evt.key() == Qt.Key_G:
            self.grip_button_click()

        if evt.key() == Qt.Key_I:
            self.grip_up_pressed()

        if evt.key() == Qt.Key_K:
            self.grip_down_pressed()

        if evt.key() == Qt.Key_J:
            self.grip_left_pressed()

        if evt.key() == Qt.Key_L:
            self.grip_right_pressed()

        if evt.key() == Qt.Key_Up:
            self.cam_up_pressed()

        if evt.key() == Qt.Key_Down:
            self.cam_down_pressed()

        if evt.key() == Qt.Key_Left:
            self.cam_left_pressed()

        if evt.key() == Qt.Key_Right:
            self.cam_right_pressed()

    def keyReleaseEvent(self, evt):
        if evt.key() == Qt.Key_W:
            self.up_key_released()

        if evt.key() == Qt.Key_S:
            self.down_key_released()

        if evt.key() == Qt.Key_A:
            self.left_key_released()

        if evt.key() == Qt.Key_D:
            self.right_key_released()

        if evt.key() == Qt.Key_I:
            self.grip_up_released()

        if evt.key() == Qt.Key_K:
            self.grip_down_released()

        if evt.key() == Qt.Key_J:
            self.grip_left_released()

        if evt.key() == Qt.Key_L:
            self.grip_right_released()

        if evt.key() == Qt.Key_Up:
            self.cam_up_released()

        if evt.key() == Qt.Key_Down:
            self.cam_down_released()

        if evt.key() == Qt.Key_Left:
            self.cam_left_released()

        if evt.key() == Qt.Key_Right:
            self.cam_right_released()

    def view_slider_moved(self):
        if self.cam_box.isVisible():
            x = self.prop_box_c.x() + self.view_slider_c.x() + int(self.view_slider_c.value()/(self.view_slider_c.maximum() - self.view_slider_c.minimum()) * (self.view_slider_c.width() - 45)) + 30
            y = self.prop_box_c.y() + self.view_slider_c.y() - 150
            self.view_label_c.move(x, y)
            self.view_label_c.setText(str(self.view_slider_c.value() - 45))

    def view_slider_pressed(self):
        if self.cam_box.isVisible():
            self.view_label_c.show()
            x = self.prop_box_c.x() + self.view_slider_c.x() + int(self.view_slider_c.value()/(self.view_slider_c.maximum() - self.view_slider_c.minimum()) * (self.view_slider_c.width() - 45)) + 30
            y = self.prop_box_c.y() + self.view_slider_c.y() - 150
            self.view_label_c.move(x, y)
            self.view_label_c.setText(str(self.view_slider_c.value()))

    def view_slider_released(self):
        if self.cam_box.isVisible():
            self.view_label_c.hide()

    def speed_slider_pressed(self):
        if self.ing_box.isVisible():
            self.speed_label_i.show()
            x = self.prop_box_i.x() + self.speed_slider_i.x() + int(self.speed_slider_i.value()/(self.speed_slider_i.maximum() - self.speed_slider_i.minimum()) * (self.speed_slider_i.width() - 45)) + 30
            y = self.prop_box_i.y() + self.speed_slider_i.y() - 90
            self.speed_label_i.move(x, y)
            self.speed_label_i.setText(str(self.speed_slider_i.value()))
        if self.arm_box.isVisible():
            self.speed_label_a.show()
            x = self.prop_box_a.x() + self.speed_slider_a.x() + int(self.speed_slider_a.value()/(self.speed_slider_a.maximum() - self.speed_slider_a.minimum()) * (self.speed_slider_a.width() - 45)) + 30
            y = self.prop_box_a.y() + self.speed_slider_a.y() - 90
            self.speed_label_a.move(x, y)
            self.speed_label_a.setText(str(self.speed_slider_a.value()))
        if self.car_box.isVisible():
            self.speed_label_r.show()
            x = self.prop_box_r.x() + self.speed_slider_r.x() + int(self.speed_slider_r.value()/(self.speed_slider_r.maximum() - self.speed_slider_r.minimum()) * (self.speed_slider_r.width() - 45)) + 30
            y = self.prop_box_r.y() + self.speed_slider_r.y() - 90
            self.speed_label_r.move(x, y)
            self.speed_label_r.setText(str(self.speed_slider_r.value()))

    def speed_slider_moved(self):
        if self.ing_box.isVisible():
            x = self.prop_box_i.x() + self.speed_slider_i.x() + int(self.speed_slider_i.value() / (
                        self.speed_slider_i.maximum() - self.speed_slider_i.minimum()) * (self.speed_slider_i.width() - 45)) + 30
            y = self.prop_box_i.y() + self.speed_slider_i.y() - 90
            self.speed_label_i.move(x, y)
            self.speed_label_i.setText(str(self.speed_slider_i.value()))
        if self.arm_box.isVisible():
            x = self.prop_box_a.x() + self.speed_slider_a.x() + int(self.speed_slider_a.value()/(self.speed_slider_a.maximum() - self.speed_slider_a.minimum()) * (self.speed_slider_a.width() - 45)) + 30
            y = self.prop_box_a.y() + self.speed_slider_a.y() - 90
            self.speed_label_a.move(x, y)
            self.speed_label_a.setText(str(self.speed_slider_a.value()))
        if self.car_box.isVisible():
            x = self.prop_box_r.x() + self.speed_slider_r.x() + int(self.speed_slider_r.value()/(self.speed_slider_r.maximum() - self.speed_slider_r.minimum()) * (self.speed_slider_r.width() - 45)) + 30
            y = self.prop_box_r.y() + self.speed_slider_r.y() - 90
            self.speed_label_r.move(x, y)
            self.speed_label_r.setText(str(self.speed_slider_r.value()))

    def speed_slider_released(self):
        if self.ing_box.isVisible():
            self.speed_label_i.hide()
        if self.arm_box.isVisible():
            self.speed_label_a.hide()
        if self.car_box.isVisible():
            self.speed_label_r.hide()

    def acl_slider_pressed(self):
        if self.ing_box.isVisible():
            self.speed_label_i.show()
            x = self.prop_box_i.x() + self.acl_slider_i.x() + int(self.acl_slider_i.value()/(self.acl_slider_i.maximum() - self.acl_slider_i.minimum()) * (self.acl_slider_i.width() - 45)) + 30
            y = self.prop_box_i.y() + self.acl_slider_i.y() - 90
            self.speed_label_i.move(x, y)
            self.speed_label_i.setText(str(self.acl_slider_i.value()))

        if self.arm_box.isVisible():
            self.speed_label_a.show()
            x = self.prop_box_a.x() + self.acl_slider_a.x() + int(
                self.acl_slider_a.value() / (self.acl_slider_a.maximum() - self.acl_slider_a.minimum()) * (
                            self.acl_slider_a.width() - 45)) + 30
            y = self.prop_box_a.y() + self.acl_slider_a.y() - 90
            self.speed_label_a.move(x, y)
            self.speed_label_a.setText(str(self.acl_slider_a.value()))

        if self.car_box.isVisible():
            self.speed_label_r.show()
            x = self.prop_box_r.x() + self.acl_slider_r.x() + int(
                self.acl_slider_r.value() / (self.acl_slider_r.maximum() - self.acl_slider_r.minimum()) * (
                            self.acl_slider_r.width() - 45)) + 30
            y = self.prop_box_r.y() + self.acl_slider_r.y() - 90
            self.speed_label_r.move(x, y)
            self.speed_label_r.setText(str(self.acl_slider_r.value()))

    def acl_slider_moved(self):
        if self.ing_box.isVisible():
            x = self.prop_box_i.x() + self.acl_slider_i.x() + int(
                self.acl_slider_i.value() / (self.acl_slider_i.maximum() - self.acl_slider_i.minimum()) * (
                            self.acl_slider_i.width() - 45)) + 30
            y = self.prop_box_i.y() + self.acl_slider_i.y() - 90
            self.speed_label_i.move(x, y)
            self.speed_label_i.setText(str(self.acl_slider_i.value()))

        if self.arm_box.isVisible():
            x = self.prop_box_a.x() + self.acl_slider_a.x() + int(
                self.acl_slider_a.value() / (self.acl_slider_a.maximum() - self.acl_slider_a.minimum()) * (
                            self.acl_slider_a.width() - 45)) + 30
            y = self.prop_box_a.y() + self.acl_slider_a.y() - 90
            self.speed_label_a.move(x, y)
            self.speed_label_a.setText(str(self.acl_slider_a.value()))

        if self.car_box.isVisible():
            x = self.prop_box_r.x() + self.acl_slider_r.x() + int(
                self.acl_slider_r.value() / (self.acl_slider_r.maximum() - self.acl_slider_r.minimum()) * (
                            self.acl_slider_r.width() - 45)) + 30
            y = self.prop_box_r.y() + self.acl_slider_r.y() - 90
            self.speed_label_r.move(x, y)
            self.speed_label_r.setText(str(self.acl_slider_r.value()))

    def acl_slider_released(self):
        if self.ing_box.isVisible():
            self.speed_label_i.hide()

        if self.arm_box.isVisible():
            self.speed_label_a.hide()

        if self.car_box.isVisible():
            self.speed_label_r.hide()

    def grip_button_pressed(self):
        if self.ing_box.isVisible():
            self.grip_button_i.setEnabled(False)
            timer = QTimer(self)
            timer.timeout.connect(lambda: self.grip_button_i.setEnabled(True))
            timer.start(3000)

        if self.arm_box.isVisible():
            self.grip_button_a.setEnabled(False)
            timer = QTimer(self)
            timer.timeout.connect(lambda: self.grip_button_a.setEnabled(True))
            timer.start(3000)

        if self.car_box.isVisible():
            self.grip_button_r.setEnabled(False)
            timer = QTimer(self)
            timer.timeout.connect(lambda: self.grip_button_r.setEnabled(True))
            timer.start(3000)

    def grip_button_click(self):
        if self.ing_box.isVisible():
            self.grip_button_i.animateClick()
        if self.arm_box.isVisible():
            self.grip_button_a.animateClick()
        if self.car_box.isVisible():
            self.grip_button_r.animateClick()

    def set_image(self, cv_image):
        # cv2.imshow("Image window", cv_image)
        # cv2.waitKey(3)
        image_height, image_width, image_depth = cv_image.shape
        img_dis = QImage(cv_image, image_width, image_height, image_width * image_depth, QImage.Format_RGB888)
        img_pix = QPixmap(img_dis)
        self.cam_box_i.setScaledContents(True)
        self.cam_box_i.setPixmap(img_pix)

    def set_arm_image(self, cv_image):
        # cv2.imshow("Image window", self.cam_img_a.cv_image)
        # cv2.waitKey(3)
        image_height, image_width, image_depth = cv_image.shape
        img_dis = QImage(cv_image, image_width, image_height, image_width * image_depth, QImage.Format_RGB888)
        img_pix = QPixmap(img_dis)
        self.cam_box_a.setScaledContents(True)
        self.cam_box_a.setPixmap(img_pix)

    def set_map(self, cv_map):
        # cv2.imshow("Map window", cv_map)
        # cv2.waitKey(3)
        image_height, image_width, image_depth = cv_map.shape
        img_dis = QImage(cv_map, image_width, image_height, image_width * image_depth, QImage.Format_RGB888)
        img_pix = QPixmap(img_dis)
        self.map_box_i.setScaledContents(True)
        self.map_box_i.setPixmap(img_pix)

    def connect_to_robot(self, ip, port):
        self.cam_img_a.connect_master(ip, port, '/camera_image', 'niryo_control/CvImage')
        self.cam_img_i.connect_master(ip, port, '/camera_image', 'pepper_control/CvImage')
        self.map_img_i.connect_master(ip, port, "/map_image", "pepper_control/MapImage")

    def show_error(self, index, error_code, error_msg):
        if index == 1:
            self.err_i.error_code = error_code
            self.err_i.error_msg = error_msg
            self.err_i.setVisible(True)
        if index == 2:
            self.err_a.error_code = error_code
            self.err_a.error_msg = error_msg
            self.err_a.setVisible(True)
        if index == 3:
            self.err_r.error_code = error_code
            self.err_r.error_msg = error_msg
            self.err_r.setVisible(True)
        if index == 4:
            self.err_c.error_code = error_code
            self.err_c.error_msg = error_msg
            self.err_c.setVisible(True)

    def setup_ui(self):

        def int_button_pressed():
            sl.setCurrentIndex(1)
            self.cam_img_i.connect_ros()
            self.map_img_i.connect_ros()

        def arm_button_pressed():
            sl.setCurrentIndex(2)
            self.cam_img_a.connect_ros()

        def car_button_pressed():
            sl.setCurrentIndex(3)

        def cam_button_pressed():
            sl.setCurrentIndex(4)

        def return_but_pressed():
            sl.setCurrentIndex(0)
            # self.cam_img_i.disconnect_ros()
            # self.map_img_i.disconnect_ros()

        self.menu.setMinimumWidth(10)
        self.menu.setMaximumWidth(70)
        self.menu.setMinimumHeight(800)
        self.menu.setObjectName("menu_bar")
        self.menu.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        h_bl = QHBoxLayout(self)
        h_bl.addWidget(self.menu)
        gl = QGridLayout()
        sl = QStackedLayout(h_bl)
        v_bl = QVBoxLayout()

        sl.addWidget(self.center_box)
        sl.addWidget(self.ing_box)
        sl.addWidget(self.arm_box)
        sl.addWidget(self.car_box)
        sl.addWidget(self.cam_box)
        h_bl.setSpacing(0)
        h_bl.setContentsMargins(0, 0, 0, 0)

        self.center_box.setLayout(v_bl)
        v_bl.addWidget(self.top_box)
        v_bl.addLayout(gl)
        gl.addWidget(self.int_button, 0, 0)
        gl.addWidget(self.arm_button, 0, 1)
        gl.addWidget(self.car_button, 1, 0)
        gl.addWidget(self.cam_button, 1, 1)
        v_bl.setSpacing(0)
        v_bl.setContentsMargins(0, 0, 0, 0)
        v_bl.setStretch(0, 1)
        v_bl.setStretch(1, 2)
        gl.setSpacing(80)
        gl.setContentsMargins(80, 40, 80, 80)

        v_bl_i = QVBoxLayout()
        h_bl_i = QHBoxLayout()

        self.ing_box.setLayout(v_bl_i)
        v_bl_i.addWidget(self.top_box_i)
        v_bl_i.addWidget(self.bot_box_i)
        self.top_box_i.setLayout(h_bl_i)
        h_bl_i.addWidget(self.cam_box_i)
        h_bl_i.addWidget(self.map_box_i)
        v_bl_i.setSpacing(10)
        v_bl_i.setContentsMargins(10, 5, 10, 10)
        h_bl_i.setSpacing(10)
        h_bl_i.setContentsMargins(10, 10, 10, 0)

        v_bl_a = QVBoxLayout()
        h_bl_a = QHBoxLayout()

        self.arm_box.setLayout(v_bl_a)
        v_bl_a.addWidget(self.top_box_a)
        v_bl_a.addWidget(self.bot_box_a)
        self.top_box_a.setLayout(h_bl_a)
        h_bl_a.addWidget(self.cam_box_a)
        h_bl_a.addWidget(self.map_box_a)
        v_bl_a.setSpacing(10)
        v_bl_a.setContentsMargins(10, 5, 10, 10)
        h_bl_a.setSpacing(10)
        h_bl_a.setContentsMargins(10, 10, 10, 0)

        v_bl_r = QVBoxLayout()
        h_bl_r = QHBoxLayout()

        self.car_box.setLayout(v_bl_r)
        v_bl_r.addWidget(self.top_box_r)
        v_bl_r.addWidget(self.bot_box_r)
        self.top_box_r.setLayout(h_bl_r)
        h_bl_r.addWidget(self.cam_box_r)
        h_bl_r.addWidget(self.map_box_r)
        v_bl_r.setSpacing(10)
        v_bl_r.setContentsMargins(10, 5, 10, 10)
        h_bl_r.setSpacing(10)
        h_bl_r.setContentsMargins(10, 10, 10, 0)

        v_bl_c = QVBoxLayout()
        h_bl_c = QHBoxLayout()

        self.cam_box.setLayout(v_bl_c)
        v_bl_c.addWidget(self.top_box_c)
        v_bl_c.addWidget(self.bot_box_c)
        self.err_c.raise_()
        self.top_box_c.setLayout(h_bl_c)
        h_bl_c.addWidget(self.cam_box_c)
        v_bl_c.setSpacing(10)
        v_bl_c.setContentsMargins(10, 5, 10, 10)
        h_bl_c.setSpacing(10)
        h_bl_c.setContentsMargins(10, 10, 10, 0)

        setting_icon = QIcon("resource/images/setting_logo.png")
        self.menu_but.resize(60, 60)
        self.menu_but.setIcon(setting_icon)
        self.menu_but.setIconSize(QSize(50, 50))
        self.menu_but.move(5, self.menu.height() - 20)
        self.menu_but.setCursor(Qt.PointingHandCursor)
        self.menu_but.setObjectName("menu_button")
        self.menu_but.pressed.connect(self.menu_button_pressed)

        self.logo_label.setParent(self.top_box)
        self.logo_label.setMaximumSize(440, 150)
        self.logo_label.setScaledContents(True)
        self.logo_label.move(int(self.width() / 2) - 250, 80)
        logo_pic = QPixmap("resource/images/logo_6.png")
        self.logo_label.setPixmap(logo_pic)

        self.exit_button.setParent(self.menu)
        self.exit_button.resize(60, 60)
        exit_icon = QIcon("resource/images/exit_button.png")
        self.exit_button.setIcon(exit_icon)
        self.exit_button.setIconSize(QSize(50, 50))
        self.exit_button.move(5, self.menu.y() + 20)
        # self.exit_button.setCursor(Qt.PointingHandCursor)
        self.exit_button.setObjectName("exit_button")
        self.exit_button.pressed.connect(self.exit_button_pressed)

        self.maximize_button.setParent(self.menu)
        self.maximize_button.resize(60, 60)
        self.maximize_button.setIcon(self.maximize_icon)
        self.maximize_button.setIconSize(QSize(50, 50))
        self.maximize_button.move(5, self.menu.y() + 100)
        # self.maximize_button.setCursor(Qt.PointingHandCursor)
        self.maximize_button.setObjectName("maximize_button")
        self.maximize_button.pressed.connect(self.maximize_button_pressed)

        self.minimize_button.setParent(self.menu)
        self.minimize_button.resize(60, 60)
        minimize_icon = QIcon("resource/images/minimize_button.png")
        self.minimize_button.setIcon(minimize_icon)
        self.minimize_button.setIconSize(QSize(50, 50))
        self.minimize_button.move(5, self.menu.y() + 180)
        # self.minimize_button.setCursor(Qt.PointingHandCursor)
        self.minimize_button.setObjectName("minimize_button")
        self.minimize_button.pressed.connect(self.minimize_button_pressed)

        self.center_box.setObjectName("center_box")
        self.ing_box.setObjectName("ing_box")
        self.arm_box.setObjectName("arm_box")
        self.car_box.setObjectName("car_box")
        self.cam_box.setObjectName("cam_box")

        self.top_box.setMaximumHeight(250)
        self.int_button.setObjectName("int_button")
        self.arm_button.setObjectName("arm_button")
        self.car_button.setObjectName("car_button")
        self.cam_button.setObjectName("cam_button")

        int_icon = QIcon("resource/images/robotic-rover.png")
        self.int_button.setIcon(int_icon)
        self.int_button.setIconSize(QSize(310, 350))
        self.int_button.setCursor(Qt.PointingHandCursor)
        self.int_button.setText("Integrate Control")
        self.int_button.adjustSize()
        self.int_button.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.int_button.setStyleSheet("border-image: url(resource/images/blue_brush.png);")
        self.int_button.pressed.connect(int_button_pressed)

        arm_icon = QIcon("resource/images/robotic-arm_2.png")
        self.arm_button.setIcon(arm_icon)
        self.arm_button.setIconSize(QSize(315, 350))
        self.arm_button.setCursor(Qt.PointingHandCursor)
        self.arm_button.setText("Arm Control")
        self.arm_button.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.arm_button.setStyleSheet("border-image: url(resource/images/blue_brush.png);")
        self.arm_button.pressed.connect(arm_button_pressed)

        car_icon = QIcon("resource/images/moon-rover.png")
        self.car_button.setIcon(car_icon)
        self.car_button.setIconSize(QSize(315, 358))
        self.car_button.setCursor(Qt.PointingHandCursor)
        self.car_button.setText("Rover Control")
        self.car_button.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.car_button.setStyleSheet("border-image: url(resource/images/blue_brush.png);")
        self.car_button.pressed.connect(car_button_pressed)

        cam_icon = QIcon("resource/images/robot_b.png")
        self.cam_button.setIcon(cam_icon)
        self.cam_button.setIconSize(QSize(292, 353))
        self.cam_button.setCursor(Qt.PointingHandCursor)
        self.cam_button.setText("Camera View")
        self.cam_button.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.cam_button.setStyleSheet("border-image: url(resource/images/blue_brush.png);")
        self.cam_button.pressed.connect(cam_button_pressed)

        self.bot_box_i.setObjectName("bot_box_i")
        self.cam_box_i.setObjectName("cam_box_i")
        self.map_box_i.setObjectName("map_box_i")
        self.cam_box_i.setScaledContents(True)
        self.map_box_i.setScaledContents(True)
        self.cam_box_i.setMovie(self.loading_gif)
        self.map_box_i.setMovie(self.loading_gif)
        # self.cam_box_i.setStyleSheet("background: url(resource/images/pic1.jpg); border-radius: 10px;")
        # self.map_box_i.setStyleSheet("border-image: url(resource/images/pic2.png);")
        self.steer_box_i.setParent(self.bot_box_i)
        self.steer_box_i.resize(490, 490)
        self.steer_box_i.move(20, 20)
        self.steer_box_i.setObjectName("steer_box")
        self.steer_box_i.setStyleSheet("border-image: url(resource/images/add-button.png)")
        self.steer_box_i.setWindowOpacity(0.5)
        gl_i = QGridLayout()
        self.steer_box_i.setLayout(gl_i)
        gl_i.addWidget(self.up_key_i, 0, 1)
        gl_i.addWidget(self.left_key_i, 1, 0)
        gl_i.addWidget(self.stop_key_i, 1, 1)
        gl_i.addWidget(self.right_key_i, 1, 2)
        gl_i.addWidget(self.down_key_i, 2, 1)
        gl_i.setSpacing(0)
        gl_i.setContentsMargins(0, 0, 0, 0)
        up_key_icon = QIcon("resource/images/up-arrow-p.png")
        self.up_key_i.setIcon(up_key_icon)
        self.up_key_i.setIconSize(QSize(80, 80))
        self.up_key_i.setObjectName("up_key")
        self.up_key_i.setCursor(Qt.PointingHandCursor)
        self.up_key_i.pressed.connect(self.up_key_pressed)
        self.up_key_i.released.connect(self.up_key_released)
        down_key_icon = QIcon("resource/images/down-arrow-p.png")
        self.down_key_i.setIcon(down_key_icon)
        self.down_key_i.setIconSize(QSize(80, 80))
        self.down_key_i.setObjectName("down_key")
        self.down_key_i.setCursor(Qt.PointingHandCursor)
        self.down_key_i.pressed.connect(self.down_key_pressed)
        self.down_key_i.released.connect(self.down_key_released)
        left_key_icon = QIcon("resource/images/left-arrow-p.png")
        self.left_key_i.setIcon(left_key_icon)
        self.left_key_i.setIconSize(QSize(80, 80))
        self.left_key_i.setObjectName("left_key")
        self.left_key_i.setCursor(Qt.PointingHandCursor)
        self.left_key_i.pressed.connect(self.left_key_pressed)
        self.left_key_i.released.connect(self.left_key_released)
        right_key_icon = QIcon("resource/images/right-arrow-p.png")
        self.right_key_i.setIcon(right_key_icon)
        self.right_key_i.setIconSize(QSize(80, 80))
        self.right_key_i.setObjectName("right_key")
        self.right_key_i.setCursor(Qt.PointingHandCursor)
        self.right_key_i.pressed.connect(self.right_key_pressed)
        self.right_key_i.released.connect(self.right_key_released)
        stop_key_icon = QIcon("resource/images/stop-button.png")
        self.stop_key_i.setIcon(stop_key_icon)
        self.stop_key_i.setIconSize(QSize(80, 80))
        self.stop_key_i.setObjectName("stop_key")
        self.stop_key_i.setCursor(Qt.PointingHandCursor)
        # self.stop_key_i.pressed.connect(self.stop_key_pressed)
        # self.stop_key_i.released.connect(self.stop_key_released)

        self.prop_box_i.setParent(self.bot_box_i)
        self.prop_box_i.resize(400, 300)
        self.prop_box_i.setStyleSheet("border-width: 0px;")
        prop_gl = QGridLayout()
        self.prop_box_i.setLayout(prop_gl)
        prop_gl.addWidget(self.speed_slider_i, 0, 0)
        prop_gl.addWidget(self.speed_term_i, 1, 0)
        prop_gl.addWidget(self.acl_slider_i, 0, 1)
        prop_gl.addWidget(self.acl_term_i, 1, 1)
        prop_gl.addWidget(self.auto_mode_i, 0, 2)
        prop_gl.addWidget(self.auto_term_i, 1, 2)
        prop_gl.setSpacing(2)
        prop_gl.setContentsMargins(0, 0, 0, 0)
        prop_gl.setAlignment(self.speed_slider_i, Qt.AlignHCenter)
        prop_gl.setAlignment(self.speed_term_i, Qt.AlignHCenter)
        prop_gl.setAlignment(self.acl_slider_i, Qt.AlignHCenter)
        prop_gl.setAlignment(self.auto_mode_i, Qt.AlignVCenter | Qt.AlignHCenter)
        prop_gl.setAlignment(self.auto_term_i, Qt.AlignHCenter)
        prop_gl.setAlignment(self.auto_term_i, Qt.AlignHCenter)
        self.speed_slider_i.setOrientation(Qt.Vertical)
        self.acl_slider_i.setOrientation(Qt.Vertical)
        self.setStyleSheet('''
                    ::handle:vertical{
                        image: url(resource/images/record-b.png);}
                    ::indicator:checked{
                        image: url(resource/images/on-button.png); width: 150px; height: 100px;}
                    ::indicator:unchecked{
                        image: url(resource/images/off-button.png); width: 150px; height: 100px;}
                ''')
        self.speed_label_i.setParent(self.bot_box_i)
        self.speed_label_i.resize(90, 90)
        self.speed_label_i.setStyleSheet("border-image: url(resource/images/message.png)")
        self.speed_label_i.setText(str(self.speed_slider_i.value()))
        self.speed_label_i.setAlignment(Qt.AlignCenter)
        self.speed_label_i.hide()
        self.speed_slider_i.sliderPressed.connect(self.speed_slider_pressed)
        self.speed_slider_i.sliderMoved.connect(self.speed_slider_moved)
        self.speed_slider_i.sliderReleased.connect(self.speed_slider_released)
        self.acl_slider_i.sliderPressed.connect(self.acl_slider_pressed)
        self.acl_slider_i.sliderMoved.connect(self.acl_slider_moved)
        self.acl_slider_i.sliderReleased.connect(self.acl_slider_released)
        self.speed_slider_i.setValue(45)
        self.speed_slider_i.setCursor(Qt.PointingHandCursor)
        self.acl_slider_i.setValue(45)
        self.acl_slider_i.setCursor(Qt.PointingHandCursor)
        self.auto_mode_i.resize(100, 50)
        self.auto_mode_i.setCursor(Qt.PointingHandCursor)
        self.speed_term_i.resize(100, 40)
        self.speed_term_i.setText("(V)")
        self.speed_term_i.setObjectName("speed_label")
        self.speed_term_i.setAlignment(Qt.AlignCenter)
        self.acl_term_i.resize(100, 40)
        self.acl_term_i.setText("(A)")
        self.acl_term_i.setObjectName("accelerate_label")
        self.acl_term_i.setAlignment(Qt.AlignCenter)
        self.auto_term_i.resize(100, 40)
        self.auto_term_i.setText("(auto)")
        self.auto_term_i.setObjectName("auto_label")
        self.auto_term_i.setAlignment(Qt.AlignLeft)

        self.grip_box_i.setParent(self.bot_box_i)
        self.grip_box_i.resize(400, 300)
        self.grip_box_i.setObjectName("grip_box")
        self.grip_box_i.setStyleSheet("border-width: 0px;")
        grip_bl = QHBoxLayout()
        self.grip_box_i.setLayout(grip_bl)
        grip_bl.addWidget(self.grip_button_i)
        grip_bl.addWidget(self.grip_auto_i)
        grip_bl.setSpacing(0)
        grip_bl.setContentsMargins(0, 0, 0, 0)
        grip_bl.setAlignment(self.grip_button_i, Qt.AlignHCenter)
        grip_bl.setAlignment(self.grip_auto_i, Qt.AlignLeft)
        self.grip_button_i.resize(100, 100)
        grip_button = QIcon("resource/images/robot-gripper.png")
        self.grip_button_i.setIcon(grip_button)
        self.grip_button_i.setIconSize(QSize(200, 200))
        self.grip_button_i.setObjectName("grip_button")
        self.grip_button_i.setCursor(Qt.PointingHandCursor)
        self.grip_button_i.pressed.connect(self.grip_button_pressed)
        self.grip_auto_i.setCursor(Qt.PointingHandCursor)

        self.grip_steer_box_i.setParent(self.bot_box_i)
        self.grip_steer_box_i.resize(280, 280)
        self.grip_steer_box_i.setObjectName("grip_steer_box")
        self.grip_steer_box_i.setStyleSheet("border-image: url(resource/images/circle.png);")
        grip_steer_gl = QGridLayout()
        self.grip_steer_box_i.setLayout(grip_steer_gl)
        grip_steer_gl.addWidget(self.grip_up_key_i, 0, 1)
        grip_steer_gl.addWidget(self.grip_left_key_i, 1, 0)
        grip_steer_gl.addWidget(self.grip_right_key_i, 1, 2)
        grip_steer_gl.addWidget(self.grip_down_key_i, 2, 1)
        grip_steer_gl.setSpacing(0)
        grip_steer_gl.setContentsMargins(0, 0, 0, 0)
        grip_up = QIcon("resource/images/up-b.png")
        self.grip_up_key_i.setIcon(grip_up)
        self.grip_up_key_i.setIconSize(QSize(90, 90))
        self.grip_up_key_i.setCursor(Qt.PointingHandCursor)
        self.grip_up_key_i.setObjectName("grip_up")
        self.grip_up_key_i.pressed.connect(self.grip_up_pressed)
        self.grip_up_key_i.released.connect(self.grip_up_released)
        grip_down = QIcon("resource/images/down-b.png")
        self.grip_down_key_i.setIcon(grip_down)
        self.grip_down_key_i.setIconSize(QSize(90, 90))
        self.grip_down_key_i.setCursor(Qt.PointingHandCursor)
        self.grip_down_key_i.setObjectName("grip_down")
        self.grip_down_key_i.pressed.connect(self.grip_down_pressed)
        self.grip_down_key_i.released.connect(self.grip_down_released)
        grip_left = QIcon("resource/images/left-b.png")
        self.grip_left_key_i.setIcon(grip_left)
        self.grip_left_key_i.setIconSize(QSize(90, 90))
        self.grip_left_key_i.setCursor(Qt.PointingHandCursor)
        self.grip_left_key_i.setObjectName("grip_left")
        self.grip_left_key_i.pressed.connect(self.grip_left_pressed)
        self.grip_left_key_i.released.connect(self.grip_left_released)
        grip_right = QIcon("resource/images/right-b.png")
        self.grip_right_key_i.setIcon(grip_right)
        self.grip_right_key_i.setIconSize(QSize(90, 90))
        self.grip_right_key_i.setCursor(Qt.PointingHandCursor)
        self.grip_right_key_i.setObjectName("grip_right")
        self.grip_right_key_i.pressed.connect(self.grip_right_pressed)
        self.grip_right_key_i.released.connect(self.grip_right_released)

        self.cam_control_box_i.setParent(self.bot_box_i)
        self.cam_control_box_i.resize(360, 360)
        self.cam_control_box_i.setObjectName("cam_control_box")
        self.cam_control_box_i.setStyleSheet("border-image: url(resource/images/circle-b.png);")

        self.cam_button_i.setParent(self.cam_control_box_i)
        self.cam_button_i.resize(250, 250)
        self.cam_button_i.move(57, 57)
        self.cam_button_i.setObjectName("cam_button_i")

        cam_gl = QGridLayout()
        self.cam_button_i.setLayout(cam_gl)
        self.cam_button_i.setStyleSheet("border-image: url(resource/images/circle.png);")
        cam_gl.addWidget(self.cam_up_i, 0, 1)
        cam_gl.addWidget(self.cam_down_i, 2, 1)
        cam_gl.addWidget(self.cam_left_i, 1, 0)
        cam_gl.addWidget(self.cam_right_i, 1, 2)
        self.cam_up_i.setObjectName("cam_up")
        self.cam_down_i.setObjectName("cam_down")
        self.cam_left_i.setObjectName("cam_left")
        self.cam_right_i.setObjectName("cam_right")
        self.cam_up_i.setCursor(Qt.PointingHandCursor)
        self.cam_down_i.setCursor(Qt.PointingHandCursor)
        self.cam_left_i.setCursor(Qt.PointingHandCursor)
        self.cam_right_i.setCursor(Qt.PointingHandCursor)
        cam_up = QIcon("resource/images/arrow_up.png")
        cam_down = QIcon("resource/images/arrow_down.png")
        cam_left = QIcon("resource/images/arrow_left.png")
        cam_right = QIcon("resource/images/arrow_right.png")
        self.cam_up_i.setIcon(cam_up)
        self.cam_down_i.setIcon(cam_down)
        self.cam_left_i.setIcon(cam_left)
        self.cam_right_i.setIcon(cam_right)
        self.cam_up_i.setIconSize(QSize(60, 60))
        self.cam_down_i.setIconSize(QSize(60, 60))
        self.cam_left_i.setIconSize(QSize(60, 60))
        self.cam_right_i.setIconSize(QSize(60, 60))
        self.cam_up_i.pressed.connect(self.cam_up_pressed)
        self.cam_down_i.pressed.connect(self.cam_down_pressed)
        self.cam_left_i.pressed.connect(self.cam_left_pressed)
        self.cam_right_i.pressed.connect(self.cam_right_pressed)
        self.cam_up_i.released.connect(self.cam_up_released)
        self.cam_down_i.released.connect(self.cam_down_released)
        self.cam_left_i.released.connect(self.cam_left_released)
        self.cam_right_i.released.connect(self.cam_right_released)

        self.return_but_i.setParent(self.bot_box_i)
        self.err_i.raise_()
        return_but = QIcon("resource/images/return-g.png")
        self.return_but_i.setIcon(return_but)
        self.return_but_i.setIconSize(QSize(80, 80))
        self.return_but_i.setCursor(Qt.PointingHandCursor)
        self.return_but_i.setObjectName("return_but")
        self.return_but_i.pressed.connect(return_but_pressed)

        bot_hbl = QHBoxLayout()
        bot_vbl = QVBoxLayout()
        bot_v3bl = QVBoxLayout()
        self.bot_box_a.setLayout(bot_hbl)
        self.bot_box_a.setObjectName("bot_box_a")
        self.cam_box_a.setScaledContents(True)
        self.cam_box_a.setObjectName("cam_box_a")
        self.map_box_a.setScaledContents(True)
        self.map_box_a.setObjectName("map_box_a")
        self.cam_box_a.setMovie(self.loading_gif)
        self.map_box_a.setMovie(self.loading_gif)
        # self.cam_box_a.setStyleSheet("border-image: url(resource/images/pic1.jpg); border-radius: 10px;")
        # self.map_box_a.setStyleSheet("border-image: url(resource/images/pic2.png); border-radius: 10px;")
        bot_hbl.addWidget(self.steer_box_a)
        bot_hbl.addLayout(bot_vbl)
        bot_hbl.addLayout(bot_v3bl)
        self.steer_box_a.resize(490, 490)
        # self.steer_box_a.move(20, 0)
        self.steer_box_a.setObjectName("steer_box")
        self.steer_box_a.setStyleSheet("border-image: url(resource/images/add-button.png)")
        self.steer_box_a.setWindowOpacity(0.5)
        gl_a = QGridLayout()
        self.steer_box_a.setLayout(gl_a)
        gl_a.addWidget(self.up_key_a, 0, 1)
        gl_a.addWidget(self.left_key_a, 1, 0)
        gl_a.addWidget(self.stop_key_a, 1, 1)
        gl_a.addWidget(self.right_key_a, 1, 2)
        gl_a.addWidget(self.down_key_a, 2, 1)
        gl_a.setSpacing(0)
        gl_a.setContentsMargins(0, 0, 0, 0)
        up_key_icon = QIcon("resource/images/up-arrow-p.png")
        self.up_key_a.setIcon(up_key_icon)
        self.up_key_a.setIconSize(QSize(80, 80))
        self.up_key_a.setObjectName("up_key")
        self.up_key_a.setCursor(Qt.PointingHandCursor)
        self.up_key_a.pressed.connect(self.up_key_pressed)
        self.up_key_a.released.connect(self.up_key_released)
        down_key_icon = QIcon("resource/images/down-arrow-p.png")
        self.down_key_a.setIcon(down_key_icon)
        self.down_key_a.setIconSize(QSize(80, 80))
        self.down_key_a.setObjectName("down_key")
        self.down_key_a.setCursor(Qt.PointingHandCursor)
        self.down_key_a.pressed.connect(self.down_key_pressed)
        self.down_key_a.released.connect(self.down_key_released)
        left_key_icon = QIcon("resource/images/left-arrow-p.png")
        self.left_key_a.setIcon(left_key_icon)
        self.left_key_a.setIconSize(QSize(80, 80))
        self.left_key_a.setObjectName("left_key")
        self.left_key_a.setCursor(Qt.PointingHandCursor)
        self.left_key_a.pressed.connect(self.left_key_pressed)
        self.left_key_a.released.connect(self.left_key_released)
        right_key_icon = QIcon("resource/images/right-arrow-p.png")
        self.right_key_a.setIcon(right_key_icon)
        self.right_key_a.setIconSize(QSize(80, 80))
        self.right_key_a.setObjectName("right_key")
        self.right_key_a.setCursor(Qt.PointingHandCursor)
        self.right_key_a.pressed.connect(self.right_key_pressed)
        self.right_key_a.released.connect(self.right_key_released)
        stop_key_icon = QIcon("resource/images/stop-button.png")
        self.stop_key_a.setIcon(stop_key_icon)
        self.stop_key_a.setIconSize(QSize(80, 80))
        self.stop_key_a.setObjectName("stop_key")
        self.stop_key_a.setCursor(Qt.PointingHandCursor)
        # self.stop_key_a.pressed.connect(self.stop_key_pressed)
        # self.stop_key_a.released.connect(self.stop_key_released)

        bot_vbl.addWidget(self.return_but_a)
        bot_vbl.addSpacing(150)
        bot_vbl.addWidget(self.grip_box_a)
        self.err_a.raise_()
        # bot_vbl.addWidget(self.prop_box_a)
        bot_vbl.setAlignment(self.return_but_a, Qt.AlignCenter)
        bot_vbl.setSpacing(20)
        bot_vbl.setContentsMargins(0, 0, 0, 0)
        self.return_but_a.setIcon(return_but)
        self.return_but_a.setIconSize(QSize(80, 80))
        self.return_but_a.setCursor(Qt.PointingHandCursor)
        self.return_but_a.setObjectName("return_but")
        self.return_but_a.pressed.connect(return_but_pressed)

        self.grip_box_a.resize(400, 300)
        self.grip_box_a.setObjectName("grip_box")
        self.grip_box_a.setStyleSheet("border-width: 0px;")
        grip_bl_a = QHBoxLayout()
        self.grip_box_a.setLayout(grip_bl_a)
        grip_bl_a.addWidget(self.grip_button_a)
        grip_bl_a.addWidget(self.grip_auto_a)
        grip_bl_a.setSpacing(0)
        grip_bl_a.setContentsMargins(0, 0, 0, 0)
        grip_bl_a.setAlignment(self.grip_button_a, Qt.AlignHCenter)
        grip_bl_a.setAlignment(self.grip_auto_a, Qt.AlignLeft)
        self.grip_button_a.resize(100, 100)
        self.grip_button_a.setIcon(grip_button)
        self.grip_button_a.setIconSize(QSize(200, 200))
        self.grip_button_a.setObjectName("grip_button")
        self.grip_button_a.setCursor(Qt.PointingHandCursor)
        self.grip_button_a.pressed.connect(self.grip_button_pressed)
        self.grip_auto_a.setCursor(Qt.PointingHandCursor)

        bot_v3bl.addWidget(self.grip_steer_box_a)
        bot_v3bl.addWidget(self.prop_box_a)
        # bot_vbl.addWidget(self.prop_box_a)
        bot_v3bl.setAlignment(self.prop_box_a, Qt.AlignLeft | Qt.AlignBottom)
        bot_v3bl.setAlignment(self.grip_steer_box_a, Qt.AlignHCenter | Qt.AlignBottom)
        bot_v3bl.setSpacing(10)
        bot_v3bl.setContentsMargins(0, 20, 0, 0)
        self.prop_box_a.setStyleSheet("border-width: 0px;")
        prop_gl_a = QGridLayout()
        self.prop_box_a.setLayout(prop_gl_a)
        prop_gl_a.addWidget(self.speed_slider_a, 0, 0)
        prop_gl_a.addWidget(self.speed_term_a, 1, 0)
        prop_gl_a.addWidget(self.acl_slider_a, 0, 1)
        prop_gl_a.addWidget(self.acl_term_a, 1, 1)
        prop_gl_a.setSpacing(15)
        prop_gl_a.setContentsMargins(0, 0, 0, 0)
        prop_gl_a.setAlignment(self.speed_slider_a, Qt.AlignHCenter)
        prop_gl_a.setAlignment(self.speed_term_a, Qt.AlignHCenter)
        prop_gl_a.setAlignment(self.acl_slider_a, Qt.AlignHCenter)
        prop_gl_a.setAlignment(self.auto_mode_a, Qt.AlignVCenter | Qt.AlignHCenter)
        prop_gl_a.setAlignment(self.auto_term_a, Qt.AlignHCenter)
        prop_gl_a.setAlignment(self.auto_term_a, Qt.AlignHCenter)
        self.speed_slider_a.setOrientation(Qt.Vertical)
        self.acl_slider_a.setOrientation(Qt.Vertical)

        self.speed_label_a.setParent(self.bot_box_a)
        self.speed_label_a.resize(90, 90)
        self.speed_label_a.setStyleSheet("border-image: url(resource/images/message.png)")
        self.speed_label_a.setText(str(self.speed_slider_a.value()))
        self.speed_label_a.setAlignment(Qt.AlignCenter)
        self.speed_label_a.hide()
        self.speed_slider_a.sliderPressed.connect(self.speed_slider_pressed)
        self.speed_slider_a.sliderMoved.connect(self.speed_slider_moved)
        self.speed_slider_a.sliderReleased.connect(self.speed_slider_released)
        self.acl_slider_a.sliderPressed.connect(self.acl_slider_pressed)
        self.acl_slider_a.sliderMoved.connect(self.acl_slider_moved)
        self.acl_slider_a.sliderReleased.connect(self.acl_slider_released)
        self.speed_slider_a.setValue(45)
        self.speed_slider_a.setCursor(Qt.PointingHandCursor)
        self.acl_slider_a.setValue(45)
        self.acl_slider_a.setCursor(Qt.PointingHandCursor)
        self.speed_term_a.resize(100, 40)
        self.speed_term_a.setText("(V)")
        self.speed_term_a.setObjectName("speed_label")
        self.speed_term_a.setAlignment(Qt.AlignCenter)
        self.acl_term_a.resize(100, 40)
        self.acl_term_a.setText("(A)")
        self.acl_term_a.setObjectName("accelerate_label")
        self.acl_term_a.setAlignment(Qt.AlignCenter)

        self.grip_steer_box_a.resize(280, 280)
        self.grip_steer_box_a.setObjectName("grip_steer_box")
        self.grip_steer_box_a.setStyleSheet("border-image: url(resource/images/circle.png);")
        grip_steer_gl_a = QGridLayout()
        self.grip_steer_box_a.setLayout(grip_steer_gl_a)
        grip_steer_gl_a.addWidget(self.grip_up_key_a, 0, 1)
        grip_steer_gl_a.addWidget(self.grip_left_key_a, 1, 0)
        grip_steer_gl_a.addWidget(self.grip_right_key_a, 1, 2)
        grip_steer_gl_a.addWidget(self.grip_down_key_a, 2, 1)
        grip_steer_gl_a.setSpacing(0)
        grip_steer_gl_a.setContentsMargins(0, 0, 0, 0)
        self.grip_up_key_a.setIcon(grip_up)
        self.grip_up_key_a.setIconSize(QSize(90, 90))
        self.grip_up_key_a.setCursor(Qt.PointingHandCursor)
        self.grip_up_key_a.setObjectName("grip_up")
        self.grip_up_key_a.pressed.connect(self.grip_up_pressed)
        self.grip_up_key_a.released.connect(self.grip_up_released)
        self.grip_down_key_a.setIcon(grip_down)
        self.grip_down_key_a.setIconSize(QSize(90, 90))
        self.grip_down_key_a.setCursor(Qt.PointingHandCursor)
        self.grip_down_key_a.setObjectName("grip_down")
        self.grip_down_key_a.pressed.connect(self.grip_down_pressed)
        self.grip_down_key_a.released.connect(self.grip_down_released)
        self.grip_left_key_a.setIcon(grip_left)
        self.grip_left_key_a.setIconSize(QSize(90, 90))
        self.grip_left_key_a.setCursor(Qt.PointingHandCursor)
        self.grip_left_key_a.setObjectName("grip_left")
        self.grip_left_key_a.pressed.connect(self.grip_left_pressed)
        self.grip_left_key_a.released.connect(self.grip_left_released)
        self.grip_right_key_a.setIcon(grip_right)
        self.grip_right_key_a.setIconSize(QSize(90, 90))
        self.grip_right_key_a.setCursor(Qt.PointingHandCursor)
        self.grip_right_key_a.setObjectName("grip_right")
        self.grip_right_key_a.pressed.connect(self.grip_right_pressed)
        self.grip_right_key_a.released.connect(self.grip_right_released)

        botr_hbl = QHBoxLayout()
        botr_vbl = QVBoxLayout()
        botr_v3bl = QVBoxLayout()
        self.bot_box_r.setLayout(botr_hbl)
        self.bot_box_r.setObjectName("bot_box_r")
        self.bot_box_r.setObjectName("bot_box_r")
        self.cam_box_r.setScaledContents(True)
        self.cam_box_r.setObjectName("cam_box_r")
        self.map_box_r.setScaledContents(True)
        self.map_box_r.setObjectName("map_box_r")
        self.cam_box_r.setMovie(self.loading_gif)
        self.map_box_r.setMovie(self.loading_gif)
        # self.cam_box_r.setStyleSheet("border-image: url(resource/images/pic1.jpg); border-radius: 10px;")
        # self.map_box_r.setStyleSheet("border-image: url(resource/images/pic2.png); border-radius: 10px;")
        botr_hbl.addWidget(self.steer_box_r)
        botr_hbl.addLayout(botr_vbl)
        botr_hbl.addLayout(botr_v3bl)
        # self.steer_box_r.move(20, 0)
        self.steer_box_r.setObjectName("steer_box")
        self.steer_box_r.setStyleSheet("border-image: url(resource/images/add-button.png)")
        self.steer_box_r.setWindowOpacity(0.5)
        gl_r = QGridLayout()
        self.steer_box_r.setLayout(gl_r)
        gl_r.addWidget(self.up_key_r, 0, 1)
        gl_r.addWidget(self.left_key_r, 1, 0)
        gl_r.addWidget(self.stop_key_r, 1, 1)
        gl_r.addWidget(self.right_key_r, 1, 2)
        gl_r.addWidget(self.down_key_r, 2, 1)
        gl_r.setSpacing(0)
        gl_r.setContentsMargins(0, 0, 0, 0)
        up_key_icon = QIcon("resource/images/up-arrow-p.png")
        self.up_key_r.setIcon(up_key_icon)
        self.up_key_r.setIconSize(QSize(80, 80))
        self.up_key_r.setObjectName("up_key")
        self.up_key_r.setCursor(Qt.PointingHandCursor)
        self.up_key_r.pressed.connect(self.up_key_pressed)
        self.up_key_r.released.connect(self.up_key_released)
        down_key_icon = QIcon("resource/images/down-arrow-p.png")
        self.down_key_r.setIcon(down_key_icon)
        self.down_key_r.setIconSize(QSize(80, 80))
        self.down_key_r.setObjectName("down_key")
        self.down_key_r.setCursor(Qt.PointingHandCursor)
        self.down_key_r.pressed.connect(self.down_key_pressed)
        self.down_key_r.released.connect(self.down_key_released)
        left_key_icon = QIcon("resource/images/left-arrow-p.png")
        self.left_key_r.setIcon(left_key_icon)
        self.left_key_r.setIconSize(QSize(80, 80))
        self.left_key_r.setObjectName("left_key")
        self.left_key_r.setCursor(Qt.PointingHandCursor)
        self.left_key_r.pressed.connect(self.left_key_pressed)
        self.left_key_r.released.connect(self.left_key_released)
        right_key_icon = QIcon("resource/images/right-arrow-p.png")
        self.right_key_r.setIcon(right_key_icon)
        self.right_key_r.setIconSize(QSize(80, 80))
        self.right_key_r.setObjectName("right_key")
        self.right_key_r.setCursor(Qt.PointingHandCursor)
        self.right_key_r.pressed.connect(self.right_key_pressed)
        self.right_key_r.released.connect(self.right_key_released)
        stop_key_icon = QIcon("resource/images/stop-button.png")
        self.stop_key_r.setIcon(stop_key_icon)
        self.stop_key_r.setIconSize(QSize(80, 80))
        self.stop_key_r.setObjectName("stop_key")
        self.stop_key_r.setCursor(Qt.PointingHandCursor)
        # self.stop_key_r.pressed.connect(self.stop_key_pressed)
        # self.stop_key_r.released.connect(self.stop_key_released)

        botr_vbl.addWidget(self.return_but_r)
        botr_vbl.addSpacing(150)
        botr_vbl.addWidget(self.grip_box_r)
        self.err_r.raise_()
        # botr_vbl.addWidget(self.prop_box_r)
        botr_vbl.setAlignment(self.return_but_r, Qt.AlignCenter)
        botr_vbl.setSpacing(20)
        botr_vbl.setContentsMargins(0, 0, 0, 0)
        self.return_but_r.setIcon(return_but)
        self.return_but_r.setIconSize(QSize(80, 80))
        self.return_but_r.setCursor(Qt.PointingHandCursor)
        self.return_but_r.setObjectName("return_but")
        self.return_but_r.pressed.connect(return_but_pressed)

        self.grip_box_r.resize(400, 300)
        self.grip_box_r.setObjectName("grip_box")
        self.grip_box_r.setStyleSheet("border-width: 0px;")
        grip_bl_r = QHBoxLayout()
        self.grip_box_r.setLayout(grip_bl_r)
        grip_bl_r.addWidget(self.grip_button_r)
        grip_bl_r.addWidget(self.grip_auto_r)
        grip_bl_r.setSpacing(0)
        grip_bl_r.setContentsMargins(0, 0, 0, 0)
        grip_bl_r.setAlignment(self.grip_button_r, Qt.AlignHCenter)
        grip_bl_r.setAlignment(self.grip_auto_r, Qt.AlignLeft)
        self.grip_button_r.resize(100, 100)
        map_button = QIcon("resource/images/location.png")
        self.grip_button_r.setIcon(map_button)
        self.grip_button_r.setIconSize(QSize(200, 200))
        self.grip_button_r.setObjectName("grip_button")
        self.grip_button_r.setCursor(Qt.PointingHandCursor)
        self.grip_button_r.pressed.connect(self.grip_button_pressed)
        self.grip_auto_r.setCursor(Qt.PointingHandCursor)

        botr_v3bl.addWidget(self.grip_steer_box_r)
        botr_v3bl.addWidget(self.prop_box_r)
        # botr_vbl.addWidget(self.prop_box_r)
        botr_v3bl.setAlignment(self.prop_box_r, Qt.AlignLeft | Qt.AlignBottom)
        botr_v3bl.setAlignment(self.grip_steer_box_r, Qt.AlignHCenter | Qt.AlignBottom)
        botr_v3bl.setSpacing(10)
        botr_v3bl.setContentsMargins(0, 20, 0, 0)
        self.prop_box_r.setStyleSheet("border-width: 0px;")
        prop_gl_r = QGridLayout()
        self.prop_box_r.setLayout(prop_gl_r)
        prop_gl_r.addWidget(self.speed_slider_r, 0, 0)
        prop_gl_r.addWidget(self.speed_term_r, 1, 0)
        prop_gl_r.addWidget(self.acl_slider_r, 0, 1)
        prop_gl_r.addWidget(self.acl_term_r, 1, 1)
        prop_gl_r.addWidget(self.auto_mode_r, 0, 2)
        prop_gl_r.addWidget(self.auto_term_r, 1, 2)
        prop_gl_r.setSpacing(15)
        prop_gl_r.setContentsMargins(0, 0, 0, 0)
        prop_gl_r.setAlignment(self.speed_slider_r, Qt.AlignHCenter)
        prop_gl_r.setAlignment(self.speed_term_r, Qt.AlignHCenter)
        prop_gl_r.setAlignment(self.acl_slider_r, Qt.AlignHCenter)
        prop_gl_r.setAlignment(self.auto_mode_r, Qt.AlignVCenter | Qt.AlignHCenter)
        prop_gl_r.setAlignment(self.auto_term_r, Qt.AlignHCenter)
        prop_gl_r.setAlignment(self.auto_term_r, Qt.AlignHCenter)
        self.speed_slider_r.setOrientation(Qt.Vertical)
        self.acl_slider_r.setOrientation(Qt.Vertical)

        self.speed_label_r.setParent(self.bot_box_r)
        self.speed_label_r.resize(90, 90)
        self.speed_label_r.setStyleSheet("border-image: url(resource/images/message.png)")
        self.speed_label_r.setText(str(self.speed_slider_a.value()))
        self.speed_label_r.setAlignment(Qt.AlignCenter)
        self.speed_label_r.hide()
        self.speed_slider_r.sliderPressed.connect(self.speed_slider_pressed)
        self.speed_slider_r.sliderMoved.connect(self.speed_slider_moved)
        self.speed_slider_r.sliderReleased.connect(self.speed_slider_released)
        self.acl_slider_r.sliderPressed.connect(self.acl_slider_pressed)
        self.acl_slider_r.sliderMoved.connect(self.acl_slider_moved)
        self.acl_slider_r.sliderReleased.connect(self.acl_slider_released)
        self.speed_slider_r.setValue(45)
        self.speed_slider_r.setCursor(Qt.PointingHandCursor)
        self.acl_slider_r.setValue(45)
        self.acl_slider_r.setCursor(Qt.PointingHandCursor)
        self.speed_term_r.resize(100, 40)
        self.speed_term_r.setText("(V)")
        self.speed_term_r.setObjectName("speed_label")
        self.speed_term_r.setAlignment(Qt.AlignCenter)
        self.acl_term_r.resize(100, 40)
        self.acl_term_r.setText("(A)")
        self.acl_term_r.setObjectName("accelerate_label")
        self.acl_term_r.setAlignment(Qt.AlignCenter)
        self.auto_mode_r.resize(100, 50)
        self.auto_mode_r.setCursor(Qt.PointingHandCursor)
        self.auto_term_r.resize(100, 40)
        self.auto_term_r.setText("(auto)")
        self.auto_term_r.setObjectName("auto_label")
        self.auto_term_r.setAlignment(Qt.AlignLeft)

        self.grip_steer_box_r.resize(280, 280)
        self.grip_steer_box_r.setObjectName("grip_steer_box")
        self.grip_steer_box_r.setStyleSheet("border-image: url(resource/images/circle.png);")
        grip_steer_gl_r = QGridLayout()
        self.grip_steer_box_r.setLayout(grip_steer_gl_r)
        grip_steer_gl_r.addWidget(self.grip_up_key_r, 0, 1)
        grip_steer_gl_r.addWidget(self.grip_left_key_r, 1, 0)
        grip_steer_gl_r.addWidget(self.grip_right_key_r, 1, 2)
        grip_steer_gl_r.addWidget(self.grip_down_key_r, 2, 1)
        grip_steer_gl_r.setSpacing(0)
        grip_steer_gl_r.setContentsMargins(0, 0, 0, 0)
        self.grip_up_key_r.setIcon(grip_up)
        self.grip_up_key_r.setIconSize(QSize(90, 90))
        self.grip_up_key_r.setCursor(Qt.PointingHandCursor)
        self.grip_up_key_r.setObjectName("grip_up")
        self.grip_up_key_r.pressed.connect(self.grip_up_pressed)
        self.grip_up_key_r.released.connect(self.grip_up_released)
        self.grip_down_key_r.setIcon(grip_down)
        self.grip_down_key_r.setIconSize(QSize(90, 90))
        self.grip_down_key_r.setCursor(Qt.PointingHandCursor)
        self.grip_down_key_r.setObjectName("grip_down")
        self.grip_down_key_r.pressed.connect(self.grip_down_pressed)
        self.grip_down_key_r.released.connect(self.grip_down_released)
        self.grip_left_key_r.setIcon(grip_left)
        self.grip_left_key_r.setIconSize(QSize(90, 90))
        self.grip_left_key_r.setCursor(Qt.PointingHandCursor)
        self.grip_left_key_r.setObjectName("grip_left")
        self.grip_left_key_r.pressed.connect(self.grip_left_pressed)
        self.grip_left_key_r.released.connect(self.grip_left_released)
        self.grip_right_key_r.setIcon(grip_right)
        self.grip_right_key_r.setIconSize(QSize(90, 90))
        self.grip_right_key_r.setCursor(Qt.PointingHandCursor)
        self.grip_right_key_r.setObjectName("grip_right")
        self.grip_right_key_r.pressed.connect(self.grip_right_pressed)
        self.grip_right_key_r.released.connect(self.grip_right_released)

        botc_hbl = QHBoxLayout()
        bot_vbl_c = QVBoxLayout()
        cmb_vbl_c = QVBoxLayout()
        self.bot_box_c.setLayout(botc_hbl)
        self.bot_box_c.setObjectName("bot_box_c")
        self.cam_box_c.setScaledContents(True)
        self.cam_box_c.setObjectName("cam_box_c")
        self.cam_box_c.setMovie(self.loading_gif)
        # self.cam_box_c.setStyleSheet("border-image: url(resource/images/depth_camera.png); border-radius: 10px;")
        botc_hbl.addWidget(self.prop_box_c)
        botc_hbl.addLayout(bot_vbl_c)
        botc_hbl.addLayout(cmb_vbl_c)
        botc_hbl.setAlignment(self.prop_box_c, Qt.AlignCenter)
        botc_hbl.setSpacing(10)
        botc_hbl.setContentsMargins(0, 20, 0, 0)
        self.prop_box_c.setStyleSheet("border-width: 0px;")
        prop_gl_c = QGridLayout()
        self.prop_box_c.setLayout(prop_gl_c)
        prop_gl_c.addWidget(self.view_term_ac, 0, 0)
        prop_gl_c.addWidget(self.view_slider_c, 1, 0)
        prop_gl_c.addWidget(self.view_term_pc, 2, 0)
        prop_gl_c.addWidget(self.acl_slider_c, 1, 1)
        prop_gl_c.addWidget(self.acl_term_c, 2, 1)
        prop_gl_c.addWidget(self.auto_mode_c, 1, 2)
        prop_gl_c.addWidget(self.auto_term_c, 2, 2)
        prop_gl_c.setSpacing(15)
        prop_gl_c.setContentsMargins(0, 0, 0, 0)
        prop_gl_c.setAlignment(self.view_slider_c, Qt.AlignHCenter)
        prop_gl_c.setAlignment(self.view_term_pc, Qt.AlignHCenter)
        prop_gl_c.setAlignment(self.view_term_ac, Qt.AlignHCenter)
        prop_gl_c.setAlignment(self.acl_slider_c, Qt.AlignHCenter)
        prop_gl_c.setAlignment(self.auto_mode_c, Qt.AlignVCenter | Qt.AlignHCenter)
        prop_gl_c.setAlignment(self.auto_term_c, Qt.AlignHCenter)
        prop_gl_c.setAlignment(self.auto_term_c, Qt.AlignHCenter)
        self.view_slider_c.setOrientation(Qt.Vertical)
        self.acl_slider_c.setOrientation(Qt.Vertical)

        self.view_label_c.setParent(self.bot_box_c)
        self.view_label_c.resize(90, 90)
        self.view_label_c.setStyleSheet("border-image: url(resource/images/message.png)")
        self.view_label_c.setText(str(self.view_slider_c.value()))
        self.view_label_c.setAlignment(Qt.AlignCenter)
        self.view_label_c.hide()
        self.view_slider_c.sliderPressed.connect(self.view_slider_pressed)
        self.view_slider_c.sliderMoved.connect(self.view_slider_moved)
        self.view_slider_c.sliderReleased.connect(self.view_slider_released)
        # self.acl_slider_c.sliderPressed.connect(self.acl_slider_pressed)
        # self.acl_slider_c.sliderMoved.connect(self.acl_slider_moved)
        # self.acl_slider_c.sliderReleased.connect(self.acl_slider_released)
        self.view_slider_c.setValue(45)
        self.view_slider_c.setCursor(Qt.PointingHandCursor)
        self.acl_slider_c.setValue(45)
        self.acl_slider_c.setCursor(Qt.PointingHandCursor)

        self.view_term_pc.resize(100, 40)
        self.view_term_pc.setText("(-)")
        self.view_term_pc.setObjectName("speed_label_p")
        self.view_term_pc.setAlignment(Qt.AlignCenter)
        self.view_term_ac.resize(100, 40)
        self.view_term_ac.setText("(+)")
        self.view_term_ac.setObjectName("speed_label_a")
        self.view_term_ac.setAlignment(Qt.AlignCenter)

        self.acl_term_c.resize(100, 40)
        self.acl_term_c.setText("")
        self.acl_term_c.setObjectName("accelerate_label")
        self.acl_term_c.setAlignment(Qt.AlignCenter)
        self.auto_mode_c.resize(100, 50)
        self.auto_mode_c.setCursor(Qt.PointingHandCursor)
        self.auto_term_c.resize(100, 40)
        self.auto_term_c.setText("(auto)")
        self.auto_term_c.setObjectName("auto_label")
        self.auto_term_c.setAlignment(Qt.AlignLeft)

        bot_vbl_c.addWidget(self.return_but_c)
        bot_vbl_c.addWidget(self.cam_control_box_c)
        bot_vbl_c.setSpacing(15)
        bot_vbl_c.setContentsMargins(0, 0, 0, 20)
        self.cam_control_box_c.resize(360, 360)
        self.cam_control_box_c.setObjectName("cam_control_box")
        self.cam_control_box_c.setStyleSheet("border-image: url(resource/images/circle-b.png);")
        cam_bl_c = QVBoxLayout()
        self.cam_control_box_c.setLayout(cam_bl_c)
        cam_bl_c.addWidget(self.cam_button_c)
        self.cam_button_c.setObjectName("cam_button")
        cam_gl_c = QGridLayout()
        self.cam_button_c.setLayout(cam_gl_c)
        self.cam_button_c.setStyleSheet("border-image: url(resource/images/circle.png);")
        cam_gl_c.addWidget(self.cam_up_c, 0, 1)
        cam_gl_c.addWidget(self.cam_down_c, 2, 1)
        cam_gl_c.addWidget(self.cam_left_c, 1, 0)
        cam_gl_c.addWidget(self.cam_right_c, 1, 2)
        self.cam_up_c.setObjectName("cam_up")
        self.cam_down_c.setObjectName("cam_down")
        self.cam_left_c.setObjectName("cam_left")
        self.cam_right_c.setObjectName("cam_right")
        self.cam_up_c.setCursor(Qt.PointingHandCursor)
        self.cam_down_c.setCursor(Qt.PointingHandCursor)
        self.cam_left_c.setCursor(Qt.PointingHandCursor)
        self.cam_right_c.setCursor(Qt.PointingHandCursor)
        # cam_up = QIcon("resource/images/arrow_up.png")
        # cam_down = QIcon("resource/images/arrow_down.png")
        # cam_left = QIcon("resource/images/arrow_left.png")
        # cam_right = QIcon("resource/images/arrow_right.png")
        self.cam_up_c.setIcon(cam_up)
        self.cam_down_c.setIcon(cam_down)
        self.cam_left_c.setIcon(cam_left)
        self.cam_right_c.setIcon(cam_right)
        self.cam_up_c.setIconSize(QSize(120, 120))
        self.cam_down_c.setIconSize(QSize(120, 120))
        self.cam_left_c.setIconSize(QSize(120, 120))
        self.cam_right_c.setIconSize(QSize(120, 120))
        self.cam_up_c.pressed.connect(self.cam_up_pressed)
        self.cam_down_c.pressed.connect(self.cam_down_pressed)
        self.cam_left_c.pressed.connect(self.cam_left_pressed)
        self.cam_right_c.pressed.connect(self.cam_right_pressed)
        self.cam_up_c.released.connect(self.cam_up_released)
        self.cam_down_c.released.connect(self.cam_down_released)
        self.cam_left_c.released.connect(self.cam_left_released)
        self.cam_right_c.released.connect(self.cam_right_released)

        self.return_but_c.setIcon(return_but)
        self.return_but_c.setIconSize(QSize(80, 80))
        self.return_but_c.setCursor(Qt.PointingHandCursor)
        self.return_but_c.setObjectName("return_but")
        self.return_but_c.pressed.connect(return_but_pressed)

        cmb_vbl_c.addWidget(self.dir_combo_c)
        cmb_vbl_c.addWidget(self.depth_combo_c)
        cmb_vbl_c.setSpacing(50)
        cmb_vbl_c.setContentsMargins(0, 0, 0, 20)
        cmb_vbl_c.setAlignment(Qt.AlignHCenter)
        self.dir_combo_c.addItems(["Left", "Right"])
        self.depth_combo_c.addItems(["Depth", "Original"])
        self.bot_box_c.setStyleSheet('''
            QComboBox::down-arrow
                {
                    right:20px;
                    width: 50px;
                    height: 50px;
                    image: url(resource/images/arrow-down.png);
                }
            QComboBox::down-arrow:on
                {
                    width: 50px;
                    height: 50px;
                    image: url(resource/images/arrow-up.png);
                }
        ''')
        self.dir_combo_c.setCursor(Qt.PointingHandCursor)
        self.depth_combo_c.setCursor(Qt.PointingHandCursor)

        self.loading_gif.setSpeed(100)
        self.loading_gif.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    control_center = ControlCenter()
    QSSTool.setQssTool('resource/qss/style.qss', app)
    control_center.show()
    sys.exit(app.exec_())
