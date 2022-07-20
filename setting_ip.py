# Developer : Lucas Liu
# Date: 6/9/2022 Time: 7:41 PM

import sys
from PyQt5.Qt import *
from tool import QSSTool
from ip_port_inputs import IPAndPortInputs


class SettingIp(QWidget):
    save_signal = pyqtSignal(list, name='ipAndPortSaved')
    return_signal = pyqtSignal(name='returnBack')

    def __init__(self, parent=None, data=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        # self.setWindowFlag(Qt.FramelessWindowHint)
        self.ip_port_data = data
        self.resize(1800, 1300)
        self.setObjectName("setting_pane")
        self.menu = QWidget()
        self.top_box_s = QWidget()
        self.bot_box_s = QWidget()
        self.set_box = QWidget()
        self.error_box = QWidget()
        self.error_label = QLabel("* Please fill all the required fields!")
        self.menu_but = QToolButton(self.menu)
        self.logo_label_s = QLabel(self.top_box_s)
        self.logo_word_s = QLabel(self.top_box_s)
        self.connect_gif = QMovie("resource/images/giphy.gif")
        self.connect_label = QLabel()
        self.connect_button = QPushButton()
        self.flag = False
        self.connect_sign = QPushButton("CONNECT")
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
        self.arm_ip_label = QLabel("IP :")
        self.arm_port_label = QLabel("PORT :")
        self.arm_ip_text = QLineEdit()
        self.arm_port_text = QLineEdit()
        self.car_ip_label = QLabel("IP :")
        self.car_port_label = QLabel("PORT :")
        self.car_ip_text = QLineEdit()
        self.car_port_text = QLineEdit()
        self.cam_ip_label = QLabel("IP :")
        self.cam_port_label = QLabel("PORT :")
        self.cam_ip_text = QLineEdit()
        self.cam_port_text = QLineEdit()
        self.arm_pic_label = QLabel()
        self.car_pic_label = QLabel()
        self.cam_pic_label = QLabel()
        self.return_button = QToolButton()
        self.save_button = QToolButton()
        self.edit_button = QToolButton()
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
        self.logo_label_s.move(int(self.width() / 2) - 370, int(self.height() / 3) - 330)
        self.logo_word_s.move(int(self.width() / 2) - 150, int(self.height() / 3) - 250)
        self.return_button.move(self.menu.x() + self.width() - 270, self.menu.y() + 30)
        self.save_button.move(self.menu.x() + self.width() - 170, self.menu.y() + 30)
        self.edit_button.move(self.menu.x() + self.width() - 370, self.menu.y() + 30)

        if len(self.error_label.text()) == 34:
            self.error_label.move(int(self.width() / 2) - 360, 4)
        elif len(self.error_label.text()) == 45:
            self.error_label.move(int(self.width() / 2) - 430, 4)

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

    def connect_but_pressed(self):
        if not self.flag:
            self.connect_gif.setPaused(True)
            self.flag = True
        else:
            self.connect_gif.setPaused(False)
            self.flag = False

    def show_display_animation(self):
        animation = QPropertyAnimation(self)
        animation.setTargetObject(self.logo_label_s)
        animation.setPropertyName(b"pos")
        animation.setKeyValueAt(0, self.logo_label_s.pos() + QPoint(80, 0))
        animation.setKeyValueAt(1, self.logo_label_s.pos())
        animation.setLoopCount(1)
        animation.setDuration(500)
        animation.setEasingCurve(QEasingCurve.InCirc)
        animation.start()
        animation.finished.connect(self.show_logo_animation)

    def show_logo_animation(self):
        self.logo_word_s.show()
        animation_w = QPropertyAnimation(self)
        animation_w.setTargetObject(self.logo_word_s)
        animation_w.setPropertyName(b"windowOpacity")
        animation_w.setKeyValueAt(0, 0)
        animation_w.setKeyValueAt(1, 1)
        animation_w.setLoopCount(1)
        animation_w.setDuration(500)
        animation_w.start()

    def show_error_animation(self):
        animation = QPropertyAnimation(self)
        animation.setTargetObject(self.error_label)
        animation.setPropertyName(b"pos")
        animation.setKeyValueAt(0, self.error_label.pos() + QPoint(10, 0))
        animation.setKeyValueAt(0.2, self.error_label.pos())
        animation.setKeyValueAt(0.5, self.error_label.pos() + QPoint(10, 0))
        animation.setKeyValueAt(0.7, self.error_label.pos())
        animation.setLoopCount(3)
        animation.setDuration(200)
        animation.setEasingCurve(QEasingCurve.InBack)
        animation.start()

    def exit_button_pressed(self):
        self.close()

    def show_full_screen(self):
        self.showFullScreen()
        self.maximize_button.setIcon(self.normalize_icon)
        self.show_display_animation()

    def show_normal_screen(self):
        self.showNormal()
        self.maximize_button.setIcon(self.maximize_icon)
        self.show_display_animation()

    def maximize_button_pressed(self):
        if self.isFullScreen():
            self.showNormal()
            self.maximize_button.setIcon(self.maximize_icon)
        else:
            self.showFullScreen()
            self.maximize_button.setIcon(self.normalize_icon)

    def minimize_button_pressed(self):
        self.showMinimized()

    def showEvent(self, evt):
        self.load_ip_port()

    def update_ip_port(self, data):
        self.ip_port_data = data

    def load_ip_port(self):

        if len(self.ip_port_data) != 0:
            for item in self.ip_port_data:
                if item.get_obj_name() == 'arm':
                    self.arm_ip_text.setText(item.get_ip())
                    self.arm_port_text.setText(item.get_port())
                if item.get_obj_name() == 'rover':
                    self.car_ip_text.setText(item.get_ip())
                    self.car_port_text.setText(item.get_port())
                if item.get_obj_name() == 'camera':
                    self.cam_ip_text.setText(item.get_ip())
                    self.cam_port_text.setText(item.get_port())

            self.edit_button.show()
            self.arm_ip_text.setEnabled(False)
            self.arm_port_text.setEnabled(False)
            self.car_ip_text.setEnabled(False)
            self.car_port_text.setEnabled(False)
            self.cam_ip_text.setEnabled(False)
            self.cam_port_text.setEnabled(False)
        else:
            self.edit_button.hide()

    def edit_button_pressed(self):
        self.arm_ip_text.setEnabled(True)
        self.car_ip_text.setEnabled(True)
        self.cam_ip_text.setEnabled(True)
        self.arm_port_text.setEnabled(True)
        self.car_port_text.setEnabled(True)
        self.cam_port_text.setEnabled(True)

    def save_button_pressed(self):
        flag = False
        ip_port_list = []
        if not len(self.arm_ip_text.text()) == 0 and not len(self.arm_port_text.text()) == 0:
            arm_ip_port = IPAndPortInputs(1, 'arm', self.arm_ip_text.text(), self.arm_port_text.text())
            ip_port_list.append(arm_ip_port)
        elif not (len(self.arm_ip_text.text()) == 0) and len(self.arm_port_text.text()) == 0 or \
                len(self.arm_ip_text.text()) == 0 and (not len(self.arm_port_text.text())) == 0:
            flag = True

        if not len(self.car_ip_text.text()) == 0 and not len(self.car_port_text.text()) == 0:
            car_ip_port = IPAndPortInputs(2, 'rover', self.car_ip_text.text(), self.car_port_text.text())
            ip_port_list.append(car_ip_port)
        elif (not len(self.car_ip_text.text()) == 0 and len(self.car_port_text.text()) == 0) or \
                (len(self.car_ip_text.text()) == 0 and not len(self.car_port_text.text()) == 0):
            flag = True

        if not len(self.cam_ip_text.text()) == 0 and not len(self.cam_port_text.text()) == 0:
            cam_ip_port = IPAndPortInputs(3, 'camera', self.cam_ip_text.text(), self.cam_port_text.text())
            ip_port_list.append(cam_ip_port)
        elif (not len(self.cam_ip_text.text()) == 0 and len(self.cam_port_text.text()) == 0) or \
                (len(self.cam_ip_text.text()) == 0 and not len(self.cam_port_text.text()) == 0):
            flag = True

        if len(ip_port_list) == 0:
            if flag:
                self.error_label.setText("* Please fill the other field of this record!")
                print(len(self.error_label.text()))
                self.error_label.show()
                self.error_label.move(int(self.width() / 2) - 430, 4)
            else:
                self.error_label.setText("* Please fill at least one record!")
                print(len(self.error_label.text()))
                self.error_label.show()
                self.error_label.move(int(self.width() / 2) - 360, 4)
            self.error_label.adjustSize()
            self.show_error_animation()
        else:
            self.error_label.hide()
            self.save_signal.emit(ip_port_list)
            self.arm_ip_text.clearFocus()
            self.car_ip_text.clearFocus()
            self.cam_ip_text.clearFocus()
            self.arm_port_text.clearFocus()
            self.car_port_text.clearFocus()
            self.cam_port_text.clearFocus()
            self.arm_ip_text.clear()
            self.car_ip_text.clear()
            self.cam_ip_text.clear()
            self.arm_port_text.clear()
            self.car_port_text.clear()
            self.cam_port_text.clear()

    def menu_button_pressed(self):
        self.logo_word_s.hide()
        self.show_display_animation()

    def return_button_pressed(self):
        self.error_label.move(int(self.width() / 2) - 360, 4)
        self.logo_word_s.hide()
        self.error_label.hide()
        self.arm_ip_text.clear()
        self.car_ip_text.clear()
        self.cam_ip_text.clear()
        self.arm_port_text.clear()
        self.car_port_text.clear()
        self.cam_port_text.clear()
        self.return_signal.emit()

    def setup_ui(self):
        self.menu.setMinimumWidth(10)
        self.menu.setMaximumWidth(70)
        self.menu.setMinimumHeight(800)
        self.menu.setObjectName("menu_bar")
        self.menu.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.set_box.setObjectName("set_box")
        h_bl = QHBoxLayout(self)
        h_bl.addWidget(self.menu)
        h_bl.addWidget(self.set_box)
        v_bl = QVBoxLayout()
        sv_bl = QVBoxLayout()
        sh_bl = QHBoxLayout()
        l_fl = QFormLayout()
        r_fl = QFormLayout()
        pv_bl = QVBoxLayout()

        self.set_box.setLayout(sv_bl)
        h_bl.setSpacing(0)
        h_bl.setContentsMargins(0, 0, 0, 0)
        v_bl.setStretch(0, 1)
        v_bl.setStretch(1, 2)
        v_bl.setSpacing(0)
        v_bl.setContentsMargins(0, 0, 0, 0)
        sv_bl.setSpacing(0)
        sv_bl.setContentsMargins(0, 0, 0, 0)
        sv_bl.addWidget(self.top_box_s)
        sv_bl.addSpacing(30)
        sv_bl.addWidget(self.error_box)
        sv_bl.addWidget(self.bot_box_s)
        sv_bl.setStretch(0, 1)
        sv_bl.setStretch(0, 1)
        sv_bl.setStretch(2, 1)
        sv_bl.setStretch(3, 3)
        self.bot_box_s.setLayout(sh_bl)
        sh_bl.addLayout(pv_bl)
        sh_bl.addLayout(l_fl)
        sh_bl.addLayout(r_fl)
        sh_bl.setSpacing(0)
        sh_bl.setContentsMargins(0, 0, 0, 0)
        pv_bl.setSpacing(0)
        pv_bl.setContentsMargins(70, 0, 0, 0)
        pv_bl.addStretch(1)
        pv_bl.addWidget(self.arm_pic_label)
        pv_bl.addSpacing(190)
        pv_bl.addWidget(self.car_pic_label)
        pv_bl.addSpacing(190)
        pv_bl.addWidget(self.cam_pic_label)
        pv_bl.addStretch(1)

        l_fl.addRow(self.arm_ip_label, self.arm_ip_text)
        l_fl.addRow(self.car_ip_label, self.car_ip_text)
        l_fl.addRow(self.cam_ip_label, self.cam_ip_text)
        l_fl.setVerticalSpacing(200)
        l_fl.setHorizontalSpacing(50)
        l_fl.setContentsMargins(100, -20, 100, 0)
        l_fl.setFormAlignment(Qt.AlignVCenter)
        l_fl.setLabelAlignment(Qt.AlignRight)
        r_fl.addRow(self.arm_port_label, self.arm_port_text)
        r_fl.addRow(self.car_port_label, self.car_port_text)
        r_fl.addRow(self.cam_port_label, self.cam_port_text)
        r_fl.setVerticalSpacing(200)
        r_fl.setHorizontalSpacing(50)
        r_fl.setContentsMargins(100, -20, 200, 0)
        r_fl.setFormAlignment(Qt.AlignVCenter)
        l_fl.setLabelAlignment(Qt.AlignRight)

        setting_icon = QIcon("resource/images/setting_logo.png")
        self.menu_but.resize(60, 60)
        self.menu_but.setIcon(setting_icon)
        self.menu_but.setIconSize(QSize(50, 50))
        self.menu_but.move(5, self.menu.height() - 20)
        self.menu_but.setCursor(Qt.PointingHandCursor)
        self.menu_but.setObjectName("menu_button")
        self.menu_but.pressed.connect(self.menu_button_pressed)

        self.connect_label.setMaximumSize(800, 450)
        self.connect_label.setMovie(self.connect_gif)
        self.connect_gif.setSpeed(200)
        self.connect_gif.start()

        self.connect_button.setParent(self.connect_label)
        self.connect_button.resize(int(self.connect_label.width()), int(self.connect_label.height()))
        self.connect_button.setStyleSheet("background: transparent;")
        self.connect_button.setCursor(Qt.PointingHandCursor)
        self.connect_button.pressed.connect(self.connect_but_pressed)

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

        self.logo_label_s.setMaximumSize(160, 160)
        self.logo_label_s.setScaledContents(True)
        logo_icon_s = QPixmap("resource/images/logo_5.png")
        self.logo_label_s.setPixmap(logo_icon_s)

        self.logo_word_s.setMaximumSize(360, 60)
        self.logo_word_s.setScaledContents(True)
        logo_word_s = QPixmap("resource/images/logo_word.png")
        self.logo_word_s.setPixmap(logo_word_s)
        self.logo_word_s.hide()

        self.error_label.setParent(self.error_box)
        self.error_box.setMaximumHeight(50)
        self.error_label.setMaximumHeight(50)
        self.error_label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)
        self.error_label.move(int(self.width() / 2) - 360, 0)
        self.error_label.setObjectName("error_label")
        self.error_label.hide()

        return_logo = QIcon("resource/images/back.png")
        self.return_button.setParent(self.top_box_s)
        self.return_button.resize(60, 60)
        self.return_button.setIcon(return_logo)
        self.return_button.setIconSize(QSize(50, 50))
        self.return_button.move(self.x() + self.width() - 300, self.x() + 20)
        self.return_button.setCursor(Qt.PointingHandCursor)
        self.return_button.setObjectName("return_button")
        self.return_button.pressed.connect(self.return_button_pressed)

        save_logo = QIcon("resource/images/checked.png")
        self.save_button.setParent(self.top_box_s)
        self.save_button.setIcon(save_logo)
        self.save_button.resize(60, 60)
        self.save_button.setIconSize(QSize(50, 50))
        self.save_button.move(self.x() + self.width() - 200, self.x() + 20)
        self.save_button.setCursor(Qt.PointingHandCursor)
        self.save_button.setObjectName("save_button")
        self.save_button.pressed.connect(self.save_button_pressed)

        edit_logo = QIcon("resource/images/write.png")
        self.edit_button.setParent(self.top_box_s)
        self.edit_button.setIcon(edit_logo)
        self.edit_button.resize(60, 60)
        self.edit_button.setIconSize(QSize(55, 45))
        self.edit_button.move(self.x() + self.width() - 400, self.x() + 20)
        self.edit_button.setCursor(Qt.PointingHandCursor)
        self.edit_button.setObjectName("edit_button")
        self.edit_button.pressed.connect(self.edit_button_pressed)

        arm_pic = QPixmap("resource/images/robot-arm.png")
        car_pic = QPixmap("resource/images/robot-rover.png")
        cam_pic = QPixmap("resource/images/robot-cam.png")
        self.arm_pic_label.setPixmap(arm_pic)
        self.car_pic_label.setPixmap(car_pic)
        self.cam_pic_label.setPixmap(cam_pic)
        self.arm_pic_label.setMaximumSize(80, 80)
        self.arm_pic_label.setScaledContents(True)
        self.car_pic_label.setMaximumSize(80, 80)
        self.car_pic_label.setScaledContents(True)
        self.cam_pic_label.setMaximumSize(80, 80)
        self.cam_pic_label.setScaledContents(True)
        self.arm_pic_label.setAlignment(Qt.AlignCenter)
        self.car_pic_label.setAlignment(Qt.AlignCenter)
        self.cam_pic_label.setAlignment(Qt.AlignCenter)

        self.arm_ip_text.setMaxLength(15)
        self.car_ip_text.setMaxLength(15)
        self.cam_ip_text.setMaxLength(15)
        self.arm_port_text.setMaxLength(5)
        self.car_port_text.setMaxLength(5)
        self.cam_port_text.setMaxLength(5)
        self.arm_ip_text.setPlaceholderText("127.0.0.1")
        self.arm_port_text.setPlaceholderText("3306")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    setting = SettingIp()
    setting.show()
    QSSTool.setQssTool('resource/qss/style.qss', app)
    sys.exit(app.exec_())
