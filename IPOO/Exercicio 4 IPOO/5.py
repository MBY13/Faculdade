#Ler e armazenar num vetor 5 números float fornecidos pelo
#usuário e calcular a média dos valores.

V = []
soma = 0 
x = 0

while x < 5:
    V.append(float(input("Digite um valor:")))
    soma += V[x]
    x+=1

media = soma / 5

print (media)