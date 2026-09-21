from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from Cal import Ui_MainWindow
import sys

class myWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(myWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # создание доп переменных
        # для зранения чисел
        self.numberA = 0
        self.numberB = 0
        self.numberC = 0
        # для хранения действия
        self.action = ''
        #для хранения указания нужно ли очищать число
        self.isClear= False


        # обработка нажатия на цифры
        self.ui.btn0.clicked.connect(self.btnNumberClick)
        self.ui.btn1.clicked.connect(self.btnNumberClick)
        self.ui.btn2.clicked.connect(self.btnNumberClick)
        self.ui.btn3.clicked.connect(self.btnNumberClick)
        self.ui.btn4.clicked.connect(self.btnNumberClick)
        self.ui.btn5.clicked.connect(self.btnNumberClick)
        self.ui.btn6.clicked.connect(self.btnNumberClick)
        self.ui.btn7.clicked.connect(self.btnNumberClick)
        self.ui.btn8.clicked.connect(self.btnNumberClick)
        self.ui.btn9.clicked.connect(self.btnNumberClick)
        # обработка нажатия на арифм кнопки
        self.ui.btnAdd.clicked.connect(self.btnAriphmetikClick)
        self.ui.btnSub.clicked.connect(self.btnAriphmetikClick)
        self.ui.btnDif.clicked.connect(self.btnAriphmetikClick)
        self.ui.btnMulty.clicked.connect(self.btnAriphmetikClick)
        self.ui.btnPow.clicked.connect(self.btnAriphmetikClick)
        #обработка нажатия равно
        self.ui.btnAnswer.clicked.connect(self.btnAnswerClick)
        #обработка нажатия на кнопку точка
        self.ui.btnDot.clicked.connect(self.btnDotClick)
        #обработка +- кнопки
        self.ui.btnPosNeg.clicked.connect(self.btnPosNegClick)
        # обработка кнопки sqrt
        self.ui.btnSqrt.clicked.connect(self.btnSqrtClick)
        # обработка кнопки back
        self.ui.btnDel.clicked.connect(self.btnDelClick)
        #обработка кнопки Clean
        self.ui.btnClean.clicked.connect(self.btnCleanClick)
        #обработка нажатия на кнопку клавы
        self.ui.number.keyPressEvent =self.onKeyPress


    # действие при нажатии на цифры
    def btnNumberClick(self):
        if self.action== '=':
            self.action= ''
        #получаем объект кнопки на которую нажали
        btn=self.sender()
        #чтекние надписи (цифры) с нажатия кнопки
        digit=btn.text()
        #чтение числа введенного в кальк
        number=self.ui.number.text()
        if self.isClear:
            number='0'
            self.isClear = False
        if number=="0":
            number= digit
        else:
            number+=digit
        #полученное число - ввод на кальк
        self.ui.number.setText(number)

    #действие при нажатии на арифм кнопки
    def btnAriphmetikClick(self):
        btn = self.sender()
        self.action = btn.text()
        self.numberA = float(self.ui.number.text())
        self.isClear=True

    #действие равно
    def btnAnswerClick(self):
        self.numberB=float(self.ui.number.text())
        if self.action == "+":
            self.numberC=self.numberA + self.numberB
        elif self.action == "-":
            self.numberC=self.numberA - self.numberB
        elif self.action == "*":
            self.numberC=self.numberA * self.numberB
        elif self.action == "/":
            if self.numberB == 0:
                self.numberC = 0
            else:
                self.numberC = self.numberA / self.numberB
        elif self.action == "x^y":
            self.numberC=self.numberA**self.numberB
        if int(self.numberC)==self.numberC:
            self.ui.number.setText(str(int(self.numberC)))
        else:
            self.ui.number.setText(str(self.numberC))
        self.ui.number.setText(str(self.numberC))
        self.isClear = True
        self.action = '='

    #действие при нажатии на точку
    def btnDotClick(self):
        number=self.ui.number.text()
        if number.find('.')==-1:
            number += "."
            self.ui.number.setText(number)
    #действие при нажатии +-
    def btnPosNegClick(self):
        number = self.ui.number.text()
        if number[0]=='-':
            number=number[1:]
        else:
            number= '-' + number
        self.ui.number.setText(number)

    # действие кнопки SQRT
    def btnSqrtClick(self):
        self.numberA=float(self.ui.number.text())

        if self.numberA>0:
            self.numberC = self.numberA**0.5
        else:
            self.numberC = 0
        self.ui.number.setText(str(self.numberC))
        self.action = '='
        self.isClear=True

    #действие кнопки back
    def btnDelClick(self):
        if self.action == '=':
            return
        number=self.ui.number.text()
        if len(number)==1:
            number = '0'
        else:
            number=number[:-1]
        self.ui.number.setText(number)

    # обработка кнопки clean
    def btnCleanClick(self):
        self.ui.number.setText('0')
        self.numberA =0
        self.numberB =0 
        self.numberC =0
        self.action=('')
        self.isClear=False

    #действие по нажатию на клавиатуре
    def onKeyPress(self, data):
        if not(data.text() >= '0' and data.text() <='9'
                or data.text() == '.' or data.text() == '-'
                or data.key() == Qt.Key_Backspace):
            return
        if self.isClear == True:
            self.ui.number.setText(data.text())
            self.isClear= False
            return
        number=self.ui.number.text()
        if number == '0':
            number = data.text()
        elif data.text()=='.':
             if number.find('.')==-1:
                 number += '.'
        elif data.text() == '-':
            if number[0]=='-':
                number = number[1:]
            else:
                number = '-' + number
        elif data.key() == Qt.Key_Backspace:
            if self.action != '=':
                if len(number)==1:
                    number= '0'
                else:
                    number=number[:-1]

        else:
            number += data.text()
        self.ui.number.setText(number)




app=QtWidgets.QApplication([])
apllication= myWindow()
apllication.show()
sys.exit(app.exec())