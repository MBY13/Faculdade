from imovel import Imovel

class Novo(Imovel):
    def __init__(self, endereco, valor,adicional):
        super().__init__(endereco, valor)
        self.__Adicional = adicional
        self.__Valor += self.__Adicional

    def get_adicional(self):
        return self.__Adicional
    def set_adicional(self,adicional):
        self.__Adicional = adicional
    def imprime_adicional(self):
        print (f"Valor do acréscimo é R${self.__Adicional}")

    def aumenta(self):
        return super().get_valor() + self.__Adicional