from distutils.log import error
from importlib.util import set_loader
import sys
from turtle import width
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

##################################################

class View(QWidget):  ## (Complete o cdigo que declara a View)
        __Lb_peso = None
        __Lb_altura = None
        __Lb_imc = None
        __Lb_classif = None
        __LEd_peso = None
        __LEd_altura = None
        __LEd_imc = None
        __LEd_classif = None
        __Bt_calc = None
        __Cntr = None
        
        ## Questo 08:  (Criar o construtor da classe View)
        def __init__(self, Cntr, Str="Janela"):
            super().__init__()
            self.__Cntr = Cntr
            self.setWindowTitle(Str)
            self.setGeometry(300,200,320,100)
            
            self.setAutoFillBackground(True)
            p = self.palette()
            p.setColor(self.backgroundRole(), QColor('orange'))
            self.setPalette(p)
            
            self.inicialize()
        
        def closeEvent(self, event):
            print('Destruindo a janela...')
            self.destroy()
            sys.exit(0)
            
        def get_Peso(self):
            return(self.__LEd_peso.text())
            
        def get_Altura(self):
            return(self.__LEd_altura.text())
            
        def set_imc(self, imc):
            self.__LEd_imc.setText("%5.2f" % imc)
            
        def set_classif(self,classif):
            self.__LEd_classif.setText("%s" % classif)
            
        def action_Bt_calc(self):
            self.__Cntr.action_Calcular()
            
        def show_error(self, Erro):
            QMessageBox.critical(self,"Janela de Erro",Erro)
            
        def inicialize(self):
            Grid=QGridLayout()
            
            p1 = self.palette()
            p1.setColor(self.backgroundRole(), Qt.yellow)
            
            self.__Lb_peso = QLabel(self, text="Peso:", width=12)
            self.__Lb_altura = QLabel(self, text="Altura:", width=12)
            self.__Lb_imc = QLabel(self, text="IMC:", width=12)
            self.__Lb_classif = QLabel(self, text="Classificação:", width=12)
            
            self.__Lb_peso.setAlignment(Qt.AlignRight)
            self.__Lb_altura.setAlignment(Qt.AlignRight)
            self.__Lb_imc.setAlignment(Qt.AlignRight)
            self.__Lb_classif.setAlignment(Qt.AlignRight)
            
            self.__Lb_peso.setContentsMargins(4,4,4,4)
            self.__Lb_altura.setContentsMargins(4,4,4,4)
            self.__Lb_imc.setContentsMargins(4,4,4,4)
            self.__Lb_classif.setContentsMargins(4,4,4,4)
            
            self.__Lb_peso.setAutoFillBackground(True)
            self.__Lb_peso.setPalette(p1)
            
            self.__LEd_peso = QLineEdit(self,width=38)
            self.__LEd_altura = QLineEdit(self,width=38)
            self.__LEd_imc = QLineEdit(self,width=38)
            self.__LEd_classif = QLineEdit(self,width=38)
            
            
            self.__Bt_calc=QPushButton(self, text='Calcular')
            self.__Bt_calc.clicked.connect(self.action_Bt_calc)
            ## Questo 17:  (Conectar o boto Bt_adic ao evento que realiza
            ##              o clculo do imc e define a classificao de risco)
            
            ############# Grid #############
            ## Questo 18:  (Acrescentar os componentes grficos na Tela)
            
            Grid.addWidget(self.__Lb_peso,0,0)
            Grid.addWidget(self.__Lb_altura,1,0)
            
            Grid.addWidget(self.__LEd_peso,0,1)
            Grid.addWidget(self.__LEd_altura,1,1)
            
            Grid.addWidget(self.__Bt_calc,2,0)
            
            Grid.addWidget(self.__Lb_imc,3,0)
            Grid.addWidget(self.__LEd_imc,3,1)
            
            Grid.addWidget(self.__Lb_classif,4,0)
            Grid.addWidget(self.__LEd_classif,4,1)
            
            self.setLayout(Grid)
            self.show()
            
            ##################################################
            
            