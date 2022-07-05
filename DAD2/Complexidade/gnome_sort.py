import time
from datetime import timedelta 
from numpy import loadtxt

def gnomeSort(aux, n):
    global valor_inicial,valor_final
    valor_inicial = time.time()

    indice = 0

    while indice < n:

        if indice == 0:
            indice = indice + 1

        if aux[indice] >= aux[indice - 1]:
            indice = indice + 1

        else:
            aux[indice], aux[indice-1] = aux[indice-1], aux[indice] # 3 operações
            indice = indice - 1
    valor_final = time.time()
    return aux

valores = []
# lines = loadtxt("dad2/Complexidade/Arquivos TXT/ordenado10000000.txt")
# lines = loadtxt("dad2/Complexidade/Arquivos TXT/SemiOrdenado10000000.txt")
# lines = loadtxt("dad2/Complexidade/Arquivos TXT/aleatorio1000000.txt")
lines = loadtxt("dad2/Complexidade/Arquivos TXT/Repetido1000000.txt")
# lines = loadtxt("dad2/Complexidade/Arquivos TXT/reverso100.txt")
for line in lines:
    valores.append(line)

n = len(valores)
gnomeSort(valores,n)

hours, rem = divmod(valor_final-valor_inicial, 3600)
minutes, seconds = divmod(rem, 60)

print("{:0>2}:{:0>2}:{:05.4f}".format(int(hours),int(minutes),seconds))