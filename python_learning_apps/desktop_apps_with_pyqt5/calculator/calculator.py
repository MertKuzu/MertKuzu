from operator import eq
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QIcon, QFont


class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(200,200,500,500)
        self.setWindowIcon(QIcon("Apple_Hesap_makinesi_Calculator-icon.png"))
        self.initUI()

    def initUI(self):
        #1 button
        self.btn_one = QPushButton(self)
        self.btn_one.setText("1")
        self.btn_one.move(30,30)
        self.btn_one.resize(70,50)

        #2 button
        self.btn_two = QPushButton(self)
        self.btn_two.setText("2")
        self.btn_two.move(110,30)
        self.btn_two.resize(70,50)

        #3 button
        self.btn_three = QPushButton(self)
        self.btn_three.setText("3")
        self.btn_three.move(190,30)
        self.btn_three.resize(70,50)

        #4 button
        self.btn_four = QPushButton(self)
        self.btn_four.setText("4")
        self.btn_four.move(30,90)
        self.btn_four.resize(70,50)

        #5 button
        self.btn_five = QPushButton(self)
        self.btn_five.setText("5")
        self.btn_five.move(110,90)
        self.btn_five.resize(70,50)

        #6 button
        self.btn_six = QPushButton(self)
        self.btn_six.setText("6")
        self.btn_six.move(190,90)
        self.btn_six.resize(70,50)

        #7 button
        self.btn_seven = QPushButton(self)
        self.btn_seven.setText("7")
        self.btn_seven.move(30,150)
        self.btn_seven.resize(70,50)

        #8 button
        self.btn_eight = QPushButton(self)
        self.btn_eight.setText("8")
        self.btn_eight.move(110,150)
        self.btn_eight.resize(70,50)

        #9 button
        self.btn_nine = QPushButton(self)
        self.btn_nine.setText("9")
        self.btn_nine.move(190,150)
        self.btn_nine.resize(70,50)

        # + button
        self.btn_sum = QPushButton(self)
        self.btn_sum.setText("+")
        self.btn_sum.move(300,30)
        self.btn_sum.resize(80,80)

        # - button
        self.btn_subt = QPushButton(self)
        self.btn_subt.setText("-")
        self.btn_subt.move(400,30)
        self.btn_subt.resize(80,80)

        # x button
        self.btn_mul = QPushButton(self)
        self.btn_mul.setText("x")
        self.btn_mul.move(300,120)
        self.btn_mul.resize(80,80)

        # / button
        self.btn_div = QPushButton(self)
        self.btn_div.setText("÷")
        self.btn_div.move(400,120)
        self.btn_div.resize(80,80)

        # = button 
        self.btn_eq = QPushButton(self)
        self.btn_eq.setText("=")
        self.btn_eq.move(300,210)
        self.btn_eq.resize(180,50)

        # 0 button
        self.btn_zero = QPushButton(self)
        self.btn_zero.setText("0")
        self.btn_zero.move(30,210)
        self.btn_zero.resize(150,50)

        # clear button
        self.btn_clear = QPushButton(self)
        self.btn_clear.setText("C")
        self.btn_clear.move(300,270)
        self.btn_clear.resize(80,80)

        # delete button
        self.btn_del = QPushButton(self)
        self.btn_del.setText("Delete")
        self.btn_del.move(400,270)
        self.btn_del.resize(80,80)

        # point button
        self.btn_point = QPushButton(self)
        self.btn_point.setText(".")
        self.btn_point.move(190,210)
        self.btn_point.resize(70,50)

        # result screen
        self.label = QtWidgets.QLabel(self)
        self.label.setText("")
        self.label.move(30,400)
        self.label.resize(422,50)
        self.label.setFont(QFont('',16))


        self.btn_one.clicked.connect(self.compute)
        self.btn_two.clicked.connect(self.compute)
        self.btn_three.clicked.connect(self.compute)
        self.btn_four.clicked.connect(self.compute)
        self.btn_five.clicked.connect(self.compute)
        self.btn_six.clicked.connect(self.compute)
        self.btn_seven.clicked.connect(self.compute)
        self.btn_eight.clicked.connect(self.compute)
        self.btn_nine.clicked.connect(self.compute)
        self.btn_zero.clicked.connect(self.compute)
        self.btn_point.clicked.connect(self.compute)
        self.btn_sum.clicked.connect(self.compute)
        self.btn_subt.clicked.connect(self.compute)
        self.btn_mul.clicked.connect(self.compute)
        self.btn_div.clicked.connect(self.compute)
        self.btn_clear.clicked.connect(self.compute)
        self.btn_del.clicked.connect(self.compute)
        self.btn_eq.clicked.connect(self.compute)


    def compute(self):
        sender = self.sender().text()
        text = self.label.text()

        #appending label text
        if sender == '1':
            self.label.setText(text + "1")
        elif sender == '2':
            self.label.setText(text + "2")
        elif sender == '3':
            self.label.setText(text + "3")
        elif sender == '4':
            self.label.setText(text + "4")
        elif sender == '5':
            self.label.setText(text + "5")
        elif sender == '6':
            self.label.setText(text + "6")
        elif sender == '7':
            self.label.setText(text + "7")
        elif sender == '8':
            self.label.setText(text + "8")
        elif sender == '9':
            self.label.setText(text + "9")
        elif sender == '0':
            self.label.setText(text + "0")
        elif sender == '.':
            self.label.setText(text+".")
        elif sender == "+":
            self.label.setText(text+"+")
        elif sender == "-":
            self.label.setText(text+"-")
        elif sender == "x":
            self.label.setText(text+"*")
        elif sender == "÷":
            self.label.setText(text+"/")
        elif sender == "C":
            self.label.setText("")
        elif sender == "Delete":
            self.label.setText(text[:len(text)-1])
        elif sender == "=":
            equal = self.label.text()

            try:
                ans = eval(equal)
                self.label.setText(text + "="+ str(ans))
            except:
                self.label.setText("Result: Wrong Input")



def app():
    app = QApplication(sys.argv)
    win = Calculator()
    win.show()

    sys.exit(app.exec_())

app()