#Faça um programa para imprimir o menor elemento de uma lista.

from random import randint
L = []
x=0
i = 100

while x < 10:
    L.append(int(randint(0,100)))
    x+=1

for nr in L:
    if nr < i :
        i = nr

print(f"A lista é {L}")
print(f"Onde o menor numero é {i}")