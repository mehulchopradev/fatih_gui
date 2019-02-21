from PyQt5 import QtWidgets
from registerui import Ui_MainWindow

class RegisterAuthMainWindow(QtWidgets.QMainWindow):
  def __init__(self):
    super().__init__()
    self.mainwindow = Ui_MainWindow()
    self.mainwindow.setupUi(self)

    self.mainwindow.countrieslist.addItems(['India', 'USA', 'Australia'])
    self.show()

  def onnavtoregister(self):
    self.mainwindow.stackedWidget.setCurrentIndex(1)

  def onnavtologin(self):
    self.mainwindow.stackedWidget.setCurrentIndex(0)

  def onregister(self):
    username = self.mainwindow.usernamefield.text()
    password = self.mainwindow.passwordfield.text()
    country = self.mainwindow.countrieslist.currentText()

    if self.mainwindow.malebtn.isChecked():
      gender = 'Male'
    else:
      gender = 'Female'

    preferences = []
    if self.mainwindow.travelbox.isChecked():
      preferences.append('Travel')

    if self.mainwindow.shoppingbox.isChecked():
      preferences.append('Shopping')

    if self.mainwindow.sportsbox.isChecked():
      preferences.append('Sports')

    print(username)
    print(password)
    print(gender)
    print(country)
    print(preferences)

    # could store this data anywhere

if __name__ == '__main__':
  app = QtWidgets.QApplication([])
  window = RegisterAuthMainWindow()
  app.exec_()