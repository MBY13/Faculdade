def f(n):
    if n >= 2:
        return f(n -2) + f(n-1)
    elif n == 0 :
        return 0
    else:
        return 1

numero = int(input("Qual posição da Fibonacci você quer imprimir? "))
print("A Fibonacci da posição",numero, "é Fibonacci", f(numero))