class ObjetoGrafico:
    _centro = None

    def __init__(self, centro):
	    self._centro = centro

    def desenha(self):
        print('Desenha objeto gráfico')

class Circulo(ObjetoGrafico):
    _raio = None
    A = None    

    def __init__(self, centro, raio):
        super().__init__(centro)
        self._raio = raio

    def desenha(self):
        print("Desenha círculo")

    def area (self):
        A = 3.14 * self._raio ** 2 
        return A 


class Retangulo(ObjetoGrafico):
    _altura = 10
    _largura = 5
    A = None  

    def __init__(self, centro, altura, largura):
        super().__init__(centro)
        self._altura = altura
        self._largura = largura

    def desenha(self):
        print('Desenha retângulo')

    def area (self):
        A = self._altura * self._largura
        return A 

class Quadrado(Retangulo):
    _largura = None 

    def __init__(self, centro, largura):
        super().__init__(centro, largura, largura)
        self._largura = largura 

    def area (self):
        A = self._largura **2
        return A 
######################################
g1 = Circulo(0, 5)
g2 = Quadrado(0, 5)

areas = []
areas.append(g1.area())
areas.append(g2.area())
areas.append(g2.area())

cont = 0

while 2 > cont:
    print(f"Area do Circulo:{areas[cont]}")
    cont +=1 
    print(f"Area do Retangulo:{areas[cont]}")
    cont +=1 
    print(f"Area do Quadrado:{areas[cont]}")