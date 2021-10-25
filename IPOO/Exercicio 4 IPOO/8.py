#Faça um programa que leia duas listas e que gere uma terceira
#com os elementos das duas primeiras.

A=[]
B=[]
C=[]
x=0

while x < 5:
    A.append(int(input("Digite um numero:")))
    x+=1
x=0
while x < 5:
    B.append(int(input("Digite um numero:")))
    x+=1

for x in A:
    C.append(x)
for x in B:
    C.append(x)
for x in C:
    print (x, end=" ")