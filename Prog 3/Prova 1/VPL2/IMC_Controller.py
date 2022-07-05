from IMC_Model import Model
from IMC_View import View

##################################################

class Controller():
    __model = None
    __view = None
    
    def __init__(self):
        self.start()
        
    def start(self):
        self.__model = Model()
        self.__view = View(self,"Calculadora IMC")
        
    def action_Calcular(self):
        str1 = self.__view.get_Peso()
        str2 = self.__view.get_Altura()
        
        try:
            peso = float(str1)
            altura = float(str2)
            
            self.__model.set__Peso(peso)
            self.__model.set_Altura(altura)
            self.__model.calcula_imc()
            
            self.__view.set_imc(self.__model.get_imc())
            self.__view.set_classif(self.__model.get_classif())
        except ValueError as ve:
            Erro = "Erro Favor digitar valores numricos. (%s)" % ve
            self.__view.show_error(Erro)
            print(Erro)
        except ZeroDivisionError as zde:
            Erro = "Erro: Diviso por zero.(%s)" % zde
            self.__view.show_error(Erro)
            print(Erro)
        except Exception as ex:
            Erro = "Erro Fatal: Erro inexperado. (%s)" % ex
            self.__view.show_error(Erro)
            print(Erro)
            
            ##################################################
            