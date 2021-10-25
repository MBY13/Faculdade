x = 2
soma = 0

while x>1:
    x = int(input("Digite um numero:"))
    
    soma = x + soma

    if x == 1:
        break
print(f"A soma dos numeros digitados foi {soma}")