import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

########################################################

class Janela(QWidget):   ## (Complete o cdigo que declara a classe Janela)
    __Lb_Nome = None
    __Lb_Telefone = None
    __Lb_Email = None
    __Lb_Endereco = None
    __LEd_Nome = None
    __LEd_Telefone = None
    __LEd_Email = None
    __LEd_Endereco = None
    
    ## Questo 02:  (Criar o construtor da classe)
    
    def __init__(self, Str="Janela"):
        super().__init__()
        super().setWindowTitle(Str)
        self.setGeometry(400, 200, 480, 200)
        
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor("orange"))
        self.setPalette(p)
        
        self.inicialize()
        
    def closeEvent(self, event):
        ## Questo 03:  (Qual o comando que encerra o programa
        ##               no canto da tela)
        self.destroy()
        sys.exit(0)
        
    def inicialize(self):
        Grid=QGridLayout()
        
        ## Questo 04:  (Alocar os componentes grficos)
        
        self.__Lb_Nome = QLabel(self, text="Nome:")
        self.__Lb_Telefone = QLabel(self, text="Telefone:")
        self.__Lb_Email = QLabel(self, text="Email:")
        self.__Lb_Endereco = QLabel(self, text="Endereço:")
        
        self.__Lb_Nome.setAlignment(Qt.AlignRight)
        self.__Lb_Telefone.setAlignment(Qt.AlignRight)
        self.__Lb_Email.setAlignment(Qt.AlignRight)
        self.__Lb_Endereco.setAlignment(Qt.AlignRight)
        
        ## Questo 05:  (Pintar os componentes grficos com Palette)
        
        p1 = self.palette()
        p1.setColor(self.backgroundRole(), Qt.yellow)
        
        self.__Lb_Nome.setAutoFillBackground(True)
        self.__Lb_Nome.setPalette(p1)
        
        self.__Lb_Telefone.setAutoFillBackground(True)
        self.__Lb_Telefone.setPalette(p1)
        
        self.__Lb_Email.setAutoFillBackground(True)
        self.__Lb_Email.setPalette(p1)
        
        self.__Lb_Endereco.setAutoFillBackground(True)
        self.__Lb_Endereco.setPalette(p1)
        
        self.__LEd_Nome = QLineEdit(self, width=52)
        self.__LEd_Telefone = QLineEdit(self, width=52)
        self.__LEd_Email = QLineEdit(self, width=52)
        self.__LEd_Endereco = QLineEdit(self, width=52)
        
        ## Questo 06:  (Acrescentar na tela os componentes grficos)
        
        Grid.addWidget(self.__Lb_Nome, 0, 0)
        Grid.addWidget(self.__Lb_Telefone, 1, 0)
        Grid.addWidget(self.__Lb_Email, 2, 0)
        Grid.addWidget(self.__Lb_Endereco, 3, 0)
        
        Grid.addWidget(self.__LEd_Nome, 0, 1, 1, 1)
        Grid.addWidget(self.__LEd_Telefone, 1, 1, 1, 1)
        Grid.addWidget(self.__LEd_Email, 2, 1, 1, 1)
        Grid.addWidget(self.__LEd_Endereco, 3, 1, 1, 1)
        
        self.setLayout(Grid)
        self.show()
        
        ########################################################