from PyQt5.QtWidgets import QWidget, QFrame, QSizePolicy
from PyQt5.QtGui import QImage, QPainter, QPen, QColor


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
        '''
        array = data
        # FIXME переделать массив в нормальный 0xAARRGGBB
        graph = QImage(array,
                       width=width,
                       height=height,
                       QImage.Format_ARGB32_Premultiplied)
        '''  # TODO: затычко

        graph = QImage(data)
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
        # painter.drawLine(self.width()*self.percent, self.height()*self.percent,
        # self.width()*(1-self.percent), self.height()*(1-self.percent))
        #
        # painter.drawLine(self.width()*(1-self.percent), self.height()*self.percent,
        #                  self.width()*self.percent, self.height()*(1-self.percent))
        accumulator_y = 0

        for i in range(len(self.__plots)):
            painter.drawImage(self.width() // 2 - self.__plots[i].width() * self.percent, accumulator_y,
                              self.__plots[i])
            accumulator_y += self.__plots[i].height()

        delta_x = 0
        for aa in range(255, 0, -20):
            painter.setPen(QPen(QColor(50, 130, 150, aa)))
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
