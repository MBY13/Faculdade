#Implemente um programa onde o usuário informa 5 valores inteiros, que ficarão
#armazenados em uma lista, daí o programa pede um valor a pesquisar e informa em qual posição o
#valor foi encontrado, ou se não foi encontrado.

A = []
x = 0
achou = False

while x < 5:
    A.append(int(input("Digite um valor:")))
    x+=1

p = (int(input("Digite um valor a ser procurado na lista:")))

x=0

while x < len(A):
    if A[x] is p:
        achou = True
        break
    x+=1

if achou:
    print(f"O valor {p} foi encontrado na possição {x}!!")
else: 
    print(f"O valor {p} não foi encontrado!!!")