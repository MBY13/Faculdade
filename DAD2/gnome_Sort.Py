import time 

def gnomeSort(aux, n):

    indice = 0

    while indice < n:

        if indice == 0:
            indice = indice + 1

        if aux[indice] >= aux[indice - 1]:
            indice = indice + 1

        else:
            aux[indice], aux[indice-1] = aux[indice-1], aux[indice]
            indice = indice - 1
 
    return aux

valor_inicial = time.time()
valores = [ 100,30,50,-10,0,1,5,3,900,2,4,56]
n = len(valores)

valores = gnomeSort(valores, n)
print (valores)

valor_final = time.time()

print(f"Demorou {valor_final - valor_inicial} segundos para executar o codigo")