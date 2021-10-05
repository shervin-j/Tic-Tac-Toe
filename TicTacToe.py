from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("TicTacToe.ui", self)
        self.counter = 0
        self.pushButton_1.clicked.connect(lambda : self.writeXO(self.pushButton_1))
        self.pushButton_2.clicked.connect(lambda : self.writeXO(self.pushButton_2))
        self.pushButton_3.clicked.connect(lambda : self.writeXO(self.pushButton_3))
        self.pushButton_4.clicked.connect(lambda : self.writeXO(self.pushButton_4))
        self.pushButton_5.clicked.connect(lambda : self.writeXO(self.pushButton_5))
        self.pushButton_6.clicked.connect(lambda : self.writeXO(self.pushButton_6))
        self.pushButton_7.clicked.connect(lambda : self.writeXO(self.pushButton_7))
        self.pushButton_8.clicked.connect(lambda : self.writeXO(self.pushButton_8))
        self.pushButton_9.clicked.connect(lambda : self.writeXO(self.pushButton_9))
        self.start_over_button.clicked.connect(self.reset)
        
        self.show()

    def writeXO(self, button):
        if self.counter % 2 == 0: 
            button.setText("X")
            self.label.setText("O's turn")
        
        else:
            button.setText("O")
            self.label.setText("X's turn")

        button.setEnabled(False)
        self.counter += 1


    def reset(self):
        buttons = [self.pushButton_1, self.pushButton_2, self.pushButton_3, self.pushButton_4, self.pushButton_5,
                    self.pushButton_6, self.pushButton_7, self.pushButton_8, self.pushButton_9]

        for button in buttons:
            button.setText("")
            button.setEnabled(True)
        
        self.counter = 0

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = UI()
    sys.exit(app.exec_())