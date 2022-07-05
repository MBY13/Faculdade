import sys
from PyQt5.QtWidgets import *
from Janela import Janela

########################################################

## Questo 14:  (Criar o programa principal que deve conter um objeto da
##               classe Janela e mostr-lo na tela)
App=QApplication(sys.argv)
Jan1=Janela("Balde")
App.exec_()

########################################################
