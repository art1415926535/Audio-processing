import logging
import threading

from PyQt5 import QtGui, QtCore, uic, QtWidgets
import PyQt5.QtCore as C
import PyQt5.QtMultimedia as M

import QPlots
from syntax_pars import PythonHighlighter as Parser
import QCodeEdit
import icons


class Window(QtWidgets.QWidget):
    def __init__(self, app, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        uic.loadUi('gui_beat.ui', self)
        self.scene = QtWidgets.QGraphicsScene()
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.app = app

        # <player
        self.qt_player = M.QMediaPlayer()
        self.qt_player.setNotifyInterval(100)

        self.play = False
        self.track = 'music/The Game.mp3'

        self.qt_player.positionChanged.connect(self.pos_changed)

        self.track_slider.valueChanged.connect(self.rewind_mouse)
        # />

        # <plots
        self.plots = []
        # />

        self.play_pause_button.clicked.connect(self.play_pause)
        self.open_file_button.clicked.connect(self.load)

        self.code_edit = QCodeEdit.QCodeEdit()

        self.layout_for_QCodeEdit.addWidget(self.code_edit)
        self.highlights = Parser(self.code_edit.document())

        self.perform_algorithm_button.clicked.connect(self.perform_algorithm)
        self.new_code_button.clicked.connect(self.new_file)
        self.save_code_button.clicked.connect(self.save_file)
        self.open_code_button.clicked.connect(self.open_file)
        self.del_code_button.clicked.connect(self.close_file)

        self.choice_algorithm_box.currentTextChanged.connect(self.number_of_current_code_changed)

        # self.exit_button.clicked.connect(self.close)
        #
        # self.fullscreen_button.clicked.connect(self.fullscreen)
        # self.windowed = True

    def perform_code(self):
        code = self.code_edit.toPlainText()
        plot = self.plots[self.code_edit.now_file]

        try:
            exec(code)
        except Exception:
            error = list(sys.exc_info())
            class_error = str(error[0])
            info = str(error[1]) + '\n' + str(error[2])

            message_box = QtWidgets.QMessageBox()
            message_box.setWindowTitle(class_error)
            message_box.setText('\n' + info + '\n')
            message_box.addButton('  FF  ', QtWidgets.QMessageBox.YesRole)
            message_box.exec_()

    def perform_algorithm(self):
        self.__thread = threading.Thread(target=self.perform_code)
        self.__thread.start()


    def add_plot(self, name):
        self.choice_algorithm_box.addItem(name)
        self.choice_algorithm_box.setCurrentIndex(self.choice_algorithm_box.count() - 1)

        message_box = QtWidgets.QMessageBox()
        message_box.setText('\n' + '2D?' + '\n')
        message_box.addButton('2d', QtWidgets.QMessageBox.YesRole)
        message_box.addButton('3d', QtWidgets.QMessageBox.NoRole)
        if message_box.exec_() == 1:
            self.plots.append(QPlots.Plot3d())
        else:
            self.plots.append(QPlots.Plot2d(name=name))

        self.plots_layout.addWidget(self.plots[-1])
        self.plots[-1].set_data()

    def number_of_current_code_changed(self, s):
        if self.plots:
            print(s)
            self.code_edit.load_file(s)

    def new_file(self):
        name = self.code_edit.new_file()
        self.add_plot(name)

    def open_file(self):
        name = self.code_edit.open_file()
        if name is not None:
            self.add_plot(name)

    def save_file(self):
        self.code_edit.save_file()

    def close_file(self):
        if self.plots:
            save_text = "Save the algorithm?"
            reply = QtWidgets.QMessageBox.question(self, 'Save',
                                                   save_text,
                                                   QtWidgets.QMessageBox.Yes,
                                                   QtWidgets.QMessageBox.No)

            if reply == QtWidgets.QMessageBox.Yes:
                self.save_file()

            number = self.code_edit.close_file()
            self.plots_layout.takeAt(number).widget().deleteLater()
            self.plots.pop(number)

            self.choice_algorithm_box.removeItem(number)

    # def fullscreen(self, full=False):
    #     if self.windowed or full:
    #         self.showMaximized()
    #         self.fullscreen_button.setIcon(QtGui.QIcon(
    #             ':/fullscreen_exit_black/ic_fullscreen_exit_black_48dp.png'))
    #         self.windowed = False
    #     else:
    #         self.showNormal()
    #         self.fullscreen_button.setIcon(QtGui.QIcon(
    #             ':/fullscreen_black/ic_fullscreen_black_48dp.png'))
    #
    #         self.windowed = True
    #
    # def mousePressEvent(self, event):
    #     self.offset = event.pos()
    #
    # def mouseMoveEvent(self, event):
    #     if event.globalY() < 20:
    #         self.fullscreen(full=True)
    #     if self.title_window_label.underMouse() and event.globalY() > 20:
    #         x = event.globalX()
    #         y = event.globalY()
    #         x_w = self.offset.x()
    #         y_w = self.offset.y()
    #         self.move(x - x_w, y - y_w)
    #
    #         if self.offset.y() < 20:
    #             self.fullscreen_button.setIcon(QtGui.QIcon(
    #                 ':/fullscreen_black/ic_fullscreen_black_48dp.png'))
    #             self.windowed = True

    # sssssssssssssssssssssssssssssssssPLAYERssssssssssssssssssssssssssssssssssssss

    def pos_changed(self):
        self.rewind(self.qt_player.position())
        for plot in self.plots:
            plot.update(self.qt_player.position() / self.qt_player.duration())

    def rewind(self, x):
        if not self.track_slider.isSliderDown():
            self.time_of_track_label.setText(str(x // 1000))  # millisec > sec
            self.track_slider.setValue(x / self.qt_player.duration() * self.track_slider.maximum())

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

        path, extension = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')
        if not path:
            logging.warning('НЕ УКАЗАН ПУТЬ К ФАЙЛУ')
        else:
            self.track = path

        for plot in self.plots:
            plot.update()

        print('play', self.track)
        url = C.QUrl.fromLocalFile(self.track)
        print(url)
        content = M.QMediaContent(url)
        print(content.canonicalUrl())

        if self.play:
            self.qt_player.pause()
            self.play_pause_button.setIcon(QtGui.QIcon(
                ':/color/ic_play_circle_fill_color_48dp.png'))
            self.play = False

        self.qt_player.setMedia(content)
        print(self.qt_player.mediaStatus())

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


        # try:
        # exec(s)
        #
        # with open('algorithms/{}.py'.format(str(i)), 'w') as f:
        #         f.write(self.editors[i].toPlainText())
        # except:
        #     error = list(sys.exc_info())
        #     class_error = str(error[0])
        #     info = str(error[1]) + '\n' + str(error[2])
        #
        #     message_box = QtWidgets.QMessageBox()
        #     message_box.setWindowTitle(class_error)
        #     message_box.setText('\n' + info + '\n')
        #     message_box.addButton('  Fuuuuuuuuuck  ', QtWidgets.QMessageBox.YesRole)
        #     message_box.exec_()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Window(app)
    window.show()
    app.exec()