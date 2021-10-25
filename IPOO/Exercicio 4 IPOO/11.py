#Modifique o exemplo (slide 21) para pesquisar dois valores. Em
#vez de apenas p, leia outro valor v que também será procurado.
#Na impressão, indique qual dos dois valores foi achado primeiro.

L = [15,7,27,39]
p = int(input("Digite o valor a procurar:"))
v = int(input("Digite o valor a procurar:"))
x= 0 
y=0
achou = False 
achou1 = False

while x < 4:
    if L[x] is p:
        achou = True
        break
    x+=1

while y < 4:
    if L[y] is v:
        achou1 = True
        break
    y+=1

if achou and achou1:
    if x > y:
        print (f"{v} Foi encontrado antes que {p}")
    if x < y:
        print (f"{p} Foi encontrado antes que {v}")
else: 
    if achou:
        print(f"O valor de {p} foi encontrado")
    else:
        print(f"O valor de {p} não foi encontrado")
    if achou1:
        print(f"O valor de {v} foi encontrado")
    else:
        print(f"O valor de {v} não foi encontrado")