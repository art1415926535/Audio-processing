from PyQt5.QtWidgets import QWidget, QFrame, QSizePolicy
from PyQt5.QtGui import QImage, QPainter, QPen, QColor
from PyQt5.QtCore import QByteArray


class Plots(QFrame):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.width_border = 0
        self.background = '#f6f6f6'
        self.setStyleSheet('border: {}px solid color; background-color:{}'.format(self.width_border,
                                                                                  self.background))

        self.__number_of_plots = 0
        self.__plots = []
        self.__percent = 0
        self.__width_of_images = 0

    def add_data(self, data=None, width=100, height=100, number=None):

        z_points = 1000
        z = []

        # n = random.randint(z_points / 5, z_points)
        n = z_points
        for i in range(n):
            # z += [[random.randint(0, 100) / 100 * x for x in range(200)]] * (z_points // n)
            z += [[x for x in range(200)]] * (z_points // n)

        data = z
        q_byte_array = QByteArray()
        print(len(data), len(data[0]))

        from time import time

        t = time()

        if type(data[0]) == list:
            for row in range(len(data[0])):
                for cell in range(len(data)):
                    rgba = self.__rgba(data[cell][row], 200)
                    for c in rgba[::-1]:
                        q_byte_array.append(chr(c))

        print('Create:', time() - t)

        graph = QImage(q_byte_array, len(data), len(data[0]), 6)

        if number is None:
            self.__plots.append(graph)
        else:
            self.__plots.insert(number, graph)

        self.repaint()

    def del_data(self, i):
        self.__plots.pop(i)
        self.repaint()

    def update(self, percent=0, *__args):
        self.percent = percent
        super().update(*__args)

    def paintEvent(self, *__args):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QPen(QColor.blue))
        accumulator_y = 0

        for i in range(len(self.__plots)):
            painter.drawImage(self.width() // 2 - self.__plots[i].width() * self.percent, accumulator_y,
                              self.__plots[i])
            accumulator_y += self.__plots[i].height()

        delta_x = 0
        for aa in range(255, 0, -20):
            painter.setPen(QPen(QColor(255, 200, 200, aa)))
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

    def __rgba(self, x, max_z):
        x = int(x / max_z * 765)
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