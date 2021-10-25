class TV:
    marca = None    # marca da TV (string)
    polegadas = None    # tamanho da TV em polegadas (inteiro)
    volume = None   # volume atual do som (inteiro)

    def __init__(self, m, p, v):
        self.marca = m
        self.polegadas = p
        self.volume = v

    def soundUp (self):
        self.volume += 1

    def soundDown (self):
        self.volume -= 1

class smartTV(TV):
    __OpSystem = None 
    __WiFi = None 

    def __init__(self,m,p,v,o,w):
        super().__init__(m,p,v)
        self.__OpSystem = o
        self.__WiFi = w