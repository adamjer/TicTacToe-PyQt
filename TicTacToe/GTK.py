#-*- coding: utf-8 -*-

import gtk

class Tic(gtk.Window):

    def __init__(self):
        gtk.Window.__init__(self)

        #self.button = gtk.Button(label="Click Here")
        self.set_title("Kółko i krzyżyk")
        self.set_size_request(360, 410)
        #self.button.connect("clicked", self.on_button_clicked)
        #self.add(self.button)

        self.player = ''
        self.winner = ''
        self.taken = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.takenBy = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.board()

    def on_button_clicked(self, widget):
        print("Hello World")

    def setBoard(self):
        # set up game board
        self.btn0 = gtk.Button()
        self.btn0.connect("clicked", self.clicked(0))  
        self.btn0.resize(100,100)
        self.btn0.move(20,280)
        self.add(self.btn0)

        self.btn1 = gtk.Button()
        self.btn1.connect("clicked", self.clicked(1))  
        self.btn1.resize(100,100)
        self.btn1.move(130,280)
        self.add(self.btn1)

        self.btn2 = gtk.Button()
        self.btn2.connect("clicked", self.clicked(2))  
        self.btn2.resize(100,100)
        self.btn2.move(240,280)
        self.add(self.btn2)

        self.btn3 = gtk.Button()
        self.btn3.connect("clicked", self.clicked(3))  
        self.btn3.resize(100,100)
        self.btn3.move(20,170)
        self.add(self.btn3)

        self.btn4 = gtk.Button()
        self.btn4.connect("clicked", self.clicked(4))  
        self.btn4.resize(100,100)
        self.btn4.move(130,170)
        self.add(self.btn4)

        self.btn5 = gtk.Button()
        self.btn5.connect("clicked", self.clicked(5))  
        self.btn5.resize(100,100)
        self.btn5.move(240,170)
        self.add(self.btn5)

        self.btn6 = gtk.Button()
        self.btn6.connect("clicked", self.clicked(6))  
        self.btn6.resize(100,100)
        self.btn6.move(20,60)
        self.add(self.btn6)

        self.btn7 = gtk.Button()
        self.btn7.connect("clicked", self.clicked(7))  
        self.btn7.resize(100,100)
        self.btn7.move(130,60)
        self.add(self.btn7)

        self.btn8 = gtk.Button()
        self.btn8.connect("clicked", self.clicked(8))  
        self.btn8.resize(100,100)
        self.btn8.move(240,60)
        self.add(self.btn8)

    def board(self):
        '''
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
        '''
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
        self.show_all()

    def change_player(self):
        if self.player == 'X':
            self.player = 'O'
        else:
            self.player = 'X'

    def clicked(self, btnval):
        if self.taken[btnval] == 0:
            # update free moves & the screen
            #self.btnDict[btnval](self.player)
            self.taken[btnval] = 1
            # update who-owns-what to check if there's a winner
            if self.player == 'X':
                self.takenBy[btnval] = 'X'
            else:
                self.takenBy[btnval] = 'O'
            print(self.takenBy)
            #self.test_for_winner()
            self.change_player()
            self.show()
        else:
            pass

def main(): 
    GUI = Tic()
    GUI.connect("destroy", gtk.main_quit)
    GUI.show_all()
    gtk.main()

if __name__ == '__main__':
    main()
