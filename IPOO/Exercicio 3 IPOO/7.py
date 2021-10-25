print ("\nDigite 0 para encerrar")

num = int(input("Digite um numero:"))
soma = 0
c = 0

while num != 0:
    soma = soma + num 
    c += 1 
    print ("\nDigite 0 para encerrar")

    num = int(input("Digite um numero:"))

media = round((soma / c),2) 

print(f"A media dos numeros digitados foi {media}\n")