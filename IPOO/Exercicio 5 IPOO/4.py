#Escreva uma função que receba a base e a altura de um
#triângulo e retorne sua área (A = (base x altura)/2).
#Exemplo de valores esperados: área_triângulo(5,8) = 20

def área_triângulo(x,y):
    A = ((x * y)/2)
    return A 

############################

x = int(input("Digite o tamanho da base do triângulo:"))
y = int(input("Digite a altura do triângulo:"))

print(f"A área do triângulo é {(área_triângulo(x,y))}")