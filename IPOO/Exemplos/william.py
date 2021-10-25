#9. Faça um programa que percorra duas listas e gere uma terceira
#sem elementos repetidos.
a = [1, 1, 3, 5]
b = [4, 5, 6, 6]
e = (a+b)
b = e[:]
f =  8
x = 0
y = 0

while x < 4 :
   
    if e[x]  == e[y]:
        del b[y]
        print(y)

    y += 1

    if y == len(e):
        x += 1
        y = 0

print(*b)