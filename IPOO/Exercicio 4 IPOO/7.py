#Escrever um programa que leia 5 números float e imprima-os
#em ordem inversa. 

V= []
x=0

while x < 5:
    V.append(float(input("Digite um numero:")))
    x+=1
print ("\n")

x = 4

while x >=0:
    print(V[x], end= " ")
    x -= 1
print ("\n")