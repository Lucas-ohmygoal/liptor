# Developer : Lucas Liu
# Date: 2022/6/4 Time: 21:10

import sys
from PyQt5.Qt import *
from tool import QSSTool
from error_display import Error


class Connector(QWidget):

    connect_signal = pyqtSignal(name='connectWithRobot')
    setting_signal = pyqtSignal(name='ipAndPortSetting')

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        # self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowIcon(QIcon("resource/images/logo_5.png"))
        self.setWindowTitle("LIPTOR")
        self.resize(1800, 1300)
        self.setObjectName("connector_pane")
        self.menu = QWidget()
        self.top_box = QWidget()
        self.bot_box = QWidget()

        self.int_box = QWidget()

        self.menu_but = QToolButton(self.menu)
        self.logo_label = QLabel(self.top_box)

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
        self.err = Error(self.top_box, "Welcome to use Liptor :)")
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
        self.connect_label.move(int(self.int_box.width()/2) - 255, 0)
        self.connect_sign.move(int(self.int_box.width()/2) - 250, int(self.connect_label.height()))
        self.exit_button.move(5, self.menu.y() + 20)
        self.maximize_button.move(5, self.menu.y() + 100)
        self.maximize_button.move(5, self.menu.y() + 100)
        self.minimize_button.move(5, self.menu.y() + 180)
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

    def show_connection_animation(self):
        animation = QPropertyAnimation(self)
        animation.setTargetObject(self.connect_label)
        animation.setPropertyName(b"pos")
        animation.setKeyValueAt(0, self.connect_label.pos() + QPoint(20, 5))
        animation.setKeyValueAt(0.2, self.connect_label.pos() + QPoint(0, 10))
        animation.setKeyValueAt(0.4, self.connect_label.pos() + QPoint(-20, -5))
        animation.setKeyValueAt(0.6, self.connect_label.pos())
        animation.setLoopCount(15)
        animation.setDuration(300)
        # animation.setEasingCurve(QEasingCurve.OutQuint)
        animation.start()

        animation.finished.connect(lambda: self.connect_signal.emit())

    def connect_with_robots(self):
        self.show_connection_animation()

    def exit_button_pressed(self):
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

    def setup_ui(self):

        def menu_button_pressed():
            self.setting_signal.emit()

        self.menu.setMinimumWidth(10)
        self.menu.setMaximumWidth(70)
        self.menu.setMinimumHeight(800)
        self.menu.setObjectName("menu_bar")
        self.menu.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.top_box.setObjectName("top_box")
        self.bot_box.setObjectName("bot_box")
        self.int_box.setObjectName("int_box")

        h_bl = QHBoxLayout(self)
        h_bl.addWidget(self.menu)
        h_bl.addWidget(self.int_box)
        v_bl = QVBoxLayout()

        self.int_box.setLayout(v_bl)
        h_bl.setSpacing(0)
        h_bl.setContentsMargins(0, 0, 0, 0)
        v_bl.addWidget(self.top_box)
        v_bl.addWidget(self.bot_box)
        v_bl.setStretch(0, 1)
        v_bl.setStretch(1, 2)
        v_bl.setSpacing(0)
        v_bl.setContentsMargins(0, 0, 0, 0)

        setting_icon = QIcon("resource/images/setting_logo.png")
        self.menu_but.resize(60, 60)
        self.menu_but.setIcon(setting_icon)
        self.menu_but.setIconSize(QSize(50, 50))
        self.menu_but.move(5, self.menu.height() - 20)
        self.menu_but.setCursor(Qt.PointingHandCursor)
        self.menu_but.setObjectName("menu_button")
        self.menu_but.pressed.connect(menu_button_pressed)

        self.logo_label.setMaximumSize(440, 150)
        self.logo_label.setScaledContents(True)
        self.logo_label.move(30, 30)
        logo_pic = QPixmap("resource/images/logo_6.png")
        self.logo_label.setPixmap(logo_pic)

        self.connect_label.setParent(self.bot_box)
        self.connect_label.setMaximumSize(800, 450)
        self.connect_label.setMovie(self.connect_gif)
        self.connect_gif.setSpeed(200)
        self.connect_gif.start()

        self.connect_button.setParent(self.connect_label)
        self.connect_button.resize(int(self.connect_label.width()), int(self.connect_label.height()))
        self.connect_button.setStyleSheet("background: transparent;")
        self.connect_button.setCursor(Qt.PointingHandCursor)
        self.connect_button.pressed.connect(self.connect_but_pressed)

        self.connect_sign.setParent(self.bot_box)
        self.connect_sign.resize(470, 100)
        self.connect_sign.setObjectName("connect_sign")
        self.connect_sign.setCursor(Qt.PointingHandCursor)
        self.connect_sign.pressed.connect(self.connect_with_robots)

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

    def show_error(self, error_code, error_msg):
        self.err.error_code = error_code
        self.err.error_msg = error_msg
        self.err.setVisible(True)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    connector = Connector()
    connector.show()
    QSSTool.setQssTool('resource/qss/style.qss', app)
    sys.exit(app.exec_())
