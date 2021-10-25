#Faça um programa que leia N valores inteiros, e depois
#apresente-os em ordem crescent

L = []
z = int(input("Digite quantos numeros deseja digitar:"))
p = 0

while p < z :
    L.append(int(input("Digite um numero:")))
    p+=1

fim = len(L)
while fim > 1:
    trocou=False
    x = 0
    while x<(fim-1):
        if L[x] > L[x+1]:
            temp = L[x]
            L[x] = L[x+1]
            L[x+1] = temp
            trocou = True
        x += 1
    if not trocou:
        break
    fim-= 1
for e in L:
    print(e,end=",")