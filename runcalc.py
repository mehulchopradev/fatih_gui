from PyQt5 import QtWidgets
from calcgui import Ui_MainWindow

class CalcMainWindow(QtWidgets.QMainWindow):
  def __init__(self):
    super().__init__()
    self.mainwindow = Ui_MainWindow()
    self.mainwindow.setupUi(self)

    self.opslist = self.mainwindow.opslist
    self.initopslist()
    self.show()

  def initopslist(self):
    self.opslist.addItems(['+','-','*','/'])

  # slot
  def oncalculate(self):
    first = float(self.mainwindow.firstfield.text())
    second = float(self.mainwindow.secondfield.text())
    op = self.opslist.currentText()

    if op == '+':
      answer = first + second
    elif op == '-':
      answer = first - second
    elif op == '*':
      answer = first * second
    else:
      answer = first / second

    self.mainwindow.answerfield.setText(str(answer))

if __name__ == '__main__':
  app = QtWidgets.QApplication([])
  window = CalcMainWindow()
  app.exec_()