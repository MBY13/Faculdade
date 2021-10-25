x = 0
soma = 0
neg = 0

while x <10:
    num = int(input("Digite um numero:"))
    x = x+1
    if num > 0:
        soma = int(float(soma + num)) 
    else:
        neg = int(float(neg + 1))

print(f"\nFoi Digitado {x} numeros")
print(f"Onde a soma dos positivos foi {soma}")
print(f"E foi digitado {neg} negativos \n")