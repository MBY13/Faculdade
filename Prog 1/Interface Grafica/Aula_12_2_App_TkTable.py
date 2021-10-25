from tkinter import *
from tkinter import messagebox

################################################################

Dados = [['01', 'Antonio', '18', '2019'],
         ['02', 'Beatriz', '19', '2018'],
         ['03', 'Carlos', '20', '2017'],
         ['04', 'Darlan', '17', '2020'],
         ['05', 'Eduardo', '21', '2016'],
         ['06', 'Fernando', '20', '2015'],
         ['07', 'Guilherme', '19', '2017'],
         ['08', 'Humberto', '18', '2018'],
         ['09', 'Isabel', '17', '2021'],
         ['10', 'Joao', '21', '2016'],
         ['11', 'Karen', '23', '2015'],
         ['12', 'Luciana', '19', '2018'],
         ['13', 'Maria', '18', '2020'],
         ['14', 'Nicole', '19', '2019']]

################################################################

class Janela(Tk):
    Cnv1 = None
    inter = None
    inter_id = None
    Matriz = None

    def __init__(self, Str="Janela", x1="0", y1="0", dx="640", dy="480", cor="ligthgray"):
        super().__init__()
        super().title(Str)
        super().geometry("%sx%s+%s+%s" % (dx, dy, x1, y1))
        super().configure(bg=cor)
        self.inicialize()

    def action_exit(self):
        print("Destruindo a janela...")
        self.destroy()
        sys.exit(0)

    def action_print(self):
        self.configure(bg='green', width='100', height='100')
        Texto = ""
        for row in self.Matriz:
            for cell in row:
                Texto += "%s,  " % cell.get()
            Texto += "\n"
        messagebox.showinfo("Information", Texto)
        print(Texto)

    # track changes to the canvas and frame width and sync them,
    # also updating the scrollbar
    def _configure_interior(self, event):
        # update the scrollbars to match the size of the inner frame
        size = (self.inter.winfo_reqwidth(), self.inter.winfo_reqheight())
        self.Cnv1.config(scrollregion="0 0 %s %s" % size)
        if self.inter.winfo_reqwidth() != self.Cnv1.winfo_width():
            # update the canvas's width to fit the inner frame
            self.Cnv1.config(width=self.inter.winfo_reqwidth())

    def _configure_canvas(self, event):
        if self.inter.winfo_reqwidth() != self.Cnv1.winfo_width():
            # update the inner frame's width to fill the canvas
            self.Cnv1.itemconfigure(self.inter_id, width=self.Cnv1.winfo_width())

    def inicialize(self):
        self.Cnv1 = Canvas(self, width=300, height=260, confine=False, yscrollincrement=10, scrollregion=(0, 0, 300, 260))
        self.Cnv1.configure(bg='yellow', scrollregion="0 0 200 360")
        self.Cnv1.xview_moveto(0)
        self.Cnv1.yview_moveto(0)

        self.inter = Frame(self.Cnv1)
        self.inter_id = self.Cnv1.create_window(0, 0, window=self.inter, anchor=NW);

        self.inter.bind('<Configure>', self._configure_interior)

        self.Cnv1.bind('<Configure>', self._configure_canvas)

        Sb1 = Scrollbar(self, orient="vertical")

        Lb1 = Label(self.inter, text="Cod.")
        Lb2 = Label(self.inter, text="Nome")
        Lb3 = Label(self.inter, text="Idade")
        Lb4 = Label(self.inter, text="Ingresso")

        Lb1.configure(bg='yellow')
        Lb2.configure(bg='yellow')
        Lb3.configure(bg='yellow')
        Lb4.configure(bg='yellow')

        Lb1.grid(row=0, column=0, sticky=W, padx=2, pady=2)
        Lb2.grid(row=0, column=1, sticky=W, padx=2, pady=2)
        Lb3.grid(row=0, column=2, sticky=W, padx=2, pady=2)
        Lb4.grid(row=0, column=3, sticky=W, padx=2, pady=2)

        nlin = len(Dados)
        ncol = len(Dados[0])
        self.Matriz = []
        for i in range(nlin):
            cols = []
            for j in range(ncol):
                Et1 = Entry(self.inter, relief=RIDGE)
                Et1.grid(row=(i+1), column=j, sticky=NSEW, padx=2, pady=2)
                Et1.insert(END, '%s' % Dados[i][j])
                cols.append(Et1)
            self.Matriz.append(cols)

        # Sb1.set(0,10)
        Sb1.config(command=self.Cnv1.yview)
        self.Cnv1.config(yscrollcommand=Sb1.set)

        Bt1 = Button(self, text='Print', padx=1, pady=1, command=self.action_print)
        Bt2 = Button(self, text='Exit', padx=1, pady=1, command=self.action_exit)

        self.Cnv1.grid(row=0, column=0, columnspan=2)
        Sb1.grid(row=0, column=ncol+1, rowspan=nlin, sticky=NS)
        Bt1.grid(row=nlin, column=0, sticky=NSEW, padx=2, pady=2)
        Bt2.grid(row=nlin, column=1, sticky=NSEW, padx=2, pady=2)

        self.protocol("WM_DELETE_WINDOW", self.action_exit)

########################################################################################################################

Jan1=Janela("Minha janela", "400", "200", "540", "410", "orange")
Jan1.mainloop()