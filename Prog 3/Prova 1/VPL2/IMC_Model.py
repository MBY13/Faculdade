import math

class Model():
    __peso=None
    __altura=None
    __imc=None
    __classif=None
    
    ## Questo 01:  (Criar o construtor da classe Model)
    def __init__(self):
        self.__peso=0
        self.__altura=0.001
        self.calcula_imc()
        
        ## Questo 02:  (Criar o mtodo set_Peso)
    def set_Peso(self, pes):
        self.__peso=pes
        
        ## Questo 03:  (Criar o mtodo set_Altura)
    def set_Altura(self, alt):
        self.__altura = alt
        
        ## Questo 04:  (Criar o mtodo get_imc)
    def get_imc(self):
        return(self.__imc)
        
        ## Questo 05:  (Criar o mtodo get_classif)
    def get_classif(self):
        return(self.__classif)
        
        ## Questo 06: (Completar o cdigo para calcular o imc e
        ##             definir a classificao de risco)
    def calcula_imc(self):
        self.__imc = self.__peso / math.pow(self.__altura, 2)
        if (self.__imc < 18.5):
            self.__classif = "Magreza"
        if ((self.__imc >= 18.5) and (self.__imc < 25.0)):
            self.__classif = "Saudvel"
        if ((self.__imc >= 25.0) and (self.__imc < 30.0)):
            self.__classif = "Sobrepeso"
        if ((self.__imc >= 30.0) and (self.__imc < 35.0)):
            self.__classif = "Obesidade Grau I"
        if ((self.__imc >= 35.0) and (self.__imc < 40.0)):
            self.__classif = "Obesidade Grau II"
        if (self.__imc >= 40.0):
            self.__classif = "Obesidade Grau III"