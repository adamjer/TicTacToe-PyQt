import sys
import random
import time
from PyQt5 import QtGui, QtWidgets, QtCore

class Tic(QtWidgets.QMainWindow):
    def __init__(self):
        super(Tic,self).__init__()
        self.setGeometry(50,50,360,410)
        self.setWindowTitle('Kółko i krzyżyk')

        self.player = ''
        self.winner = ''
        self.board()
        self.new_game()

    def setBoard(self):
        # set up game board
        self.btn0 = QtWidgets.QPushButton('', self)   # first argument is the text
        self.btn0.clicked.connect(lambda: self.clicked(0))  
        self.btn0.resize(100,100)
        self.btn0.move(20,280)

        self.btn1 = QtWidgets.QPushButton('', self)   
        self.btn1.clicked.connect(lambda: self.clicked(1))  
        self.btn1.resize(100,100)
        self.btn1.move(130,280)

        self.btn2 = QtWidgets.QPushButton('', self)  
        self.btn2.clicked.connect(lambda: self.clicked(2))  
        self.btn2.resize(100,100)
        self.btn2.move(240,280)

        self.btn3 = QtWidgets.QPushButton('', self)   
        self.btn3.clicked.connect(lambda: self.clicked(3))  
        self.btn3.resize(100,100)
        self.btn3.move(20,170)

        self.btn4 = QtWidgets.QPushButton('', self)   
        self.btn4.clicked.connect(lambda: self.clicked(4))  
        self.btn4.resize(100,100)
        self.btn4.move(130,170)

        self.btn5 = QtWidgets.QPushButton('', self)  
        self.btn5.clicked.connect(lambda: self.clicked(5))  
        self.btn5.resize(100,100)
        self.btn5.move(240,170)

        self.btn6 = QtWidgets.QPushButton('', self)   
        self.btn6.clicked.connect(lambda: self.clicked(6))  
        self.btn6.resize(100,100)
        self.btn6.move(20,60)

        self.btn7 = QtWidgets.QPushButton('', self)   
        self.btn7.clicked.connect(lambda: self.clicked(7))  
        self.btn7.resize(100,100)
        self.btn7.move(130,60)

        self.btn8 = QtWidgets.QPushButton('', self)  
        self.btn8.clicked.connect(lambda: self.clicked(8))  
        self.btn8.resize(100,100)
        self.btn8.move(240,60)

    def board(self):
        newAction = QtWidgets.QAction('Nowa gra', self)
        newAction.setShortcut('Ctrl+N')
        newAction.setStatusTip('Rozpocznij nową rozgrywkę')
        newAction.triggered.connect(self.new_game)

        # add an exit feature
        exitAction = QtWidgets.QAction('Zakończ', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Wyjście z aplikacji')
        exitAction.triggered.connect(self.close_application)

        aboutAction = QtWidgets.QAction('O programie', self)
        aboutAction.setStatusTip('Informacje o programie')
        aboutAction.triggered.connect(self.about)

        self.statusBar()

        # menu part of exit feature
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('Plik')
        helpMenu = mainMenu.addMenu('Pomoc')

        # new game feature
        fileMenu.addAction(newAction)

        # exit
        fileMenu.addAction(exitAction)

        #about
        helpMenu.addAction(aboutAction)

        # initialize board
        self.setBoard()

        # list of taken move positions
        self.taken = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.takenBy = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.btnDict = {  
            0 : lambda x : (self.btn0.setText(x), self.btn0.setFont(QtGui.QFont('Times', 50))),
            1 : lambda x : (self.btn1.setText(x), self.btn1.setFont(QtGui.QFont('Times', 50))),
            2 : lambda x : (self.btn2.setText(x), self.btn2.setFont(QtGui.QFont('Times', 50))),
            3 : lambda x : (self.btn3.setText(x), self.btn3.setFont(QtGui.QFont('Times', 50))),
            4 : lambda x : (self.btn4.setText(x), self.btn4.setFont(QtGui.QFont('Times', 50))),
            5 : lambda x : (self.btn5.setText(x), self.btn5.setFont(QtGui.QFont('Times', 50))),
            6 : lambda x : (self.btn6.setText(x), self.btn6.setFont(QtGui.QFont('Times', 50))),
            7 : lambda x : (self.btn7.setText(x), self.btn7.setFont(QtGui.QFont('Times', 50))),
            8 : lambda x : (self.btn8.setText(x), self.btn8.setFont(QtGui.QFont('Times', 50)))
        }

        # this should always be last
        self.show()

    def change_player(self):
        if self.player == 'X':
            self.player = 'O'
        else:
            self.player = 'X'

    def clicked(self, btnval):
        if self.taken[btnval] == 0:
            # update free moves & the screen
            self.btnDict[btnval](self.player)
            self.taken[btnval] = 1
            # update who-owns-what to check if there's a winner
            if self.player == 'X':
                self.takenBy[btnval] = 'X'
            else:
                self.takenBy[btnval] = 'O'
            print(self.takenBy)
            self.test_for_winner()
            self.change_player()
            self.show()
        else:
            pass

    def new_game(self):
        [self.btnDict[key]("") for key in self.btnDict]
        self.winner = ''

        self.taken = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.takenBy = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.player = 'O'
        if(random.randrange(10) < 5):
            self.player = 'X'

    def showDialog(self, title, text):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Question)
        msgBox.setText(text)
        msgBox.setWindowTitle(title)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        buttonY = msgBox.button(QtWidgets.QMessageBox.Yes)
        buttonY.setText('Tak')
        buttonN = msgBox.button(QtWidgets.QMessageBox.No)
        buttonN.setText('Nie')
        return msgBox.exec_()

    def test_for_winner(self):
        # enumerate possible winner configurations
        winning_configs = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for j in range(8):
            if self.takenBy[winning_configs[j][0]] == 'X' and \
               self.takenBy[winning_configs[j][1]] == 'X' and \
               self.takenBy[winning_configs[j][2]] == 'X':
                self.winner = 'X'
            if self.takenBy[winning_configs[j][0]] == 'O' and \
               self.takenBy[winning_configs[j][1]] == 'O' and \
               self.takenBy[winning_configs[j][2]] == 'O':
                self.winner = 'O'

        # if there is a winner, report it and end the game
        if self.winner == 'X' or self.winner == 'O':
            msg = '{} wygrał! Chcesz zagrać ponownie?'.format(self.winner)

            if self.showDialog('Koniec gry!', msg) == QtWidgets.QMessageBox.Yes:
                self.close()
                self.__init__()
            else:
                sys.exit()

        # if there's a draw, handle it here
        if self.winner == '' and sum(self.taken) == 9:
            msg = 'Remis! Chcesz zagrać ponownie?'

            if self.showDialog('Koniec gry!', msg) == QtWidgets.QMessageBox.Yes:
                self.close()
                self.__init__()
            else:
                sys.exit()

    def close_application(self):
        # add functionality to see if we want to exit

        if self.showDialog('Wyjście', 'Na pewno chcesz wyjść?') == QtWidgets.QMessageBox.Yes:
            sys.exit()
        else:
            pass

    def about(self):
        layout = QtWidgets.QVBoxLayout()
        label = QtWidgets.QLabel("Autor: Adam Jereczek\nKółko i krzyżyk\nProjekt na Języki Skryptowe")
        layout.addWidget(label)
        dialog = QtWidgets.QDialog()
        dialog.setWindowTitle("O programie")    
        dialog.setLayout(layout)
        dialog.setFixedSize(200, 100)
        dialog.exec_()

def main(): 
    app = QtWidgets.QApplication(sys.argv)
    GUI = Tic()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()