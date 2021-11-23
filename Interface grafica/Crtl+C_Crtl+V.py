# shift + alt  + a 
import pyautogui

pyautogui.write('''import sys
from PyQt5.QtWidgets import *
from Prova_Janela import Janela

######################################################################

#Questão 11  ## (Implemente o programa principal)
App=QApplication(sys.argv)
Jan1=Janela("Proporção de Alunos por Professor")
App.exec_()

######################################################################
''', 

interval=0.01, _pause=True)