print ("\nDigite 0 para encerrar")
idade = int(input("Digite a idade da pessoa:"))

maior = 0
menor = 0 

while idade  > 0:

    if idade < 18:
        menor += 1
    if idade > 60:
        maior += 1 
    
    print ("\nDigite 0 para encerrar")
    idade = int(input("Digite a idade da pessoa:"))

print (f"\nTeve {menor} pessoas com menos de 18 anos")
print (f"Teve {maior} pessoas com mais de 60 anos\n")