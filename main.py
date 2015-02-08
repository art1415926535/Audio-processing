import logging

from PyQt5 import QtGui, QtCore, uic, QtWidgets
import PyQt5.QtCore as C
import PyQt5.QtMultimedia as M

from syntax_pars import PythonHighlighter as Parser


class Window(QtWidgets.QWidget):
    def __init__(self, app, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        uic.loadUi('gui_beat.ui', self)
        self.scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.app = app

        # <player
        self.qt_player = M.QMediaPlayer()
        self.qt_player.setNotifyInterval(100)

        self.play = False
        self.track = 'music/The Game.mp3'

        self.qt_player.positionChanged.connect(self.rewind)

        self.track_slider.valueChanged.connect(self.rewind_mouse)
        # />

        self.play_pause_button.clicked.connect(self.play_pause)
        self.open_file_button.clicked.connect(self.load)

        # <editors

        self.editors = [self.text_program_0, self.text_program_1, self.text_program_2]
        self.highlights = []
        for i in range(3):
            self.highlights.append(Parser(self.editors[i].document()))

            with open('algorithms/{}.py'.format(str(i)), 'r') as f:
                self.editors[i].setPlainText(f.read())

        self.editors[0].textChanged.connect(
            lambda: self.update_graphics(self.editors[0].toPlainText(), 0))
        self.editors[1].textChanged.connect(
            lambda: self.update_graphics(self.editors[1].toPlainText(), 1))
        self.editors[2].textChanged.connect(
            lambda: self.update_graphics(self.editors[2].toPlainText(), 2))

        # self.graphicsView.resizeEvent.connect(self.test)

        self.labels = []
        self.add_label_button.clicked.connect(self.add_label)
        self.del_label_button.clicked.connect(self.del_label)

        self.exit_button.clicked.connect(self.close)

        self.fullscreen_button.clicked.connect(self.fullscreen)
        self.windowed = True

    def add_label(self):
        self.labels.append(QtWidgets.QLabel('Label ' + str(len(self.labels))))
        self.labels_layout.addWidget(self.labels[-1])
        # self.labels[-1].clicked.connect(self.del_label)

    def del_label(self):
        if self.labels:
            self.labels_layout.removeWidget(self.labels.pop())

    def fullscreen(self, full=False):
        if self.windowed or full:
            self.showFullScreen()
            self.fullscreen_button.setIcon(QtGui.QIcon(
                ':/fullscreen_exit_black/ic_fullscreen_exit_black_48dp.png'))
            self.windowed = False
        else:
            self.showNormal()
            self.fullscreen_button.setIcon(QtGui.QIcon(
                ':/fullscreen_black/ic_fullscreen_black_48dp.png'))

            self.windowed = True

    def mousePressEvent(self, event):
        self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if event.globalY() < 20:
            self.fullscreen(full=True)
        if self.title_window_label.underMouse() and event.globalY() > 20:
            x = event.globalX()
            y = event.globalY()
            x_w = self.offset.x()
            y_w = self.offset.y()
            self.move(x - x_w, y - y_w)

            if self.offset.y() < 20:
                self.fullscreen_button.setIcon(QtGui.QIcon(
                    ':/fullscreen_black/ic_fullscreen_black_48dp.png'))
                self.windowed = True

    # sssssssssssssssssssssssssssssssssPLAYERssssssssssssssssssssssssssssssssssssss
    def rewind(self, x):
        # print(self.track_slider.value() / self.track_slider.maximum() * self.qt_player.duration() - 1000,
        # x,
        #       self.track_slider.value() / self.track_slider.maximum() * self.qt_player.duration() + 1000,
        #       self.track_slider.value() / self.track_slider.maximum() * self.qt_player.duration() - 1000 <
        #       x
        #       < self.track_slider.value() / self.track_slider.maximum() * self.qt_player.duration() + 1000)
        if not self.track_slider.isSliderDown():
            self.time_of_track_label.setText(str(x // 1000))  # millisec > sec
            self.track_slider.setValue(x / self.qt_player.duration() * self.track_slider.maximum())

        self.move_line(self.track_slider.value())

    def rewind_mouse(self, x):
        maximum = self.track_slider.maximum()
        duration = self.qt_player.duration()
        d_pos = x / maximum * duration

        if not (d_pos - maximum / 20) < self.qt_player.position() < (d_pos + maximum / 20):
            self.qt_player.setPosition(d_pos)
            print(d_pos, self.qt_player.position())
            print(self.play)


    def load(self, path):
        self.play_pause_button.setEnabled(True)
        if not path:
            logging.warning('НЕ УКАЗАН ПУТЬ К ФАЙЛУ')
        else:
            self.track = path

        self.title_window_label.setText(self.track)

        print('play', self.track)
        url = C.QUrl.fromLocalFile(self.track)
        content = M.QMediaContent(url)
        self.qt_player.setMedia(content)

        if self.play:
            self.qt_player.pause()
            self.play_pause_button.setIcon(QtGui.QIcon(
                ':/color/ic_play_circle_fill_color_48dp.png'))
            self.play = False

    def play_pause(self):
        print("PLAY PAUSE")
        if self.play:
            self.qt_player.pause()
            self.play_pause_button.setIcon(QtGui.QIcon(
                ':/color/ic_play_circle_fill_color_48dp.png'))
        else:
            self.qt_player.play()
            self.play_pause_button.setIcon(QtGui.QIcon(
                ':/color/ic_pause_circle_fill_color_48dp.png'))

        self.play = not self.play

        # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxPLAYERxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

    def update_graphics(self, s, i):
        check = s.replace('\n', '')
        phrase = 'ok!'
        if len(check) > len(phrase) and check[-len(phrase):] in phrase:
            s = s[::-1].replace(phrase[::-1], '', 1)[::-1]  # del phrase from end
            try:
                exec(s)

                with open('algorithms/{}.py'.format(str(i)), 'w') as f:
                    f.write(self.editors[i].toPlainText())
            except:
                error = list(sys.exc_info())
                class_error = str(error[0])
                info = str(error[1]) + '\n' + str(error[2])

                message_box = QtWidgets.QMessageBox()
                message_box.setWindowTitle(class_error)
                message_box.setText('\n' + info + '\n')
                message_box.addButton('  Fuuuuuuuuuck  ', QtWidgets.QMessageBox.YesRole)
                message_box.exec_()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Window(app)
    window.show()
    window.add_line()
    app.exec()