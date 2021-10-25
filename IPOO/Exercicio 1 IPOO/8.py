print("\nDigite o custo de fabrica para que seja calculado o valor de venda")

CF = float(input("Digite o Custo de fábrica R$"))

DI = ((45*CF)/100)
A = (CF + DI)

PD = ((A*28)/100)
VV = (CF + A + PD)

print(f"\nCusto de fabrica R${CF}")
print(f"IPI(Imposto Sobre Produto) R${DI}")
print(f"Distribuidor R${PD}")
print(f"Valor de Venda R${VV}\n")