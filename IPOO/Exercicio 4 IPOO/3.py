#Ler 5 inteiros do teclado e armazenar num vetor. Depois
#percorrer este vetor mostrando os números ímpares. 

vetor = []
index = 0
while index <= 4:
    vetor.append(int(input("= Insira um numero: ")))
    index += 1
index = 0
while index <= 4:
    if vetor[index] % 2 != 0:
        print("## ", vetor[index])
    index += 1