print("\nDigite -123 para encerrar")

maior = -9999
menor = 9999

num = int(input("Digite um numero:"))

while num != -123:
    if num < menor:
        menor = num 
    if num > maior:
        maior = num 

    print("\nDigite -123 para encerrar")
    num = int(input("Digite um numero:"))

print (f"\nO maior numero digitado foi {maior}")
print(f"O menor numero digitado foi {menor}\n")