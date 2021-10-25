#A lista de temperaturas de Mons, na Bélgica, foi armazenada na
#lista T = [-10, -8, 0, 1, 2, 3, -2, -4]. Faça um programa que
#imprima a menor e a maior temperatura, assim como a
#temperatura média.

T = [-10, -8, 0, 1, 2, 3, -2, -4]
menor = 9999
maior = -9999
x=0
soma = 0

for nr in T:
    if nr < menor :
        menor = nr
    if nr > maior :
        maior = nr 

while x < len(T):
    soma = soma + T[x]
    x+=1

media = soma / len(T)

print(f"A menor temperatura em Mons é {menor}")
print(f"A maior temperatura em Mons é {maior}")
print(f"A media da temperatura de Mons é {media}")