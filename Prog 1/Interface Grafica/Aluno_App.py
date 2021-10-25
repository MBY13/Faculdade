from tkinter import *
import pygubu

class Aluno_App:
    
    def __init__(self):

        #1: Create a builder
        self.builder = pygubu.Builder()

        #2: Load an ui file
        self.builder.add_from_file('Aluno_App.ui')

        #3: obtém os objetos da UI
        self.Jan1 = self.builder.get_object('JanelaPrincipal')
        self.Et_Nt1 = self.builder.get_object('Et_Nt1')
        self.Et_Nt2 = self.builder.get_object('Et_Nt2')
        self.Et_Nt3 = self.builder.get_object('Et_Nt3')
        self.Et_Media = self.builder.get_object('Et_Media')

        self.builder.connect_callbacks(self)
        
    def run(self):
        self.Jan1.mainloop()
    
    def action_calcular(self):
        print('Entrei no evento')
        n1=float(self.Et_Nt1.get())
        n2=float(self.Et_Nt2.get())
        n3=float(self.Et_Nt3.get())
        total=(n1+n2+n3)/3
        self.Et_Media.delete(0, END)
        self.Et_Media.insert(END, "%4.1f" % total)
    
if __name__ == '__main__':
    app = Aluno_App()
    app.run()