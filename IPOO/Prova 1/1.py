#Implementar um programa em Python que leia o valor de um produto (float), 
# a quantidade de produtos comprados (int) e 
#informe o valor a ser pago com desconto conforme a quantidade comprada:
#até 5 unidades: 3% de desconto
#até 10 unidades: 5% de desconto
#acima de 10 unidades: 7% de desconto

quant = int(input("Digite quantos produtos foram comprados:"))
valor = float(input("Digite o valor do produto R$"))

if quant <= 5 : 
    desconto = (((valor*quant)*3)/100) 
    vb = (valor*quant) - desconto 

    print ("Foi comprado", quant, "produtos" )
    print ("O valor total ficara de R$", vb)
elif quant <= 10:
    desconto = (((valor*quant)*5)/100) 
    vb = (valor*quant) - desconto 

    print ("Foi comprado", quant, "produtos" )
    print ("O valor total ficara de R$", vb)
elif quant > 10:
    desconto = (((valor*quant)*7)/100) 
    vb = (valor*quant) - desconto 

    print ("Foi comprado", quant, "produtos" )
    print ("O valor total ficara de R$", vb)