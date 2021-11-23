import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

##################################################

class Janela(QWidget): ## Questo 01: (Complete o cdigo que declara a classe)
    __Lb_valor1=None
    __Lb_valor2=None
    __Lb_result=None
    __LEd_valor1=None
    __LEd_valor2=None
    __LEd_result=None
    __Bt_adic=None
    __Bt_sub=None
    __Bt_mult=None
    __Bt_div=None
    
    ## Questo 02: (Criar o construtor da classe Janela)
    def __init__(self, Str="Janela"):
        super().__init__()
        super().setWindowTitle(Str)
        self.setGeometry(480, 200, 380, 200)
        
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor("orange"))
        self.setPalette(p)
        
        self.inicialize()
        
    def closeEvent(self, event):
        ## Questo 03: (Qual o cdigo necessrio para encerrar o programa no canto
        ##             superior direito da janela)
        self.destroy()
        sys.exit(0)
        
    def action_Bt_adic(self):
        try:
            ## Questo 04: (Criar o evento que calcula a adio dos valores numricos)
            n1 = float(self.__LEd_valor1.text().replace(',', '.'))
            n2 = float(self.__LEd_valor2.text().replace(',', '.'))
            total = n1 + n2 
            self.__LEd_result.setText("%04.2f" % total)
        except ValueError as ve:
            ## Primeira soluo
            QMessageBox.critical(None, "Janela de Erro #1", "Voce deve digitar valores numricos")
            ## Segunda soluo
            QMessageBox.critical(self, "Janela de Erro #2", "Voce deve digitar valores numricos")
            ## Terceira soluo
            print(self, "Janela de Erro #3", "Erro de digitao___________    ___________", "Voce deve digitar valores numricos",
            "Erro1: Voce deve digitar valores numricos: %s" % ve)
            print("Erro1: Voce deve digitar valores numricos: %s" % ve)
        except Exception as ex:
            print(self, "Janela de Erro", "Erro fatal", "Verifique nos detalhes o que ocorreu",
            "Erro2: Erro inexperado: %s" % ex)
            print("Erro2: Erro inexperado: %s" % ex)
                
    def action_Bt_sub(self):
        try:
            ## Questo 05: (Criar o evento que calcula a subtrao dos valores numricos)
            n1 = float(self.__LEd_valor1.text().replace(',', '.'))
            n2 = float(self.__LEd_valor2.text().replace(',', '.'))
            total = n1 - n2 
            self.__LEd_result.setText("%04.2f" % total)
        except ValueError as ve:
            ## Primeira soluo
            QMessageBox.critical(None, "Janela de Erro #1", "Voce deve digitar valores numricos")
            ## Segunda soluo
            QMessageBox.critical(self, "Janela de Erro #2", "Voce deve digitar valores numricos")
            ## Terceira soluo
            print(self, "Janela de Erro #3", "Erro de digitao___________    ___________", "Voce deve digitar valores numricos",
            "Erro1: Voce deve digitar valores numricos: %s" % ve)
            print("Erro1: Voce deve digitar valores numricos: %s" % ve)
        except Exception as ex:
            print(self, "Janela de Erro", "Erro fatal", "Verifique nos detalhes o que ocorreu",
                "Erro2: Erro inexperado: %s" % ex)
            print("Erro2: Erro inexperado: %s" % ex)
                            
    def action_Bt_mult(self):
        try:
            ## Questo 06: (Criar o evento que calcula a multiplicao dos valores numricos)
            n1 = float(self.__LEd_valor1.text().replace(',', '.'))
            n2 = float(self.__LEd_valor2.text().replace(',', '.'))
            total = n1 * n2 
            self.__LEd_result.setText("%04.2f" % total)
        except ValueError as ve:
            ## Primeira soluo
            QMessageBox.critical(None, "Janela de Erro #1", "Voce deve digitar valores numricos")
            ## Segunda soluo
            QMessageBox.critical(self, "Janela de Erro #2", "Voce deve digitar valores numricos")
            ## Terceira soluo
            print(self, "Janela de Erro #3", "Erro de digitao___________    ___________", "Voce deve digitar valores numricos",
            "Erro1: Voce deve digitar valores numricos: %s" % ve)
            print("Erro1: Voce deve digitar valores numricos: %s" % ve)
        except Exception as ex:
            print(self, "Janela de Erro", "Erro fatal", "Verifique nos detalhes o que ocorreu",
            "Erro2: Erro inexperado: %s" % ex)
            print("Erro2: Erro inexperado: %s" % ex)
                    
    def action_Bt_div(self):
        try:
            ## Questo 07: (Criar o evento que calcula a diviso dos valores numricos)
            n1 = float(self.__LEd_valor1.text().replace(',', '.'))
            n2 = float(self.__LEd_valor2.text().replace(',', '.'))
            total = n1 / n2 
            self.__LEd_result.setText("%5.2f" % total)
        except ValueError as ve:
            ## Primeira soluo
            QMessageBox.critical(None, "janela de Erro #1", "Voce deve digitar valores numricos")
            ## Segunda soluo
            QMessageBox.critical(self, "Janela de Erro #2", "Voce deve digitar valores numricos")
            ## Terceira soluo
            print(self, "Janela de Erro #3", "Erro de digitao___________    ___________", "Voce deve digitar valores numricos",
            "Erro1: Voce deve digitar valores numricos: %s" % ve)
            print("Erro1: Voce deve digitar valores numricos: %s" % ve)
        except Exception as ex:
            print(self, "Janela de Erro", "Erro fatal", "Verifique nos detalhes o que ocorreu",
            "Erro2: Erro inexperado: %s" % ex)
            print("Erro2: Erro inexperado: %s" % ex)
                        
    def inicialize(self):
        Grid=QGridLayout()
        
        ## Questo 08: Realize a alocao dos componentes grficos)
        self.__Lb_valor1= QLabel(self, text="Valor1:")
        self.__Lb_valor2=QLabel(self, text="Valor2:")
        self.__Lb_result=QLabel(self, text="Resultado:")
        
        self.__Lb_valor1.setAlignment(Qt.AlignRight)
        self.__Lb_valor2.setAlignment(Qt.AlignRight)
        self.__Lb_result.setAlignment(Qt.AlignRight)
        
        p1 = self.palette()
        p1.setColor(self.backgroundRole(), Qt.yellow)
        
        self.__Lb_valor1.setAutoFillBackground(True)
        self.__Lb_valor1.setPalette(p1)
        
        self.__Lb_valor2.setAutoFillBackground(True)
        self.__Lb_valor2.setPalette(p1)
        
        self.__Lb_result.setAutoFillBackground(True)
        self.__Lb_result.setPalette(p1)
        
        self.__LEd_valor1=QLineEdit(self, width=52)
        self.__LEd_valor2=QLineEdit(self, width=52)
        self.__LEd_result=QLineEdit(self, width=52)
        
        self.__Bt_adic=QPushButton(self, text='Add')
        self.__Bt_adic.clicked.connect(self.action_Bt_adic)
        ## Questo 09: (Conectar o boto Bt_adic ao evento que realiza
        ##              a adio dos valores numricos)
        
        self.__Bt_sub=QPushButton(self, text='Sub')
        self.__Bt_sub.clicked.connect(self.action_Bt_sub)
        ## Questo 10: (Conectar o boto Bt_sub ao evento que realiza
        ##              a subtrao dos valores numricos)
        
        self.__Bt_mult=QPushButton(self, text='Mult')
        self.__Bt_mult.clicked.connect(self.action_Bt_mult)
        ## Questo 11: (Conectar o boto Bt_mult ao evento que realiza
        ##              a multiplicao dos valores numricos)
        
        self.__Bt_div=QPushButton(self, text='Div')
        self.__Bt_div.clicked.connect(self.action_Bt_div)
        ## Questo 12: (Conectar o boto Bt_div ao evento que realiza
        ##              a diviso dos valores numricos)
        
        ############# Grid #############
        ## Questo 13: (Acrescentar os componentes grficos na Tela) 
        Grid.addWidget(self.__Lb_valor1, 0, 0)
        Grid.addWidget(self.__Lb_valor2, 1, 0)
        Grid.addWidget(self.__Lb_result, 3, 0)
        Grid.addWidget(self.__Bt_adic, 2, 1)
        Grid.addWidget(self.__Bt_sub, 2, 2)
        Grid.addWidget(self.__Bt_mult, 2, 3)
        Grid.addWidget(self.__Bt_div, 2, 4)
        
        Grid.addWidget(self.__LEd_valor1, 0, 1, 1, 4)
        Grid.addWidget(self.__LEd_valor2, 1, 1, 1, 4)
        Grid.addWidget(self.__LEd_result, 3, 1, 1, 4)
        
        self.setLayout(Grid)
        self.show()
        
        ##################################################
                                                                            