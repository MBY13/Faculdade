#Ler um número inteiro de 3 dígitos, e imprimir se o algarismo da casa das centenas é
#par ou ímpar.

num = int(input("Digite um numero com 3 digitos:"))

if num <=999 and num > 99:
    if (num % 2)==0:
        print("O numero digitado é par")
    else:
        print("O numero digitado é impar")
else:
    print("o numero digitado não tem 3 digitos")