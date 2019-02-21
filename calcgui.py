# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.firstfield = QtWidgets.QLineEdit(self.centralwidget)
        self.firstfield.setGeometry(QtCore.QRect(130, 60, 113, 21))
        self.firstfield.setObjectName("firstfield")
        self.opslist = QtWidgets.QComboBox(self.centralwidget)
        self.opslist.setGeometry(QtCore.QRect(320, 60, 104, 26))
        self.opslist.setObjectName("opslist")
        self.secondfield = QtWidgets.QLineEdit(self.centralwidget)
        self.secondfield.setGeometry(QtCore.QRect(520, 60, 113, 21))
        self.secondfield.setObjectName("secondfield")
        self.calcbtn = QtWidgets.QPushButton(self.centralwidget)
        self.calcbtn.setGeometry(QtCore.QRect(320, 150, 113, 32))
        self.calcbtn.setObjectName("calcbtn")
        self.answerfield = QtWidgets.QLineEdit(self.centralwidget)
        self.answerfield.setGeometry(QtCore.QRect(320, 240, 113, 21))
        self.answerfield.setObjectName("answerfield")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.calcbtn.clicked.connect(MainWindow.oncalculate)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.firstfield.setPlaceholderText(_translate("MainWindow", "First Number"))
        self.secondfield.setPlaceholderText(_translate("MainWindow", "Second Number"))
        self.calcbtn.setText(_translate("MainWindow", "Calculate"))
        self.answerfield.setPlaceholderText(_translate("MainWindow", "Answer"))

