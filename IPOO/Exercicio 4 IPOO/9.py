#Faça um programa que percorra duas listas e gere uma terceira
#sem elementos repetidos.

A=[]
B=[]
L=[]
x=0

while x < 5:
    A.append(int(input("Digite um numero:")))
    x+=1
x=0
while x < 5:
    B.append(int(input("Digite um numero:")))
    x+=1

C=(A+B)

fim = len(C)
while fim > 1:
    trocou = False
    x=0
    while x<(fim -1):
        if C[x]>C[x+1]:
            temp = C[x]
            C[x] = C[x+1]
            C[x+1] = temp
            trocou = True
        x+=1
    if not trocou:
        break
    fim -=1

x=0
L = C[:]
y=0

while x < 9:
    if C[x] == C[x+1]:
        L.pop(x-y)
        y+=1
    x +=1

print ('\n',*L)