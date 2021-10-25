# Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas
#primeiras.

A = []
B = []
x = int(input("Digite quantos numeros deseja digitar:"))
p = 0

while p < x :
    A.append(int(input("Digite um numero:")))
    p+=1

p = 0

while p < x :
    B.append(int(input("Digite um numero:")))
    p+=1

C = [A+B]

print("A lista formada com a soma das Duas outras foi:")
print(*C , end= " ")