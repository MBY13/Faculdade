from tkinter import *
import sys

class Janela(Tk):

    __Lb_fusca=None
    __Lb_opala=None
    __Lb_corsa=None
    __Lb_km=None
    __Lb_litr=None
    __Lb_consum=None
    __Lb_menor_consum=None
    __Et_fusca_km=None
    __Et_fusca_litr=None
    __Et_fusca_consum=None
    __Et_opala_km=None
    __Et_opala_litr=None
    __Et_opala_consum=None
    __Et_corsa_km=None
    __Et_corsa_litr=None
    __Et_corsa_consum=None
    __Et_menor_consum = None
    __Bt_Calc=None

    def __init__(self, Str="Janela"):
        super().__init__()
        super().title(Str)
        super().configure(bg="orange")
        self.inicialize()

    def init_text(self):
        self.__Lb_km.configure(text="Quilometragem:")
        self.__Lb_litr.configure(text="Litros:")
        self.__Lb_consum.configure(text="Consumo:")
        self.__Lb_menor_consum.configure(text="Menor Consumo:")
    
    def action_Consumo_Fusca(self):
        cf = float(float(self.__Et_fusca_km.get()) / float(self.__Et_fusca_litr.get()))
        self.__Et_fusca_consum.delete(0,END)
        self.__Et_fusca_consum.insert(END,"%5.2f" % cf)

    def action_Consumo_Opala(self):
        co = float(float(self.__Et_opala_km.get()) / float(self.__Et_opala_litr.get()))
        self.__Et_opala_consum.delete(0,END)
        self.__Et_opala_consum.insert(END,"%5.2f" % co) 
    
    def action_Consumo_Corsa(self):
        cc = float(float(self.__Et_corsa_km.get()) / float(self.__Et_corsa_litr.get()))
        self.__Et_corsa_consum.delete(0,END)
        self.__Et_corsa_consum.insert(END,"%5.2f" % cc) 
    
    def action_Menor_Consumo(self):
        menor = -999999999
        if float(self.__Et_fusca_consum.get()) > menor:
            menor = float(self.__Et_fusca_consum.get())
            self.__Et_menor_consum.delete(0,END)
            self.__Et_menor_consum.insert(END,"Fusca")
        if float(self.__Et_opala_consum.get()) > menor:
            menor = float(self.__Et_opala_consum.get())
            self.__Et_menor_consum.delete(0,END)
            self.__Et_menor_consum.insert(END,"Opala")
        if float(self.__Et_corsa_consum.get()) > menor:
            self.__Et_menor_consum.delete(0,END)
            self.__Et_menor_consum.insert(END,"Corsa")

    def action_exit(self):
        self.destroy()
        sys.exit(0)
    
    def action_Bt_Calc(self):
        self.action_Consumo_Fusca()
        self.action_Consumo_Opala()
        self.action_Consumo_Corsa()
        self.action_Menor_Consumo()
    
    def inicialize(self):
        self.__Lb_fusca = Label(self, text="Fusca", width=17)
        self.__Lb_opala = Label(self, text="Opala", width=17)
        self.__Lb_corsa = Label(self, text="Corsa", width=17)
        self.__Lb_km = Label(self, text=self.__Lb_km, width=17)
        self.__Lb_litr = Label(self, text=self.__Lb_litr, width=17)
        self.__Lb_consum = Label(self, text=self.__Lb_consum, width=17)
        self.__Lb_menor_consum = Label(self, text=self.__Lb_menor_consum , width=17)

        self.__Lb_fusca.configure(bg='yellow', anchor="c")
        self.__Lb_opala.configure(bg='yellow', anchor="c")
        self.__Lb_corsa.configure(bg='yellow', anchor="c")
        self.__Lb_km.configure(bg='yellow', anchor="ne")
        self.__Lb_litr.configure(bg='yellow', anchor="ne")
        self.__Lb_consum.configure(bg='yellow', anchor="ne")
        self.__Lb_menor_consum.configure(bg='yellow', anchor="ne")

        self.__Lb_fusca.grid(row=1, column=2, sticky=NW, padx=4, pady=4)
        self.__Lb_opala.grid(row=1, column=3, sticky=NW, padx=4, pady=4)
        self.__Lb_corsa.grid(row=1, column=4, sticky=NW, padx=4, pady=4)
        self.__Lb_km.grid(row=2, column=1, sticky=NW, padx=4, pady=4)
        self.__Lb_litr.grid(row=3, column=1, sticky=NW, padx=4, pady=4)
        self.__Lb_consum.grid(row=4, column=1, sticky=NW, padx=4, pady=4)
        self.__Lb_menor_consum.grid(row=6, column=1, sticky=NW, padx=4, pady=4)
        
        self.__Et_fusca_km = Entry(self)
        self.__Et_fusca_litr = Entry(self)
        self.__Et_fusca_consum = Entry(self)
        self.__Et_opala_km = Entry(self)
        self.__Et_opala_litr = Entry(self)
        self.__Et_opala_consum = Entry(self)
        self.__Et_corsa_km = Entry(self)
        self.__Et_corsa_litr = Entry(self)
        self.__Et_corsa_consum = Entry(self)
        self.__Et_menor_consum = Entry(self)

        self.__Et_fusca_km.grid(row=2, column=2, sticky=NW, padx=4, pady=4)
        self.__Et_fusca_litr.grid(row=3, column=2, sticky=NW, padx=4, pady=4)
        self.__Et_fusca_consum.grid(row=4, column=2, sticky=NW, padx=4, pady=4)
        self.__Et_opala_km.grid(row=2, column=3, sticky=NW, padx=4, pady=4)
        self.__Et_opala_litr.grid(row=3, column=3, sticky=NW, padx=4, pady=4)
        self.__Et_opala_consum.grid(row=4, column=3, sticky=NW, padx=4, pady=4)
        self.__Et_corsa_km.grid(row=2, column=4, sticky=NW, padx=4, pady=4)
        self.__Et_corsa_litr.grid(row=3, column=4, sticky=NW, padx=4, pady=4)
        self.__Et_corsa_consum.grid(row=4, column=4, sticky=NW, padx=4, pady=4)
        self.__Et_menor_consum.grid(row=6, column=2, sticky=NW, padx=4, pady=4)

        self.__Bt_Calc=Button(self, text='Calcular', command=self.action_Bt_Calc)
        self.__Bt_Calc.grid(row=5, column=2, sticky=NW, padx=4, pady=4)

        self.protocol("WM_DELETE_WINDOW", self.action_exit)
        self.init_text()
########################################################################################################################

Jan1 = Janela("Consumo de Automóveis (Dados Hipotéticos)")

Jan1.mainloop()