# A área A de um triângulo é calculada por: A = (base * altura)/2.0.
# Implemente uma classe chamada 'triangulo' com os atributos 'base' e 'altura' e método 'area'.
# Base e altura são informadas pelo usuário e passadas para o método construtor na criação do objeto.
# O método 'area' retorna a área do triângulo.
# Crie dois objetos da classe 'triangulo' com base e altura fornecidas pelo usuário, e informe a área do
#triângulo maior.

class triangulo:
    base = None
    altura = None

    def __init__(self):
        self.base = float(input("Digite a Base do TRIANGULO:"))
        self.altura = float(input("Digite a Altura do TRIANGULO:"))

    def area (self):
        A = (self.base * self.altura)/2.0
        return A 
#############################################################
print("\nDIGITE OS DADOS DO PRIMEIRO TRIANGULO")
trium = triangulo()

print("\nDIGITE OS DADOS DO SEGUNDO TRIANGULO")
tridois = triangulo()

if trium.area() > tridois.area():
    print("=========="*10)
    print(f"\t\t\tA maior área de triangulo foi o 1º com exatos {trium.area()} de area")
    print("=========="*10)
elif trium.area() < tridois.area():
    print("=========="*10)
    print(f"\t\t\tA maior área de  triangulo foi o 2º com exatos {tridois.area()} de area")
    print("=========="*10)
elif trium.area() == tridois.area():
    print("=========="*10)
    print(f"\t\t\tOs dois triangulos tem a mesma área com exatos {tridois.area()} de area")
    print("=========="*10)