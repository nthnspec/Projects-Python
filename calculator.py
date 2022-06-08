from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Calculator")
        MainWindow.resize(380, 320)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-1, 0, 501, 50))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.label.setObjectName("label")
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_0.setGeometry(QtCore.QRect(0, 263, 213, 57))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn_0.setFont(font)
        self.btn_0.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.btn_0.setObjectName("btn_0")
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(0, 50, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.btn_7.setObjectName("btn_7")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(0, 121, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.btn_4.setObjectName("btn_4")
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(142, 121, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.btn_6.setObjectName("btn_6")
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(142, 50, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.btn_9.setObjectName("btn_9")
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(142, 192, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.btn_3.setObjectName("btn_3")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(71, 192, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.btn_2.setObjectName("btn_2")
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(71, 50, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.btn_8.setObjectName("btn_8")
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(71, 121, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.btn_5.setObjectName("btn_5")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(0, 192, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.btn_1.setObjectName("btn_1")
        self.btn_equal = QtWidgets.QPushButton(self.centralwidget)
        self.btn_equal.setGeometry(QtCore.QRect(213, 263, 168, 57))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn_equal.setFont(font)
        self.btn_equal.setStyleSheet("background-color: rgb(255, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.btn_equal.setObjectName("btn_equal")
        self.btn_sqrt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sqrt.setGeometry(QtCore.QRect(213, 50, 84, 71))
        self.btn_sqrt.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.btn_sqrt.setObjectName("btn_sqrt")
        self.btn_minus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_minus.setGeometry(QtCore.QRect(297, 192, 84, 71))
        self.btn_minus.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.btn_minus.setObjectName("btn_minus")
        self.btn_plus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_plus.setGeometry(QtCore.QRect(213, 192, 84, 71))
        self.btn_plus.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.btn_plus.setObjectName("btn_plus")
        self.btn_razd = QtWidgets.QPushButton(self.centralwidget)
        self.btn_razd.setGeometry(QtCore.QRect(297, 121, 84, 71))
        self.btn_razd.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.btn_razd.setObjectName("btn_razd")
        self.btn_umn = QtWidgets.QPushButton(self.centralwidget)
        self.btn_umn.setGeometry(QtCore.QRect(213, 121, 84, 71))
        self.btn_umn.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.btn_umn.setObjectName("btn_umn")
        self.btn_pow = QtWidgets.QPushButton(self.centralwidget)
        self.btn_pow.setGeometry(QtCore.QRect(297, 50, 84, 71))
        self.btn_pow.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.btn_pow.setObjectName("btn_pow")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_func()
        self.is_equal = False

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Calculator", "Calculator"))
        self.label.setText(_translate("MainWindow", "0"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_equal.setText(_translate("MainWindow", "="))
        self.btn_sqrt.setText(_translate("MainWindow", "**0.5"))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_razd.setText(_translate("MainWindow", "/"))
        self.btn_umn.setText(_translate("MainWindow", "*"))
        self.btn_pow.setText(_translate("MainWindow", "**"))

    def add_func(self):
            self.btn_1.clicked.connect(lambda: self.write_number(self.btn_1.text()))
            self.btn_2.clicked.connect(lambda: self.write_number(self.btn_2.text()))
            self.btn_3.clicked.connect(lambda: self.write_number(self.btn_3.text()))
            self.btn_4.clicked.connect(lambda: self.write_number(self.btn_4.text()))
            self.btn_5.clicked.connect(lambda: self.write_number(self.btn_5.text()))
            self.btn_6.clicked.connect(lambda: self.write_number(self.btn_6.text()))
            self.btn_7.clicked.connect(lambda: self.write_number(self.btn_7.text()))
            self.btn_8.clicked.connect(lambda: self.write_number(self.btn_8.text()))
            self.btn_9.clicked.connect(lambda: self.write_number(self.btn_9.text()))
            self.btn_0.clicked.connect(lambda: self.write_number(self.btn_0.text()))
            self.btn_plus.clicked.connect(lambda: self.write_number(self.btn_plus.text()))
            self.btn_minus.clicked.connect(lambda: self.write_number(self.btn_minus.text()))
            self.btn_umn.clicked.connect(lambda: self.write_number(self.btn_umn.text()))
            self.btn_razd.clicked.connect(lambda: self.write_number(self.btn_razd.text()))
            self.btn_pow.clicked.connect(lambda: self.write_number(self.btn_pow.text()))
            self.btn_sqrt.clicked.connect(lambda: self.write_number(self.btn_sqrt.text()))

            self.btn_equal.clicked.connect(lambda: self.make_res())

    def write_number(self, number):
            res = number
            if self.label.text() == '0' or self.is_equal == True:
                self.label.setText(number)
                self.is_equal = False
            else:    
                self.label.setText(self.label.text() + number) 


    def make_res(self):
            if not self.is_equal:
                res = eval(self.label.text())
                self.label.setText(str(res))
                self.is_equal = True
            else: 
                error = QMessageBox()

                error.setWindowTitle('Ошибка')
                error.setText('Сейчас это действие выполнить нельзя')
                error.setIcon(QMessageBox.Warning)
                error.setStandardButtons(QMessageBox.Reset | QMessageBox.Ok)
                error.setDefaultButton(QMessageBox.Ok)
                error.setInformativeText('Нет никаких математический действий')
                error.setDetailedText('Двойное нажатие клавиши "=" приводит к ошибке, так как нет никаких действий, которые считывает программа')
                error.buttonClicked.connect(self.popup_action)


                error.exec_()


    def popup_action(self, btn):
            if btn.text() == 'Reset':
                self.label.setText('')
                self.is_equal = False




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())