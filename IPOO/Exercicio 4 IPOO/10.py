#10. Faça um programa de forma a realizar a mesma tarefa do
#exemplo localizado no slide 21, mas sem utilizar a variável
#achou. Dica: observe a condição de saída do while.

L = [15,7,27,39]
p = int(input("Digite o valor a procurar:"))
x= 0 
y = 0

while x < 4:
    if L[x] is p:
        y = 1 
        break
    x+=1
if y:
    print("%d achado na posição %d" % (p,x))
else:
    print("%d não encontrado"%p)