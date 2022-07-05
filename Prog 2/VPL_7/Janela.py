import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui  import * #Questo 06  ## (Complete o cdigo que realiza a
##  importao da biblioteca QtGui)
from ThreadBalde import ThreadBalde

########################################################

class Janela(QWidget): ## (Complete o cdigo que declara a classe Janela)
    __LEd1 = None
    __PBar=None
    __Bt1 = None
    __MeuBalde=None
    
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
        self.__MeuBalde.parar()
        self.destroy()
        sys.exit(0)
        
        
    def action_executar(self):
        if (self.__MeuBalde.isRunning()):
            self.__MeuBalde.parar()
            self.__Bt1.setText('Iniciar')
        else:
            self.__MeuBalde.iniciar(100)
            self.__Bt1.setText('Parar')
            
    def inicialize(self):
        Grid = QGridLayout()
        p1 = self.palette()
        p1.setColor(self.backgroundRole(), Qt.yellow)
        
        ## Questo 11:  (Alocar todos os componentes grficos)
        
        self.__LEd1=QLineEdit(width=20)
        self.__PBar = QProgressBar(self)
        self.__PBar.setOrientation(Qt.Vertical)
        self.__PBar.setMaximum(100)
        self.__PBar.setValue(0)
        
        self.__MeuBalde = ThreadBalde(self.__LEd1,self.__PBar)
        
        self.__Bt1=QPushButton()
        
        self.__Bt1.setText('Iniciar')
        
        
        ## Questo 12:  (Acrescentar na tela todos os componentes grficos)
        
        self.__Bt1.clicked.connect(self.action_executar)
        
        Grid.addWidget(self.__Bt1, 2,1,1, 1)
        
        Grid.addWidget(self.__LEd1, 1, 1,1,1)
        
        Grid.addWidget(self.__PBar, 0, 0,4,1)
        
        ## Questo 13:  (Associar o boto Bt1 ao evento que inicia e para a Thread)
        
        self.setLayout(Grid)
        self.show()
        
        ########################################################
        