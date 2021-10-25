print("\n insira os valores para que seja descoberto o valor de venda \n")

VC = float(input("Digite o valor pago pelo produto R$"))
T = float(input("Digite A procentagem de lucro sobre o produto:"))

AC = ((VC * T)/100)
VV = (AC + VC)

print(f"\nVocê terá um lucro de R${AC} e vendera o item por R${VV}\n")