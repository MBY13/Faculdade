class imovel:
    _endereco = None 

    def __init__(self):
        self._endereco = input("Digite o endereço do imóvel:")
        self._Valor = float(input("Digite o valor do aluguel R$"))

    def getEndereco(self):
        return self._endereco

    def getValor(self):
        return self._Valor 

class Apartamento(imovel):
    __andar = None
    __TaxaCondominio = None 
    valorM = None 
    
    def __init__(self):
        imovel.__init__(self)
        self.__andar = int(input("Digite o andar do apartamento:"))
        self.__TaxaCondominio = float(input("Digite a taxa do condominio R$"))
        
    def valorMensal(self):
        self.valorM =  super().getValor() + self.__TaxaCondominio 
        return self.valorM

    def getAndar(self):
        return self.__andar
###########################################
cont = 1
cont2 = 0
quant= int(input("Digite quantos apartamentos deseja cadastrar:"))
end = []
anda = []
vm = []

while cont <= quant:
    print(f"DADOS DO {cont}º IMÓVEL")
    ap = Apartamento()
    a = ap.getAndar()
    b = ap.valorMensal()
    if a >= 2:
        if b <= 1000:
            end.append (ap.getEndereco())
            anda.append (ap.getAndar())
            vm.append (ap.valorMensal())
            cont2 +=1
    cont += 1

cont = 0  

print("LISTAGEM DOS AP ACIMA DO 2º E COM VALOR ATÉ R$1000,00")
while cont < cont2:
    print("=========="*10)
    print ("ENDEREÇO:",end[cont])
    print("ANDAR:",anda[cont])
    print("VALOR MENSAL R$",vm[cont])
    print("=========="*10)
    cont +=1 