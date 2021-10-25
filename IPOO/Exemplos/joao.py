vetor = []

i=0
while i < 5:

    n = int(input("Insira um numero aqui: "))
    i += 1
    vetor.append(n)

p = int(input('Digite o valor que deseja achar'))

achou = False

x = 0

while x < len[vetor]:
    if vetor[x] is p:
        achou = True
        break

    x += 1

if achou:
    print('%d achado na posição %d” % (p,x)')
else:
    print('%d não encontrado” % p') 