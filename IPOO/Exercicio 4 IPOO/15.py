#Modifique o programa do slide 32 para ordenar a lista em ordem
#decrescente. L=[2,1,5,4,3] deve ser ordenada como L=[5,4,3,2,1].

L = [2,1,5,4,3]
fim = len(L)
while fim > 1:
    trocou=False
    x = 0
    while x<(fim-1):
        if L[x] < L[x+1]:
            temp = L[x]
            L[x] = L[x+1]
            L[x+1] = temp
            trocou = True
        x += 1
    if not trocou:
        break
    fim-= 1
for e in L:
    print(e,end=",")