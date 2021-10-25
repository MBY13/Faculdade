from tkinter import *
import sys

class Janela(Tk):

    __lb_nome = None
    __lb_telefone = None
    __lb_email = None
    __lb_Endereco = None
    __et_nome = None
    __et_telefone = None
    __et_email = None
    __et_Endereco = None

    def __init__(self, Str="Janela",x1="0",y1="0",dx="640",dy="480",cor="ligthgray"):
        super().__init__()
        super().title(Str)
        super().geometry("%sx%s+%s+%s" % (dx, dy, x1, y1))
        super().configure(bg=cor)  ## Python 3
        self.inicialize()
       
    def inicialize(self):

        self__lb_nome = Label(self, text="Nome:", width=17)
        self__lb_telefone = Label(self, text="Telefone:", width=17)
        self__lb_email = Label(self, text="Email:", width=17)
        self__lb_Endereco = Label(self, text="Endereço:", width=17)

        self__lb_nome.configure(bg='yellow', anchor="ne")
        self__lb_telefone.configure(bg='yellow', anchor="ne")
        self__lb_email.configure(bg='yellow', anchor="ne")
        self__lb_Endereco.configure(bg='yellow', anchor="ne")

        self__lb_nome.grid(row=0, column=1, sticky=NW, padx=4, pady=4)
        self__lb_telefone.grid(row=1, column=1, sticky=NW, padx=4, pady=4)
        self__lb_email.grid(row=2, column=1, sticky=NW, padx=4, pady=4)
        self__lb_Endereco.grid(row=3, column=1, sticky=NW, padx=4, pady=4)

        self__et_nome = Entry(self, width=42)
        self__et_telefone = Entry(self, width=42)
        self__et_email = Entry(self, width=42)
        self__et_Endereco = Entry(self, width=42)

        self__et_nome.grid(row=0, column=2, sticky=NW, padx=4, pady=4)
        self__et_telefone.grid(row=1, column=2, sticky=NW, padx=4, pady=4)
        self__et_email.grid(row=2, column=2, sticky=NW, padx=4, pady=4)
        self__et_Endereco.grid(row=3, column=2, sticky=NW, padx=4, pady=4)

########################################################################################################################

Jan1 = Janela("Minha janela Tkinter", "500", "250", "400", "120", "orange")
Jan1.mainloop()