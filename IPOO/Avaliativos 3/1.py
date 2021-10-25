#Exercício 1) (idem exercício 10 dos slides) Implemente um programa com uma função chamada
#somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre
#vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera”
#o valor de custo para incluir o imposto sobre vendas.

def somaImposto(taxaImposto,Custo):
    Custo += ((taxaImposto * 100)/Custo)
    return Custo
#############################################

taxa = float(input("Digite o valor da Taxa:"))
custo = float(input("Digite o Custo base do produto:"))

print(f"O valor do produto para venda será de R${somaImposto(taxa,custo)}")