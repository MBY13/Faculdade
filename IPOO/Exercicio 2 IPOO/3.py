#Construir um programa que leia dois números e efetue a adição. Caso o valor somado
#seja maior que 20, este deverá ser apresentado somando-se a ele mais 8; caso o valor
#somado seja menor ou igual a 20, este deverá ser apresentado subtraindo-se 5.

num1 = int(input("Digite um numero:"))
num2 = int(input("Digite um numero:"))

soma = (num1 + num2)

if soma > 20:
    soma = (soma + 8)
    print (F"A SOMA DOS NUMEROS E MAIOR QUE 10 (+8) RESULTADO = {soma}")
else:
    soma = (soma -5)
    print (F"A SOMA E MENOR QUE 10(-5) RESULTADO = {soma}")