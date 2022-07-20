# Developer : Lucas Liu
# Date: 7/14/2022 Time: 9:02 PM

from PyQt5.Qt import *
import sys


class Error(QLabel):

    def __init__(self, parent=None, error_code=None, error_msg=None):
        super().__init__(parent)
        self.parent = parent
        self.error_code = error_code
        self.error_msg = error_msg
        self.timer = QTimer(self)
        self.timer.timeout.connect(lambda: self.setVisible(False))
        self.setup_ui()
        self.setVisible(False)

    def showEvent(self, event):
        super().showEvent(event)
        self.setText("{0} - {1}".format(self.error_code, self.error_msg))
        # self.adjustSize()
        self.show_error_animation()
        self.timer.start(3000)

    def show_error_animation(self):
        animation = QPropertyAnimation(self)
        animation.setTargetObject(self)
        animation.setPropertyName(b"pos")
        animation.setKeyValueAt(0, self.pos() + QPoint(0, -40))
        animation.setKeyValueAt(0.2, self.pos() + QPoint(0, -30))
        animation.setKeyValueAt(0.4, self.pos() + QPoint(0, -15))
        animation.setKeyValueAt(0.6, self.pos() + QPoint(0, -5))
        animation.setKeyValueAt(0.8, self.pos())
        animation.setLoopCount(1)
        animation.setDuration(800)
        animation.setEasingCurve(QEasingCurve.OutCirc)
        animation.start()

    def setup_ui(self):
        self.resize(500, 80)
        self.move(int(self.parent.width()), 80)
        self.setObjectName("error_board")
        self.setAlignment(Qt.AlignCenter)

