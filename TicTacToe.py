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
        self.wincheck()


    def wincheck(self):
        is_win = False
        # Row
        if self.pushButton_1.text() != "" and self.pushButton_1.text() == self.pushButton_2.text() == self.pushButton_3.text():
            self.win(self.pushButton_1, self.pushButton_2, self.pushButton_3)
            is_win = True
        
        elif self.pushButton_4.text() != "" and self.pushButton_4.text() == self.pushButton_5.text() == self.pushButton_6.text():
            self.win(self.pushButton_4, self.pushButton_5, self.pushButton_6)
            is_win = True
        
        elif self.pushButton_7.text() != "" and self.pushButton_7.text() == self.pushButton_8.text() == self.pushButton_9.text():
            self.win(self.pushButton_7, self.pushButton_8, self.pushButton_9)
            is_win = True
        
        # column
        elif self.pushButton_1.text() != "" and self.pushButton_1.text() == self.pushButton_4.text() == self.pushButton_7.text():
            self.win(self.pushButton_1, self.pushButton_4, self.pushButton_7)
            is_win = True
        
        elif self.pushButton_2.text() != "" and self.pushButton_2.text() == self.pushButton_5.text() == self.pushButton_8.text():
            self.win(self.pushButton_2, self.pushButton_5, self.pushButton_8)
            is_win = True
        
        elif self.pushButton_3.text() != "" and self.pushButton_3.text() == self.pushButton_6.text() == self.pushButton_9.text():
            self.win(self.pushButton_3, self.pushButton_6, self.pushButton_9)
            is_win = True
        
        # diagonal
        elif self.pushButton_1.text() != "" and self.pushButton_1.text() == self.pushButton_5.text() == self.pushButton_9.text():
            self.win(self.pushButton_1, self.pushButton_5, self.pushButton_9)
            is_win = True

        elif self.pushButton_3.text() != "" and self.pushButton_3.text() == self.pushButton_5.text() == self.pushButton_7.text():
            self.win(self.pushButton_3, self.pushButton_5, self.pushButton_7)
            is_win = True
        
        # Tie
        if (not is_win) and self.counter == 9:
            self.label.setText("Tie!")  

        
    def win(self, button1, button2, button3):
        button1.setStyleSheet("QPushButton{background-color:rgb(10, 25, 49); color:rgb(255, 73, 122);}")
        button2.setStyleSheet("QPushButton{background-color:rgb(10, 25, 49); color:rgb(255, 73, 122);}")
        button3.setStyleSheet("QPushButton{background-color:rgb(10, 25, 49); color:rgb(255, 73, 122);}")

        buttons = [self.pushButton_1, self.pushButton_2, self.pushButton_3, self.pushButton_4, self.pushButton_5,
                    self.pushButton_6, self.pushButton_7, self.pushButton_8, self.pushButton_9]

        for button in buttons:
            button.setEnabled(False)

        self.label.setText(f"{button1.text()} Win!")

    
    def reset(self):
        buttons = [self.pushButton_1, self.pushButton_2, self.pushButton_3, self.pushButton_4, self.pushButton_5,
                    self.pushButton_6, self.pushButton_7, self.pushButton_8, self.pushButton_9]

        for button in buttons:
            button.setText("")
            button.setEnabled(True)
            button.setStyleSheet("QPushButton{background-color: rgb(10, 25, 49); color: rgb(255, 201, 71);}\n"
                                "QPushButton::pressed{background-color: rgb(255, 201, 71); color: rgb(10, 25, 49);}")
        
        self.counter = 0
        self.label.setText("X's turn")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = UI()
    sys.exit(app.exec_())