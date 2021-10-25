#Em épocas de pouco dinheiro, os comerciantes estão procurando aumentar suas vendas oferecendo desconto. Faça um
#programa que possa receber um valor de um produto e um valor de desconto. Calcule e imprima o novo valor do produto.

print  ("\n Abaixo entre com o Valor Bruto dos produtos e o Desconto (%) para que aparecera o Valor Liquido \n")

VB = float(input("Digite o Valor Bruto R$"))
Des = float(input("Digite a porcentagem do desconto(%):"))

Des = float((VB * Des)/100)
VL = float(VB - Des)

print (f"Valor do Descont R$ {Des}")
print ("O Valor Liquido é R$", VL )