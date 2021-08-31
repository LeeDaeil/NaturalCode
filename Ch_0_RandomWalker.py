"""
Title : Random Walker 구현

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

        self.walk_history = [[int(self.width()/2), int(self.height()/2)]]  # (x, y)

        timer = QTimer(self)
        timer.setInterval(30)
        timer.timeout.connect(self.walk)
        timer.start()

    def paintEvent(self, QPaintEvent):
        qp = QPainter(self)
        qp.save()

        qp.setPen(Qt.NoPen)
        qp.setBrush(QBrush(Qt.blue))
        for (x, y) in self.walk_history:
            qp.drawEllipse(x, y, 5, 5)

        qp.restore()

    def walk(self):
        self.update()
        old_x = self.walk_history[-1][0]
        old_y = self.walk_history[-1][1]

        direct = randint(1, 4)
        if direct == 1:
            old_x += 1
        elif direct == 2:
            old_x -= 1
        elif direct == 3:
            old_y += 1
        elif direct == 4:
            old_y -= 1

        self.walk_history.append([old_x, old_y])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWin()
    w.show()
    sys.exit(app.exec_())
