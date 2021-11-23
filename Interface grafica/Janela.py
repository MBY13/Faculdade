import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from MyMessageBox import MyMessageBox

##################################################

class Janela(QWidget):
    __LEd_Nota1=None
    __LEd_Nota2=None
    __LEd_Nota3=None
    __LEd_Media=None

    def __init__(self, Str="Janela", x1=0, y1=0, dx=640, dy=480, cor="lightgray"):
        super().__init__()
        super().setWindowTitle(Str)
        self.setGeometry(x1, y1, dx, dy)

        # Set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(cor))
        self.setPalette(p)

        self.inicialize()

    def action_Bt_Calc(self):
        try:
            n1=float(self.__LEd_Nota1.text().replace(',', '.'))
            n2=float(self.__LEd_Nota2.text().replace(',', '.'))
            n3=float(self.__LEd_Nota3.text().replace(',', '.'))
            total=(n1+n2+n3)/3
            self.__LEd_Media.setText(("%04.1f" % total).replace('.', ','))
        except ValueError as ve:
            ## Primeira solução
            QMessageBox.critical(None, "Janela de Erro #1", "Voce deve digitar valores numéricos")
            ## Segunda solução
            QMessageBox.critical(self, "Janela de Erro #2", "Voce deve digitar valores numéricos")
            ## Terceira solução
            MyMessageBox(self, "Janela de Erro #3", "Erro de digitação___________\t___________", "Voce deve digitar valores numéricos",
                         "Erro1: Voce deve digitar valores numéricos: \n\n%s" % ve)
            print("Erro1: Voce deve digitar valores numéricos: \n\n%s" % ve)
        except Exception as ex:
            MyMessageBox(self, "Janela de Erro", "Erro fatal", "Verifique nos detalhes o que ocorreu",
                         "Erro2: Erro inexperado: \n\n%s" % ex)
            print("Erro2: Erro inexperado: \n\n%s" % ex)

    def closeEvent(self, event):
        print("Destruindo janela...")
        self.destroy()
        sys.exit(0)

    def inicialize(self):
        Grid = QGridLayout()

        Lb_Nome=QLabel(self, text="Nome=")
        Lb_Sexo=QLabel(self, text="Sexo=")
        Lb_Nota1=QLabel(self, text="Nota1=")
        Lb_Nota2=QLabel(self, text="Nota2=")
        Lb_Nota3=QLabel(self, text="Nota3=")
        Lb_Media=QLabel(self, text="Media=")

        Lb_Nome.setAlignment(Qt.AlignRight)
        Lb_Sexo.setAlignment(Qt.AlignRight)
        Lb_Nota1.setAlignment(Qt.AlignRight)
        Lb_Nota2.setAlignment(Qt.AlignRight)
        Lb_Nota3.setAlignment(Qt.AlignRight)
        Lb_Media.setAlignment(Qt.AlignRight)

        p1 = self.palette()
        p1.setColor(self.backgroundRole(), Qt.yellow)

        Lb_Nome.setAutoFillBackground(True)
        Lb_Nome.setPalette(p1)

        Lb_Sexo.setAutoFillBackground(True)
        Lb_Sexo.setPalette(p1)

        Lb_Nota1.setAutoFillBackground(True)
        Lb_Nota1.setPalette(p1)

        Lb_Nota2.setAutoFillBackground(True)
        Lb_Nota2.setPalette(p1)

        Lb_Nota3.setAutoFillBackground(True)
        Lb_Nota3.setPalette(p1)

        Lb_Media.setAutoFillBackground(True)
        Lb_Media.setPalette(p1)

        LEd_Nome=QLineEdit(self, width=52) ## opção desconhecida height=12, exceto com layout Place
        self.__LEd_Nota1=QLineEdit(self, width=52)
        self.__LEd_Nota2=QLineEdit(self, width=52)
        self.__LEd_Nota3=QLineEdit(self, width=52)
        self.__LEd_Media=QLineEdit(self, width=52)

        CB_Sexo = QComboBox(self, height=60, width=80)
        CB_Sexo.addItem("Escolha o sexo")
        CB_Sexo.addItem("Masculino")
        CB_Sexo.addItem("Feminino")

        Bt_Calc=QPushButton(self, text='Calcular')
        Bt_Calc.clicked.connect(self.action_Bt_Calc)

        Grid.addWidget(Lb_Nome, 0, 0)
        Grid.addWidget(Lb_Sexo, 1, 0)
        Grid.addWidget(Lb_Nota1, 2, 0)
        Grid.addWidget(Lb_Nota2, 3, 0)
        Grid.addWidget(Lb_Nota3, 4, 0)
        Grid.addWidget(Lb_Media, 5, 0)
        Grid.addWidget(Bt_Calc, 6, 1)

        Grid.addWidget(LEd_Nome, 0, 1, 1, 2)
        Grid.addWidget(CB_Sexo, 1, 1, 1, 2)
        Grid.addWidget(self.__LEd_Nota1, 2, 1, 1, 2)
        Grid.addWidget(self.__LEd_Nota2, 3, 1, 1, 2)
        Grid.addWidget(self.__LEd_Nota3, 4, 1, 1, 2)
        Grid.addWidget(self.__LEd_Media, 5, 1, 1, 2)

        self.setLayout(Grid)
        self.show()

##################################################
