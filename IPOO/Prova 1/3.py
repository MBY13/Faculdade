v = [ ]
valor = int ( input("Digite valor (0 para fim): "))
while (valor != 0):
     v.append(valor)
     valor = int ( input("Digite valor (0 para fim): ")) 

num = 0
for n in v:
    if v[num] < 0:
        print ("Valores negativos na posição:",num)
    num += 1