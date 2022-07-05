# Algoritmo de ordenação Bubble/Bolha
def bubble_sort(valores):
   n = len(valores)-1
   for i in range(n,0,-1):
      for j in range(n):
         #print(j, j+1, valores)
         if valores[j] > valores[j + 1]:
            auxiliar = valores[j]
            valores[j] = valores[j + 1]
            valores[j + 1] = auxiliar
   return valores

# Chamada para teste
valores = [5, 4, 3, 2, 1, 6, 0]
print(bubble_sort(valores))