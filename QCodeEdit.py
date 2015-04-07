from PyQt5.QtWidgets import QPlainTextEdit, QSizePolicy, QFileDialog, QMessageBox

import styleSheets


class QCodeEdit(QPlainTextEdit):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.setStyleSheet(styleSheets.QCodeEdit)
        self.setWordWrapMode(0)

        self.loaded_files = []  # [{name of file, text of file, text of file}, ...]
        self.now_file = None

    @property
    def now_file(self):
        return self.__now_file

    @now_file.setter
    def now_file(self, n):
        self.__now_file = n

    def new_file(self):
        if self.now_file is not None:
            self.loaded_files[self.now_file]['text'] = self.toPlainText()
        import datetime

        with open('default.py', 'r') as f:
            code = f.read()

        self.loaded_files.append({'name': 'Algorithm {}'.format(len(self.loaded_files)),
                                  'path': None,
                                  'text': '# {date}\n{code}'.format(
                                      date=datetime.datetime.now().isoformat(' ')[:-7], code=code)})

        self.setPlainText(self.loaded_files[-1]['text'])
        self.now_file = len(self.loaded_files) - 1
        return self.loaded_files[-1]['name']

    def open_file(self):
        if self.now_file is not None:
            try:
                self.loaded_files[self.now_file]['text'] = self.toPlainText()
            except:
                pass
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
        return None

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
            self.loaded_files[self.now_file]['path'], _ = \
                QFileDialog.getSaveFileName(self, 'Save algorithm', '', filter='*.py')

        print(self.loaded_files[self.now_file]['path'])
        if self.loaded_files[self.now_file]['path']:
            if self.loaded_files[self.now_file]['path'][-3:] not in '.py':
                self.loaded_files[self.now_file]['path'] += '.py'

            with open(self.loaded_files[self.now_file]['path'], 'w') as f:
                f.write(self.loaded_files[self.now_file]['text'])

        message_box = QMessageBox()
        message_box.setWindowTitle('Save')
        if self.loaded_files[self.now_file]['path']:
            message_box.setText('\nAlgorithm save to' + self.loaded_files[self.now_file]['path'] + '\n')
        else:
            message_box.setText("\nThe algorithm is not saved" + '\n')

        message_box.addButton(QMessageBox.Ok)
        message_box.exec_()

    def close_file(self):
        number = self.now_file

        self.loaded_files.pop(self.now_file)

        if self.loaded_files:
            self.now_file = 0
            self.load_file(self.loaded_files[self.now_file]['name'])
        else:
            self.setPlainText('Загрузите файл')  # FIXME создать новый файл
            self.now_file = None
        return number

