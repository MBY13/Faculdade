import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui  import * #Questo 06  ## (Complete o cdigo que realiza a
##  importao da biblioteca QtGui)
from ThreadClock import ThreadClock

########################################################

class Janela(QWidget): ## (Complete o cdigo que declara a classe Janela)
    __Lb1 = None
    __LEd1 = None
    __Bt1 = None
    __MeuRelogio=None
    
    ## Questo 08:  (Criar o construtor da classe Janela)
    def __init__(self, Str="Janela", x1=400, y1=200, dx=640, dy=480, cor="orange"):
        super().__init__() 
        self.setWindowTitle(Str)
        self.setGeometry(x1, y1, dx, dy)
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(cor))
        self.setPalette(p)
        
        self.inicialize()
        
    def closeEvent(self, event):
        ## Questo 09:  (Criar o cdigo para encerrar o programa clicando no
        ##               cone do canto superior direito da janela)
        print("Destruindo janela...")
        self.__MeuRelogio.parar()
        self.destroy()
        sys.exit(0)
        
        
    def action_executar(self):
        if (self.__MeuRelogio.isRunning()):
            self.__MeuRelogio.parar()
            self.__Bt1.setText("Iniciar")
        else:
            self.__MeuRelogio.iniciar(3000)
            self.__Bt1.setText("Parar")
            
    def inicialize(self):
        Grid = QGridLayout()
        p1 = self.palette()
        p1.setColor(self.backgroundRole(), Qt.yellow)
        
        ## Questo 11:  (Alocar todos os componentes grficos)
        
        self.__LEd1=QLineEdit()
        
        self.__MeuRelogio = ThreadClock(self.__LEd1)
        
        self.__Bt1=QPushButton(text='Iniciar')
        
        self.__Lb1 = QLabel(self, text="Hora:")
        
        self.__Lb1.setAutoFillBackground(True)
        self.__Lb1.setPalette(p1)
        ## Questo 12:  (Acrescentar na tela todos os componentes grficos)
        
        self.__Bt1.clicked.connect(self.action_executar)
        
        Grid.addWidget(self.__Bt1, 1, 1)
        
        Grid.addWidget(self.__LEd1, 0, 1,1,2)
        
        Grid.addWidget(self.__Lb1, 0, 0)
        
        ## Questo 13:  (Associar o boto Bt1 ao evento que inicia e para a Thread)
        
        self.setLayout(Grid)
        self.show()
        
        ########################################################
