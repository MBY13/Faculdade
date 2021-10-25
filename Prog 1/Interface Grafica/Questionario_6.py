from tkinter import *
import sys

class Janela(Tk):

    __Lb_flamengo=None
    __Lb_vasco=None
    __Lb_torcida_total=None
    __Lb_pr=None
    __Lb_sc=None
    __Lb_rs=None
    __Et_flamengo_pr=None
    __Et_flamengo_sc=None
    __Et_flamengo_rs=None
    __Et_vasco_pr=None
    __Et_vasco_sc=None
    __Et_vasco_rs=None
    __Et_total_flamengo=None
    __Et_total_vasco=None
    __Bt_Calc=None

    def __init__(self, Str="Janela"):
        super().__init__()
        super().title("Torcida de Futebol")
        super().geometry("%sx%s+%s+%s" % ("420", "200", "400", "200"))
        super().configure(bg="orange")  ## Python 3
        self.init_text()
        self.inicialize()

    def init_text(self):
        self.__Lb_pr = "Paraná"
        self.__Lb_sc = "Santa Catarina"
        self.__Lb_rs = "Rio G. do Sul"
    
    def action_Total_Flamengo(self):
        tf = float(float(self.__Et_flamengo_pr.get()) + float(self.__Et_flamengo_sc.get()) + float(self.__Et_flamengo_rs.get()))
        self.__Et_total_flamengo.delete(0,END)
        self.__Et_total_flamengo.insert(END,"%5.2f" % tf)

    def action_Total_vasco(self):
        tv = float(float(self.__Et_vasco_pr.get()) + float(self.__Et_vasco_sc.get()) + float(self.__Et_vasco_rs.get()))
        self.__Et_total_vasco.delete(0,END)
        self.__Et_total_vasco.insert(END,"%5.2f" % tv) 

    def action_exit(self):
        print("Destruindo a janela...")
        self.destroy()
        sys.exit(0)
    
    def action_Bt_Calc(self):
        self.action_Total_Flamengo()
        self.action_Total_vasco()
        self.__Et_total_vasco['state'] = DISABLED
        self.__Et_total_flamengo['state'] = DISABLED
    
    def inicialize(self):
        self.__Lb_flamengo = Label(self, text="Flamengo", width=17)
        self.__Lb_vasco = Label(self, text="Vasco", width=17)
        self.__Lb_pr = Label(self, text=self.__Lb_pr, width=17)
        self.__Lb_sc = Label(self, text=self.__Lb_sc, width=17)
        self.__Lb_rs = Label(self, text=self.__Lb_rs, width=17)
        self.__Lb_torcida_total = Label(self, text="Torcida Total:", width=17)

        self.__Lb_flamengo.configure(bg='yellow', anchor="c")
        self.__Lb_vasco.configure(bg='yellow', anchor="c")
        self.__Lb_pr.configure(bg='yellow', anchor="c")
        self.__Lb_sc.configure(bg='yellow', anchor="c")
        self.__Lb_rs.configure(bg='yellow', anchor="c")
        self.__Lb_torcida_total.configure(bg='yellow', anchor="c")

        self.__Lb_flamengo.grid(row=0, column=1, sticky=NW, padx=4, pady=4)
        self.__Lb_vasco.grid(row=0, column=3, sticky=NW, padx=5, pady=4)
        self.__Lb_pr.grid(row=1, column=0, sticky=NW, padx=4, pady=4) 
        self.__Lb_sc.grid(row=2, column=0, sticky=NW, padx=4, pady=4)
        self.__Lb_rs.grid(row=3, column=0, sticky=NW, padx=4, pady=4)
        self.__Lb_torcida_total.grid(row=5, column=0, sticky=NW, padx=4, pady=4)
        
        self.__Et_flamengo_pr=Entry(self, width=19)
        self.__Et_vasco_pr=Entry(self, width=19)
        self.__Et_flamengo_sc=Entry(self, width=19)
        self.__Et_vasco_sc=Entry(self, width=19)
        self.__Et_flamengo_rs=Entry(self, width=19)
        self.__Et_vasco_rs=Entry(self, width=19)
        self.__Et_total_vasco=Entry(self, width=19)
        self.__Et_total_flamengo=Entry(self, width=19)

        self.__Et_flamengo_pr.grid(row=1, column=1, sticky=NW, padx=4, pady=4)
        self.__Et_vasco_pr.grid(row=1, column=3, sticky=NW, padx=4, pady=4)
        self.__Et_flamengo_sc.grid(row=2, column=1, sticky=NW, padx=4, pady=4)
        self.__Et_vasco_sc.grid(row=2, column=3, sticky=NW, padx=4, pady=4)
        self.__Et_flamengo_rs.grid(row=3, column=1, sticky=NW, padx=4, pady=4)
        self.__Et_vasco_rs.grid(row=3, column=3, sticky=NW, padx=4, pady=4)
        self.__Et_total_vasco.grid(row=5, column=3, sticky=NW, padx=4, pady=4)
        self.__Et_total_flamengo.grid(row=5, column=1, sticky=NW, padx=4, pady=4)

        self.Bt_Calc=Button(self, text='Calcular', command=self.action_Bt_Calc)
        self.Bt_Calc.grid(row=4, column=1, sticky=NW, padx=4, pady=4)

        self.protocol("WM_DELETE_WINDOW", self.action_exit)
########################################################################################################################

Jan1 = Janela("Minha janela")

Jan1.mainloop()