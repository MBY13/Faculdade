import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

######################################################################

class Janela(QWidget): ## (Complete o código que declara a classe)
    __Lb_escolaTitulo=None
    __Lb_alunos=None
    __Lb_professores=None
    __Lb_aluProf=None

    __Lb_escola=[]
    __LEd_alunos=[]
    __LEd_professores=[]
    __LEd_aluProf=[]

    __LEd_maior=None
    __Bt_calc=None

    #  Questão 02  ## (Criar o construtor da classe)
    def __init__(self, Str="Janela"):
        super().__init__()
        super().setWindowTitle(Str)
        super().setGeometry(400, 200, 480, 200)
        
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor("orange"))
        self.setPalette(p)
        
        self.inicialize()

    def calcula_proporcao(self):
        #  Questão 03  ## (Criar o evento que calcula a proporção
                     ## de alunos por professor em cada escola)
        try:
            n1 = len(self.__LEd_alunos)
            for i in range(0,n1,1):
                val1=float(self.__LEd_alunos[i].text())
                val2=float(self.__LEd_professores[i].text())
                total=val1/val2
                self.__LEd_aluProf[i].setText("%4.2f" % total)
        except ValueError as ex:
            QMessageBox.critical(self, "Janela de Erro",
            "Erro: Favor digitar valores numricos.(%s)" % ex)
            print("Erro fatal: Erro inexperado. (%s)" % ex)
        except Exception as ve:
            QMessageBox.critical(self, "Janela de Erro",
            "Erro: Favor digitar valores numricos.(%s)" % ve)
            print("Erro fatal: Erro inexperado. (%s)" % ve)


    def acha_maior(self):
        #  Questão 04  ## (Criar o evento que identifica qual o
                     ## colégio onde há a maior proporção de alunos por professor)
        try:
            max=0
            n1 = len(self.__LEd_aluProf)
            for i in range(0, n1, 1):
                val=float(self.__LEd_aluProf[i].text())
                if  (max < val):
                    max=val
                    ii=i
            self.__LEd_maior.setText(self.__Lb_escola[ii].text())
        except ValueError as ve:
            QMessageBox.critical (self, "Janela de Erro",
            "Erro: Favor digitar valores numricos.(%s)" % ve)
            print("Erro: Favor digitar valores numericos.(%s)"% ve)
        except Exception as ex:
            QMessageBox.critical (self, "Janela de Erro",
            "Erro fatal: Erro inexperado.(%s)" % ex)
            print("Erro fatal: Erro inexperado.(%s)"% ex)    

    def closeEvent(self, event):
        #  Questão 05  ## (Qual o comando que encerra o programa
                     ## no canto da tela?)
        self.destroy()
        sys.exit(0)

    def action_Bt_calc(self):
        #  Questão 06  ## (Chamar os eventos que fazem os cálculos
                     ## citados em 03, 04)
        self.calcula_proporcao()
        self.acha_maior()

    def inicialize(self):
        Grid=QGridLayout()

        p1 = self.palette()
        p1.setColor(self.backgroundRole(), Qt.yellow)

        #  Questão 07  ## (Alocar os componentes gráficos)
        self.__Lb_escolaTitulo=QLabel(self, text="N. Escola")
        self.__Lb_alunos=QLabel(self, text="Aluno")
        self.__Lb_professores=QLabel(self, text="Professores")
        self.__Lb_aluProf=QLabel(self, text="Alunos/Prof.")
        
        self.__Lb_escolaTitulo.setAlignment(Qt.AlignLeft)
        self.__Lb_alunos.setAlignment(Qt.AlignLeft)
        self.__Lb_professores.setAlignment(Qt.AlignLeft)
        self.__Lb_aluProf.setAlignment(Qt.AlignLeft)

        #  Questão 08  ## (Pintar os componentes gráficos com Palette)
        self.__Lb_escolaTitulo.setAutoFillBackground(True)
        self.__Lb_escolaTitulo.setPalette(p1)

        self.__Lb_alunos.setAutoFillBackground(True)
        self.__Lb_alunos.setPalette(p1)

        self.__Lb_professores.setAutoFillBackground(True)
        self.__Lb_professores.setPalette(p1)
        
        self.__Lb_aluProf.setAutoFillBackground(True)
        self.__Lb_aluProf.setPalette(p1)

        Escolas = ['01 Global', '02 Bom Jesus', '03 Floebl', '04 Celso Ramos', '05 Henrique Schwarz', '06 Orestes Guimarães' , '07 Carlos Zieperer', '08 João Ropelatto', '09 Espaço Infantil']

        n1=len(Escolas)
        for i in range(0, n1, 1):
            Lb = QLabel(self, text=Escolas[i])
            Lb.setAlignment(Qt.AlignLeft)
            Lb.setAutoFillBackground(True)
            Lb.setPalette(p1)
            self.__Lb_escola.append(Lb)
            
            LEd = QLineEdit(self, width=52)
            self.__LEd_alunos.append(LEd)
            
            LEd = QLineEdit(self, width=52)
            self.__LEd_professores.append(LEd)
            
            LEd = QLineEdit(self, width=52)
            self.__LEd_aluProf.append(LEd)

        #  Questão 09  ## (Associar o botão Bt_calc ao evento da questão 06)

        self.__Bt_calc=QPushButton(self, text='Calcular')
        self.__Bt_calc.clicked.connect(self.action_Bt_calc)
        
        self.__LEd_maior = QLineEdit(self,width=52)

        #  Questão 10  ## (Acrescentar na tela os componentes gráficos)
        Grid.addWidget(self.__Lb_escolaTitulo, 0, 0)
        Grid.addWidget(self.__Lb_alunos, 0, 1)
        Grid.addWidget(self.__Lb_professores, 0, 2)
        Grid.addWidget(self.__Lb_aluProf, 0, 3)
        
        n1=len(self.__Lb_escola)
        for i in range(0, n1, 1):
            Grid.addWidget(self.__Lb_escola[i], i+1, 0)
            Grid.addWidget(self.__LEd_alunos[i], i+1, 1)
            Grid.addWidget(self.__LEd_professores[i], i+1, 2)
            Grid.addWidget(self.__LEd_aluProf[i], i+1, 3)
            
        Grid.addWidget(self.__Bt_calc, n1+1, 1)
        Grid.addWidget(self.__LEd_maior, n1+1, 2)

        self.setLayout(Grid)
        self.show()

######################################################################