#Entrar com um número e informar se ele é divisível por 3 e por 7.

num = int(input("Digite um numero :"))

if (num % 3) == 0:
    print ("O NUMERO É DIVISIVEL POR 3")
else:
    print("O NUMERO NÃO É DIVISIVEL POR 3")

if (num % 7) == 0:
    print ("O NUMERO É DIVISIVEL POR 7")
else:
    print("O NUMERO NÃO É DIVISIVEL POR 7")