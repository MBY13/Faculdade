# Faça um programa que calcule as raízes de ax²+bx+c, pressupondo que seu delta sempre será positivo e 
# sempre terá uma raiz exata. 

print("\nFORMULA : AX²+BX+C")
print("Entre com os valores abaixo\n")

a = int(input("Digite o valor de A:"))
x = int(input("Digite o valor de X:"))
b =int(input("Digite o valor de B:"))
c = int(input("Digite o valor de C:"))

delta = ((a*(x**2))+(b*x) + c )

import math
raiz = math.sqrt(delta)
print(f'\nA raiz quadrada de {a}.{x**2}+{b}.{x}+{c} é {raiz}\n')