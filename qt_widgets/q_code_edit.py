import os
import datetime
import logging

from PyQt5.QtWidgets import QPlainTextEdit, QSizePolicy, QFileDialog, QMessageBox


class Database():
    def __init__(self):
        self.loaded_files = []  # [{name: name_of_file, path: path_of_file, text: text_of_file}, ...]
        self._now_file = None

    @property
    def now_file(self):
        return self._now_file

    @now_file.setter
    def now_file(self, n):
        if (n is None) or (0 < n + 1 <= len(self.loaded_files)):
            self._now_file = n
        else:
            logging.warning(
                "n is None: " + str(n is None) +
                "0 < n+1 < len(self.loaded_files): " + str(0 < n + 1 < len(self.loaded_files)) +
                "str(n): " + str(n) +
                "len(self.loaded_files): " + str(len(self.loaded_files))
            )
            raise IndexError

    @property
    def script_name(self):
        return self.loaded_files[self.now_file]['name']

    @script_name.setter
    def script_name(self, name):
        self.loaded_files[self.now_file]['name'] = name

    @property
    def script_path(self):
        return self.loaded_files[self.now_file]['path']

    @script_path.setter
    def script_path(self, path):
        self.loaded_files[self.now_file]['path'] = path

    @property
    def script(self):
        return self.loaded_files[self.now_file]['text']

    @script.setter
    def script(self, text):
        self.loaded_files[self.now_file]['text'] = text


class QCodeEdit(QPlainTextEdit, Database):
    def __init__(self, *args):
        super().__init__(*args)
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.setWordWrapMode(0)

    def new_file(self):
        if self.now_file is not None:
            self.script = self.toPlainText()

        with open(os.path.join('.settings', 'default_script.py'), 'r') as f:
            code = f.read()

        name = 'Algorithm #{}'.format(len(self.loaded_files))
        date = datetime.datetime.now().isoformat(' ')[:-7]
        text = '# {date}\n{code}'.format(date=date, code=code)

        self.loaded_files.append({'name': name,
                                  'path': None,
                                  'text': text})

        self.setPlainText(text)
        self.now_file = len(self.loaded_files) - 1
        return name

    def open_file(self):
        if self.now_file is not None:
            self.script = self.toPlainText()  # saving changes of the algorithm
        path, extension = QFileDialog.getOpenFileName(self, 'Open algorithm', '')
        if path:
            name_of_file = os.path.basename(path)
            with open(path, 'r') as f:
                text = f.read()

            self.loaded_files.append({'name': name_of_file,
                                      'path': path,
                                      'text': text})

            self.setPlainText(text)
            self.now_file = len(self.loaded_files) - 1

            return name_of_file
        return None

    def cache_file(self):
        logging.info('Cache file #' + str(self.now_file))
        self.script = self.toPlainText()

    def load_file(self, name):
        logging.info('Load file: ' + str(name))
        for i in range(len(self.loaded_files)):
            if self.loaded_files[i]['name'] in name:
                self.setPlainText(self.loaded_files[i]['text'])
                self.now_file = i
                logging.info('Load file #' + str(i))
                break

    def save_file(self):
        self.cache_file()
        if self.script_path is None:
            self.script_path, _ = QFileDialog.getSaveFileName(self, 'Save algorithm', '')
        else:
            if self.script_path[-3:] != '.py':
                self.script_path += '.py'

            with open(self.script_path, 'w') as f:
                f.write(self.script)

        message_box = QMessageBox()
        message_box.setWindowTitle('Save')
        if self.script_path:
            message_box.setText('\nAlgorithm save to' + self.script_path + '\n')
            logging.info("File has been saved.")
        else:
            message_box.setText("\nFile has NOT been saved" + '\n')

        message_box.addButton(QMessageBox.Ok)
        message_box.exec_()

    def close_file(self):
        number = self.now_file

        self.loaded_files.pop(self.now_file)

        if self.loaded_files:
            self.now_file = 0
            self.load_file(self.script_name)
        else:
            self.setPlainText('Загрузите файл')
            self.now_file = None
        return number
