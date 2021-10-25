print ("\nDigite um numero negativou ou maior que 140 para encerrar")
idade = int(input("Digite a idade da pessoa:"))

maior = 0
menor = 0 

while idade  >  0 and idade < 140:

    if idade < 21:
        menor += 1
    if idade > 50:
        maior += 1 
    
    print ("\nDigite um numero negativou ou maior que 140 para encerrar")
    idade = int(input("Digite a idade da pessoa:"))

print (f"Teve {menor} pessoas com menos de 21 anos")
print (f"Teve {maior} pessoas com mais de 50 anos")