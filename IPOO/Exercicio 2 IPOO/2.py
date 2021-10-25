#Construir um programa que leia dois valores numéricos inteiros e efetue a adição, caso
# o resultado seja maior que 10, apresentá-lo

num1 = int(input("Digite um numero:"))
num2 = int(input("Digite um numero:"))

soma = (num1 + num2)

if soma > 10:
    print (F"A SOMA DOS NUMEROS E MAIOR QUE 10   {soma}")
else:
    print (F"A SOMA E MENOR QUE 10 ")