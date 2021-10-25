#Escreva um programa que leia dois números e que pergunte qual operação o usuário
#deseja realizar. Deve-se poder calcular a soma (+), subtração (-), multiplicação (*) e
#divisão (/). Exiba o resultado da operação solicitada.

num1 = float(input("Digite primeiro numero:"))
num2 = float(input("Digite segundo numero:"))
op = input("Digite a operação desejada(+,-,*,/):")

if op == "+":
    soma = round((num1 + num2),3)
    print (f"{soma}")
elif op == "-":
    soma = round((num1 - num2),3)
    print (f"{soma}")
elif op == "*":
    soma = round((num1 * num2),3)
    print (f"{soma}")
elif op == "/":
    soma = round((num1 / num2),3)
    print (f"{soma}")
else:
    print ("operação digitada invalida")