from imovel import Imovel

class Velho (Imovel):
    def __init__(self, endereco, valor,desconto):
        super().__init__(endereco, valor)
        self.__Desconto = desconto
    
    def get_desconto(self):
        return self.__Desconto
    def set_desconto(self,desconto):
        self.__Desconto = desconto
    def imprime_desconto(self):
        print (f"Valor do desconto é {self.__Desconto}")

    def diminui(self):
        return super().get_valor() - self.__Desconto