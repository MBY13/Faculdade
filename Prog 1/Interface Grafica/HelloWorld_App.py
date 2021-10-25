## HelloWorld_App.py
from tkinter import *
import pygubu

class HelloWorld_App:
    
    def __init__(self):

        #1: Create a builder
        self.builder = pygubu.Builder()

        #2: Load an ui file
        self.builder.add_from_file('HelloWorld_App.ui')

        #3: Create the mainwindow
        self.Jan1 = self.builder.get_object('JanelaPrincipal')
        
    def run(self):
        self.Jan1.mainloop()

if __name__ == '__main__':
    app = HelloWorld_App()
    app.run()