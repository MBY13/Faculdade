import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui  import *  
from ThreadJogo import ThreadJogo

############################################################

class Janela(QWidget):
    __LEd1=None
    __LEd2 = None
    __LEd3 = None
    __Bt_Iniciar=None
    __Bt_Parar=None
    __Jogador1 = None
    __Jogador2 = None
    __Jogador3 = None

    def __init__(self, Str="Janela", x1=400, y1=200, dx=540, dy=180, cor="orange"):
        super().__init__() 
        self.setWindowTitle(Str)
        self.setGeometry(x1, y1, dx, dy)
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(cor))
        self.setPalette(p)
        self.inicialize()

    def closeEvent(self, event):
        print("Destruindo janela...")
        self.__Jogador1.parar()
        self.__Jogador2.parar()
        self.__Jogador3.parar()
        self.destroy()
        sys.exit(0)

    def action_iniciar(self):
        self.__Jogador1.iniciar(3000)
        self.__Jogador2.iniciar(3000)
        self.__Jogador3.iniciar(3000)

    def action_parar(self):
        self.__Jogador1.parar()
        self.__Jogador2.parar()
        self.__Jogador3.parar()

    def inicialize(self):
        Grid = QGridLayout()

        self.__LEd1=QLineEdit(width=20)
        self.__LEd2=QLineEdit(width=20)
        self.__LEd3=QLineEdit(width=20)

        self.__Jogador1 = ThreadJogo(self.__LEd1)
        self.__Jogador2 = ThreadJogo(self.__LEd2)
        self.__Jogador3 = ThreadJogo(self.__LEd3)

        self.__Bt_Iniciar=QPushButton(self, text='Iniciar')
        self.__Bt_Parar=QPushButton(self, text='Parar')

        self.__Bt_Iniciar.clicked.connect(self.action_iniciar)
        self.__Bt_Parar.clicked.connect(self.action_parar)

        Grid.addWidget(self.__Bt_Iniciar, 3, 0,1,2)
        Grid.addWidget(self.__Bt_Parar, 3,2, 1,2)

        Grid.addWidget(self.__LEd1, 0, 1,1,2)
        Grid.addWidget(self.__LEd2, 1, 1,1,2)
        Grid.addWidget(self.__LEd3, 2, 1,1,2)
        
        self.setLayout(Grid)
        self.show()

############################################################