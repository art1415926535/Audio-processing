from time import time

from PyQt5.QtWidgets import QWidget, QFrame, QSizePolicy, QApplication
from PyQt5.QtGui import QImage, QPainter, QPen, QColor
from PyQt5.QtCore import QByteArray, Qt

import styleSheets


def test_spectrum(function):
    def decorated(self, *args, **kwargs):
        import random

        count_numbers = 1000  # random.randint(500, 1500)
        max_number = 100
        data = []

        # if random.randint(0, 1):
        # from math import sin
        #     for i in range(count_numbers):
        #         data += [[x * random.normalvariate(0.9, 0.1)*sin(x*random.normalvariate(0.95, 0.05)/10)**2 for x in range(max_number)]]
        # else:
        for i in range(count_numbers):
            data += [[int(x * random.normalvariate(0.9, 0.1)) for x in range(max_number)]]

        t = time()
        function(self, data, max_number)
        print('>>> Время выполнения функции: {}\n>>> Количество значений: {}'.format(
            time() - t,
            count_numbers * max_number)
        )

    return decorated


def rgba(x, max_x):
    x = x * 765 // max_x
    # r  g  b
    color = [1, 1, 1]
    for i in (2, 0, 1):
        if x > 255:
            color[i] = 255
        elif x > 0:
            color[i] = x

        x -= 255

    if color[0] > 1:
        color[2] = 256 - color[0]

    return [255] + color


class Plot(QFrame):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.setMinimumHeight(42)  # MAGIC!
        self.setMaximumHeight(9000)  # OVERMAGIC!

        self.background = '#f6f6f6'
        self.setStyleSheet(styleSheets.qplots(self.background))
        self.q_byte_array = QByteArray()
        self.filling = 0

        self.__plot = QImage()
        self.src = QImage()
        self.__percent = 0

    @test_spectrum
    def add_data(self, data=None, max_number=50, height=100):
        if type(data[0]) == list:
            for row in range(len(data[0])):
                for cell in range(len(data)):
                    rgba_c = rgba(data[cell][row], max_number)
                    for c in rgba_c[::-1]:
                        self.q_byte_array.append(chr(c))
        else:
            assert AttributeError

        self.src = QImage(self.q_byte_array, len(data), len(data[0]), 6)

        self.__plot = self.src
        self.repaint()

    def append_q_bate_array(self, c):
        self.q_byte_array.append(c)

        self.src = QImage(self.q_byte_array, len(data), len(data[0]), 6)
        self.__plot = self.src
        self.repaint()


    def del_data(self):
        self.__plot = QImage()
        self.repaint()

    def update(self, percent=0, *__args):
        self.percent = percent
        super().update(*__args)

    def resizeEvent(self, *args, **kwargs):
        self.__plot = self.src.scaled(self.__plot.width(), self.height())

    def paintEvent(self, *__args):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QPen(QColor.blue))
        accumulator_y = 0

        painter.drawImage(self.width() // 2 - self.__plot.width() * self.percent, accumulator_y,
                          self.__plot)
        accumulator_y += self.__plot.height()

        delta_x = 0
        for aa in range(255, 0, -20):
            painter.setPen(QPen(QColor(0, 0, 0, aa)))
            painter.drawLine(self.width() // 2 - delta_x, 0, self.width() // 2 - delta_x, self.height())
            delta_x += 1

    @property
    def percent(self):
        return self.__percent

    @percent.setter
    def percent(self, p):
        if 0 <= p <= 100:
            self.__percent = p
        else:
            raise IndexError

    def wheelEvent(self, event):
        if 20 < self.minimumHeight() < self.parent().height() - 200 or \
                (event.angleDelta().y() < 0 and self.minimumHeight() >= self.parent().height()):
            self.setMinimumHeight(self.height() + event.angleDelta().y() / 24)
            self.setMaximumHeight(self.height() + event.angleDelta().y() / 24)
        elif self.maximumHeight() > 50 or event.angleDelta().y() > 0:
            self.setMinimumHeight(self.height() + event.angleDelta().y() / 24)
            self.setMaximumHeight(self.height() + event.angleDelta().y() / 24)

    def mouseReleaseEvent(self, mouse_event):
        if mouse_event.button() == Qt.MidButton:
            self.setMinimumHeight(42)
            self.setMaximumHeight(9000)

        elif mouse_event.button() == Qt.LeftButton:
            self.__plot = self.src.scaled(self.__plot.width() + 100, self.__plot.height())

        elif mouse_event.button() == Qt.RightButton and self.__plot.width() > 200:
            self.__plot = self.src.scaled(self.__plot.width() - 100, self.__plot.height())

        self.repaint()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Plot()
    window.show()
    window.add_data('lalka')
    # window.close()
    app.exec()