y = int(input("Digite com quantos numero você deseja digitar:"))
z = 0
numn = 10000
numm = -10000

while z < y:
    num = int(input("Digite um numero:"))
    z += 1

    if num > numm:
        numm = num 
    if num < numn:
        numn = num

print(f"\nFoi digitado {z} numeros")
print(f"Onde o maior foi {numm}")
print(f"E o menor {numn}\n")