from time import time

from PyQt5.QtWidgets import QWidget, QFrame, QSizePolicy
from PyQt5.QtGui import QImage, QPainter, QPen, QColor
from PyQt5.QtCore import QByteArray, Qt


def test_spectrum(function):
    def decorated(self, *args, **kwargs):
        count_numbers = 10000
        max_number = 10
        data = []
        import random

        for i in range(count_numbers):
            data += [[x * random.normalvariate(0.9, 0.1) for x in range(max_number)]] * (count_numbers // count_numbers)

        t = time()
        function(self, data, max_number)
        print('>>> Время выполнения функции: {}\n>>> Количество значений: {}'.format(
            time() - t,
            count_numbers * max_number)
        )

    return decorated


class Plots(QFrame):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.setMinimumHeight(42)
        self.setMaximumHeight(9000)

        self.width_border = 0
        self.background = '#f6f6f6'
        self.setStyleSheet('border: {}px solid color; background-color:{}'.format(self.width_border,
                                                                                  self.background))

        self.__plot = QImage()
        self.src = QImage()
        self.__percent = 0
        self.q_byte_array = QByteArray()

    @test_spectrum
    def add_data(self, data=None, max_number=50, height=100):
        if type(data[0]) == list:
            for row in range(len(data[0])):
                for cell in range(len(data)):
                    rgba = self.__rgba(data[cell][row], max_number)
                    for c in rgba[::-1]:
                        self.q_byte_array.append(chr(c))
        else:
            assert AttributeError

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

    def __rgba(self, x, max_x):
        x = int(x / max_x * 765)
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

    def wheelEvent(self, event):
        print(event.angleDelta())
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

        elif mouse_event.button() == Qt.LeftButton and self.height() < 500:
            self.setMinimumHeight(self.height() + 100)
            self.setMaximumHeight(self.height() + 100)

        elif mouse_event.button() == Qt.RightButton and self.height() > 142:
            self.setMinimumHeight(self.height() - 100)
            self.setMaximumHeight(self.height() - 100)



