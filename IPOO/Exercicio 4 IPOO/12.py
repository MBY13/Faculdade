#Modifique o exercício anterior de forma a pesquisar p e v em
#toda a lista e informando ao usuário a posição onde p e a posição
#onde v foram encontrados.

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
        print (f"{v}: encontrado na posição {y}")
        print (f"{p}: encontrado na posição {x}")
    if x < y:
        print (f"{p} Foi encontrado antes que {v}")
        print (f"{p}: encontrado na posição {x}")
        print (f"{v}: encontrado na posição {y}")
else: 
    if achou:
        print(f"O valor de {p} foi encontrado")
        print (f"{p}: encontrado na posição {x}")
    else:
        print(f"O valor de {p} não foi encontrado")
    if achou1:
        print(f"O valor de {v} foi encontrado")
        print (f"{v}: encontrado na posição {y}")
    else:
        print(f"O valor de {v} não foi encontrado")