import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui  import * #Questo 06  ## (Complete o cdigo que realiza a
##  importao da biblioteca QtGui)
from ThreadSchlacht import ThreadSchlacht

##################################################

class Janela(QWidget):  ## (Complete o cdigo que declara a classe Janela)
    __LEd1 = None
    __LEd2 = None
    __LEd3 = None
    __Bt_Abertura=None
    __Bt_Fechamento=None
    __Barraca1 = None
    __Barraca2 = None
    __Barraca3 = None

## Questo 07:  (Criar o construtor da classe Janela)
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
        self.__Barraca1.parar()
        self.__Barraca2.parar()
        self.__Barraca3.parar()
        self.destroy()
        sys.exit(0)
        
    def action_abertura(self):
        self.__Barraca1.iniciar(3000)
        self.__Barraca2.iniciar(3000)
        self.__Barraca3.iniciar(3000)
        
    def action_fechamento(self):
        self.__Barraca1.parar()
        self.__Barraca2.parar()
        self.__Barraca3.parar()
        
    def inicialize(self):
        Grid = QGridLayout()
        
        self.__LEd1=QLineEdit(width=20)
        self.__LEd2=QLineEdit(width=20)
        self.__LEd3=QLineEdit(width=20)
        
        self.__Barraca1 = ThreadSchlacht(self.__LEd1)
        self.__Barraca2 = ThreadSchlacht(self.__LEd2)
        self.__Barraca3 = ThreadSchlacht(self.__LEd3)
        
        self.__Bt_Abertura=QPushButton(self, text='Abertura')
        self.__Bt_Fechamento=QPushButton(self, text='Fechamento')
        
        self.__Bt_Abertura.clicked.connect(self.action_abertura)
        self.__Bt_Fechamento.clicked.connect(self.action_fechamento)
        
        Grid.addWidget(self.__Bt_Abertura, 3, 0,1,2)
        Grid.addWidget(self.__Bt_Fechamento, 3,2, 1,2)
        
        Grid.addWidget(self.__LEd1, 0, 1,1,2)
        Grid.addWidget(self.__LEd2, 1, 1,1,2)
        Grid.addWidget(self.__LEd3, 2, 1,1,2)
        
        self.setLayout(Grid)
        self.show()
        
        
        ##################################################