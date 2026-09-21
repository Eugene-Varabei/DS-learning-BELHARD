from PyQt5 import QtWidgets
from HelloUI import Ui_MainWindow
import sys

class myWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(myWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #подкл обраб события нажатия на кнопку
        self.ui.btnAnswer.clicked.connect(self.btnAnsw)

    # действие при нажатии на кнопку
    def btnAnsw(self):
        name = self.ui.lineEdit.text()
        text = f'{name}, ваш iPhone заблокирован'
        self.ui.result.setText(text)


app=QtWidgets.QApplication([])
apllication= myWindow()
apllication.show()
sys.exit(app.exec())