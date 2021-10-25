x = 1
soma = 0

while x<=5:
    num = int(input("Digite um numero:"))
    soma = num + soma 
    x = x+1 

media = int(float(soma / 5))

print (f"A media dos numeros digitado é {media}")