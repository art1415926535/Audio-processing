import logging
import os

import PyQt5.QtCore as Core
import PyQt5.QtMultimedia as Multimedia
from PyQt5 import QtWidgets, QtGui


class QPlayer():
    def __init__(self):
        self.qt_player = Multimedia.QMediaPlayer()
        self.qt_player.setNotifyInterval(1)

        self.play = False
        self.track = ''

    def position_changed(self):
        self.rewind(self.qt_player.position())
        for plot in self.plots:
            plot.update(self.qt_player.position() / self.qt_player.duration())

    def rewind(self, x):
        if not self.track_slider.isSliderDown():
            self.time_of_track_label.setText(str(x // 1000))  # milliseconds to seconds
            self.track_slider.setValue(x / self.qt_player.duration() * self.track_slider.maximum())

    def rewind_mouse(self, x):
        maximum = self.track_slider.maximum()
        duration = self.qt_player.duration()
        d_pos = x / maximum * duration

        if not (d_pos - maximum / 20) < self.qt_player.position() < (d_pos + maximum / 20):
            self.qt_player.setPosition(d_pos)
            logging.info(str(d_pos) + str(self.qt_player.position()))

    def load_file(self):
        path, extension = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')
        if not path:
            logging.info('The path is empty. Loading canceled.')
            return

        logging.info('Open ' + path)
        self.track = path
        self.setWindowTitle(os.path.basename(self.track))
        self.play_pause_button.setEnabled(True)
        url = Core.QUrl.fromLocalFile(self.track)
        content = Multimedia.QMediaContent(url)

        if self.play:
            self.play_and_pause()
            self.play_pause_button.setIcon(QtGui.QIcon(':/color/ic_play_circle_fill_color_48dp.png'))
            self.play = False
        self.qt_player.setMedia(content)
        self.rewind(0)

    def play_and_pause(self):
        if self.play:
            logging.info("Pause")
            self.qt_player.pause()
            self.play_pause_button.setIcon(QtGui.QIcon(':/color/ic_play_circle_fill_color_48dp.png'))
        else:
            logging.info("Play")
            self.qt_player.play()
            self.play_pause_button.setIcon(QtGui.QIcon(':/color/ic_pause_circle_fill_color_48dp.png'))

        self.play = not self.play
