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

#############################################################################

tv = TV("XingLing",50,10)

tv.soundUp()
tv.soundUp()

print("Característica da Televissão:")
print(f"A marca da TV é {tv.marca}")
print(f"O volume do som atual é {tv.volume}")