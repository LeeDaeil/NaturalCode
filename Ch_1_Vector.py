"""
Title : Bounce Ball

"""
# import Part ----------------------------------------------------------------------------------------------------------
import numpy as np
from random import randint
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
# ----------------------------------------------------------------------------------------------------------------------


class MainWin(QWidget):
    def __init__(self):
        super(MainWin, self).__init__(parent=None)
        self.setGeometry(100, 100, 500, 500)

        self.ball_box_x, self.ball_box_y = 20, 20
        self.ball_box_size = 100
        self.ball_pos_x, self.ball_pos_y = 90, 90       # 20 ~ 90
        self.ball_size = 30
        self.x_speed, self.y_speed = 1, 3.3

        timer = QTimer(self)
        timer.setInterval(30)
        timer.timeout.connect(self.move_ball)
        timer.start()

    def paintEvent(self, QPaintEvent):
        qp = QPainter(self)
        qp.save()

        qp.setPen(Qt.NoPen)
        qp.setBrush(QBrush(Qt.blue))
        qp.drawEllipse(self.ball_pos_x, self.ball_pos_y, self.ball_size, self.ball_size)

        qp.setPen(QPen(Qt.black, 2))
        qp.setBrush(Qt.NoBrush)
        qp.drawRect(self.ball_box_x, self.ball_box_y, self.ball_box_size, self.ball_box_size)

        qp.restore()

    def move_ball(self):
        self.ball_pos_x = self.ball_pos_x + self.x_speed
        self.ball_pos_y = self.ball_pos_y + self.y_speed

        if self.ball_pos_x > self.ball_box_size - 10 or self.ball_pos_x < 20:
            self.x_speed = self.x_speed * -1

        if self.ball_pos_y > self.ball_box_size - 10 or self.ball_pos_y < 20:
            self.y_speed = self.y_speed * -1

        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWin()
    w.show()
    sys.exit(app.exec_())
