import os
import logging
import threading

from PyQt5 import uic, QtWidgets

from qt_widgets.syntax_pars import PythonHighlighter as Parser
from qt_widgets import q_code_edit, q_plots, q_player
from user_interface import gui


class Window(QtWidgets.QWidget, q_player.QPlayer, gui.UiForm):
    def __init__(self, parent=None):

        QtWidgets.QWidget.__init__(self, parent)
        gui.UiForm.__init__(self, self)
        # uic.loadUi(os.path.join('user_interface', 'gui_beat.ui'), self)
        self.code_edit = q_code_edit.QCodeEdit()
        with open(os.path.join(".settings", 'q_code_edit.stylesheets')) as f:
            self.code_edit.setStyleSheet(f.read())
        self.layout_for_QCodeEdit.addWidget(self.code_edit)
        self.highlights = Parser(self.code_edit.document())
        self.perform_algorithm_button.clicked.connect(self.start_thread_of_script)
        self.new_code_button.clicked.connect(self.new_file)
        self.save_code_button.clicked.connect(self.save_file)
        self.open_code_button.clicked.connect(self.open_file)
        self.del_code_button.clicked.connect(self.close_file)
        self.choice_algorithm_box.currentTextChanged.connect(self.number_of_current_code_changed)

        q_player.QPlayer.__init__(self)
        self.qt_player.positionChanged.connect(self.position_changed)
        self.track_slider.valueChanged.connect(self.rewind_mouse)
        self.play_pause_button.clicked.connect(self.play_and_pause)
        self.open_file_button.clicked.connect(self.load_file)

        self.scene = QtWidgets.QGraphicsScene()
        self.plots = []

    def start_thread_of_script(self):
        thread = threading.Thread(target=self.running_script)
        thread.start()

    def running_script(self):
        code = self.code_edit.toPlainText().format(wav=self.track)
        try:
            logging.info('Start script execution.')
            exec(code, {"plot": self.plots[self.code_edit.now_file]})
            logging.info('The end of the script.')
        except Exception:
            error = [str(i) for i in sys.exc_info()]
            logging.warning('Runtime error: {}'.format(" | ".join(error)))

            # TODO: does not respond message box and main window
            # message_box.setWindowTitle(error[0])
            # message_box.setText(error[1])
            # message_box.setDetailedText(error[2])
            # message_box.show()

    def add_plot(self, name):
        self.choice_algorithm_box.addItem(name)
        self.choice_algorithm_box.setCurrentIndex(self.choice_algorithm_box.count() - 1)

        message_box = QtWidgets.QMessageBox()
        message_box.setText('\n' + 'Choose type of graph' + '\n')
        message_box.addButton('2D', QtWidgets.QMessageBox.YesRole)
        message_box.addButton('3D', QtWidgets.QMessageBox.NoRole)
        if message_box.exec_():
            self.plots.append(q_plots.Plot3dTest())
            logging.info('Add 3D graph')
        else:
            self.plots.append(q_plots.Plot2d(name=name))
            logging.info('Add 2D graph')

        self.plots_layout.addWidget(self.plots[-1])
        self.plots[-1].set_data()

    def number_of_current_code_changed(self, s):
        if self.plots:
            self.code_edit.cache_file()
            self.code_edit.load_file(s)

    def new_file(self):
        name = self.code_edit.new_file()
        self.add_plot(name)
        logging.info('Create new file and add plot: {}'.format(name))

    def open_file(self):
        name = self.code_edit.open_file()
        if name is not None:
            self.add_plot(name)
            logging.info('Open file and add plot: {}'.format(name))

    def save_file(self):
        self.code_edit.save_file()

    def close_file(self):
        if self.plots:
            save_text = "Save the algorithm?"
            reply = QtWidgets.QMessageBox.question(self,
                                                   'Save',
                                                   save_text,
                                                   QtWidgets.QMessageBox.Yes,
                                                   QtWidgets.QMessageBox.No)

            if reply == QtWidgets.QMessageBox.Yes:
                self.save_file()
            else:
                logging.info("File has NOT been saved.")

            number = self.code_edit.close_file()
            self.plots_layout.takeAt(number).widget().deleteLater()
            self.plots.pop(number)

            self.choice_algorithm_box.removeItem(number)


if __name__ == "__main__":
    logging.basicConfig(
        filename='.log',
        format='%(module)-10s LINE:%(lineno)-3d %(levelname)-8s [%(asctime)s]  %(message)s',
        level=logging.INFO)
    logging.info("Start logging")

    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()

    logging.info('End logging\n')
