from tkinter import *

class Janela(Tk):

        __form = None
        __calc = None
        __resultado = None

        def __init__(self, Str="Calculadora para Estatistica",xy = "800x600"):
            super().__init__()
            super().title(Str)
            super().geometry(xy)
            #super().wm_iconbitmap('icone.ico') #não vou colocar icone pois no video esta linha esta comentada
            #ficaremos com o icone padrão da Biblioteca TKinter
            self.inicialize()
        
        def inicialize(self):
            self.__form = Entry(self)
            self.__form.grid(row=1, column=1, sticky=N, padx=325, pady=4)
            self.__calc = Button(self, text='Calcule')
            self.__calc.grid(row=2, column=1, sticky=N, padx=325, pady=4)
            self.__resultado = Label(self, text="Resultado", fg= "blue")
            self.__resultado.grid(row=3, column=1, sticky=N, padx=325, pady=4)

#######################################################################################################
instancia = Janela()
instancia.mainloop()
