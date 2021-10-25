class TV:
    marca = None    # marca da TV (string)
    polegadas = None    # tamanho da TV em polegadas (inteiro)
    volume = None   # volume atual do som (inteiro)
    __canal = None  # canal atual da TV (inteiro)

    def __init__(self, m, p, v=10, c=1):
        self.marca = m
        self.polegadas = p
        self.volume = v
        self.__canal = c

    def soundUp (self):
        self.volume += 1

    def soundDown (self):
        self.volume -= 1

    def canalUp (self):
        self.__canal += 1

    def canalDown (self):
        self.__canal -= 1

    def getcanal(self):
        return self.__canal