from PyQt5 import QtGui, QtCore, uic, QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        uic.loadUi('gui_beat.ui', self)
        self.scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.scene)

        self.img = None
        self.load_img()

        self.line = None
        self.add_line()

        self.pos_line_x = 0

        # self.effect = QtWidgets.QGraphicsTransform()
        # self.line.setGraphicsEffect(self.effect)

        self.ag = QtCore.QSequentialAnimationGroup()
        self.delta_time = 100

        self.track_slider.valueChanged.connect(lambda: self.move_line(self.track_slider.value()))

    def load_img(self):
        self.img = self.scene.addPixmap(QtGui.QPixmap('1.jpg'))

    def add_line(self):
        self.line = self.scene.addLine(100, 100, 200, 200)

    def move_line(self, x):
        t = QtGui.QTransform.fromTranslate(x, 20.0)
        self.img.setTransform(t)

        # self.ag.addAnimation(self.anim_move_line(self.pos_line_x, x))
        # self.ag.start()
        # self.pos_line_x = x

    def anim_move_line(self, start, end):
        an = QtCore.QPropertyAnimation(self.effect, "rotation")
        an.setDuration(self.delta_time)
        an.setStartValue(start)
        an.setEndValue(end)
        return an


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.showMaximized()
    app.exec()