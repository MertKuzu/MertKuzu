import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()

    win.setWindowTitle("First App")  #title
    win.setGeometry(200,200,500,500)   #window size
    win.setWindowIcon(QIcon("logo.png"))
    win.setToolTip("ses ver adana zirveden selam")

    win.show() 
    sys.exit(app.exec_())  #adding x icon for exit

window()