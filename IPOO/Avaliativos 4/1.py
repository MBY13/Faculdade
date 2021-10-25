# A área A de um círculo é calculada por: A = PI * (raio * raio), sendo PI=3,1415.
# Implemente uma classe chamada 'circulo' com o atributo 'raio' e método 'area'.
# O raio é informado pelo usuário e passado para o método construtor na criação do objeto.
# O método 'area' retorna a área do círculo.
# Crie um objeto da classe 'circulo' com raio fornecido pelo usuário, e informe a área do círculo
#chamando o método 'area'

class circulo:
    raio = None 

    def __init__(self):
        self.raio = float(input("Digite o Valor do RAIO:"))
    def area (self):
        A = 3.1415*(self.raio * self.raio)
        return A
######################################
print("\nDIGITE OS DADOS DO CIRCULO")
area_do_circulo = circulo()

print("=========="*10)
print (f"\t\t\tA área de do circulo é {round(area_do_circulo.area(),2)}")
print("=========="*10)