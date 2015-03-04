from PyQt5.QtWidgets import QPlainTextEdit, QSizePolicy, QFileDialog, QMessageBox

import styleSheets


class QCodeEdit(QPlainTextEdit):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.setStyleSheet(styleSheets.QCodeEdit)

        self.loaded_files = []  # [[name of file, text of file], ...]
        self.now_file = 0

    def new_file(self):
        import datetime

        self.loaded_files.append({'name': 'Algorithm {}'.format(len(self.loaded_files)),
                                  'path': None,
                                  'text': '{date}\n\nimport calc\n\n'.format(
                                      date=datetime.datetime.now().isoformat(' ')[:-7])})

        self.setPlainText(self.loaded_files[-1]['text'])
        return self.loaded_files[-1]['name']

    def open_file(self):
        path, extension = QFileDialog.getOpenFileName(self, 'Open algorithm', '', filter='*.py')
        if path:
            with open(path, 'r') as f:
                self.setPlainText(f.read())

            name_of_file = path[-path[::-1].find('/'):]
            self.loaded_files.append({'name': name_of_file,
                                      'path': path,
                                      'text': self.toPlainText()})
            self.now_file = len(self.loaded_files) - 1
            return name_of_file

    def load_file(self, name):
        self.loaded_files[self.now_file]['text'] = self.toPlainText()

        for i in range(len(self.loaded_files)):
            if self.loaded_files[i]['name'] in name:
                self.now_file = i
                self.setPlainText(self.loaded_files[i]['text'])
                break

    def save_file(self):
        self.loaded_files[self.now_file]['text'] = self.toPlainText()

        if self.loaded_files[self.now_file]['path'] is None:
            path, extension = QFileDialog.getSaveFileName(self, 'Save algorithm', '', filter='*.py')
            if path[:-3] not in extension[1:]:
                path += extension[1:]
            self.loaded_files[self.now_file]['path'] = path

        with open(self.loaded_files[self.now_file]['path'], 'w') as f:
            f.write(self.toPlainText())

        message_box = QMessageBox()
        message_box.setWindowTitle('Save')
        message_box.setText('\nAlgorithm save to' + self.loaded_files[self.now_file]['path'] + '\n')
        message_box.addButton(QMessageBox.Ok)
        message_box.exec_()

    def close_file(self):
        name = self.loaded_files[self.now_file]['name']
        self.loaded_files.pop(self.now_file)

        if self.loaded_files:
            self.now_file = 0
            self.load_file(self.loaded_files[self.now_file]['name'])
        else:
            self.new_file()

        return name

