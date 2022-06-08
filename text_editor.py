from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QFileDialog
import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle('Редактор текста')
        self.setGeometry(300, 250, 350, 200)

        self.text_edit = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.createMenu()

    def createMenu(self):
        self.menu = QMenuBar(self)
        self.setMenuBar(self.menu)

        self.menu_task = QMenu('&Файл', self)
        self.menu.addMenu(self.menu_task)

        self.menu_task.addAction('Открыть', self.action)
        self.menu_task.addAction('Сохранить', self.action)


    @QtCore.pyqtSlot()
    def action(self):
        act = self.sender()
        if act.text() == 'Открыть':
            file = QFileDialog.getOpenFileName(self)[0]

            try:
                f = open(file, 'r')
                with f:
                    data = f.read()
                    self.text_edit.setText(data)
                f.close()
            except FileNotFoundError:
                print('No such file')

        elif act.text() == 'Сохранить':
            file = QFileDialog.getSaveFileName(self)[0]

            try:
                f = open(file, 'w')
                text = self.text_edit.toPlainText()
                f.write(text)
                f.close()
            except FileNotFoundError:
                print('No such file')




def start():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    start()
