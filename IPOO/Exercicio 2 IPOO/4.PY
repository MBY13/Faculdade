#Entrar com um número e imprimir a raiz quadrada do número caso ele seja positivo e
#o quadrado do número caso ele seja negativo.

num = int(input("Digite um numero(positivo ou negativo):"))

if num > 0:
    import math
    raiz = int(math.sqrt(num))
    print(f'\nA raiz quadrada de {num} é {raiz}\n')
else:
    quad = (num**2)
    print(f'\nO quadrado de {num} é {quad}\n')