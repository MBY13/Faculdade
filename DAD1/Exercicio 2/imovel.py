class Imovel :
    def __init__(self,endereco,valor) :
        self.__Endereco = endereco
        self.__Valor = valor 

    def get_endereco(self):
        return self.__Endereco
    def set_endereco(self,endereco):
        self.__Endereco = endereco

    def get_valor(self):
        return self.__Valor
    def set_valor(self,valor):
        self.__Valor = valor