# 1. Crie a classe Imovel, que possui um endereço e 
# um preço.

# a) crie uma classe Novo, que herda Imovel e possui um 
# adicional no preço. Crie métodos de acesso e 
# impressão deste valor adicional.

# b) crie uma classe Velho, que herda Imovel e possui um 
# desconto no preço. Crie métodos de acesso e 
# impressão para este desconto.

from velho import Velho
from novo import Novo

def main():
    
    operacao = 5
    endereco = input("Digite o endereço do Imóvel:")
    valor = float(input("Digite o valor do imóvel R$:"))
    
    while True:
        operacao = int(input("OPÇÕES\n"
                            "1 - Valor do Desconto\n"
                            "2 - Valor do Acréscimo\n"
                            "0 - Para encerrar\n"
                            "DIGITE A OPÇÃO DESEJADA:"))
        
        if operacao == 1:
            desconto = float(input("Digite o valor do desconto R$"))
            imovel = Velho(endereco,valor,desconto)
            print("O valor total do imovel é R$", imovel.diminui())
            print(imovel.imprime_desconto())
            break

        elif operacao == 2:
            acrescimo = float(input("Digite o valor do Acréscimo R$"))
            imovel = Novo(endereco,valor,acrescimo)
            print("O valor total ficou de R$", imovel.aumenta())
            print(imovel.imprime_adicional())
            break 

        elif operacao == 0:
            break

        else:
            print("Digite uma opção valida")

if __name__ == '__main__':
    main()