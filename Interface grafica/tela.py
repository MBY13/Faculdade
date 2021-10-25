import PySimpleGUI as sg 

#https://pysimplegui.readthedocs.io/en/latest/

class TelaPython:
    def __init__(self):
        #sg.change_look_and_feel("nome do tema")
        #Layout
        Layout = [
            [sg.Text("Nome:",size=(5,0)),sg.Input(size=(15,0),key="nome")],
            [sg.Text("Idade:",size=(5,0)),sg.Input(size=(15,0),key="idade")],
            [sg.Text("Quais provedores de e-mail são aceitos?")],
            [sg.Checkbox("Gmail",key="Gmail"),sg.Checkbox("Outlook",key="Outlook"),sg.Checkbox("Yahoo",key="Yahoo")],
            [sg.Text("Aceita cartão?")],
            [sg.Radio("sim",'cartao',key="cartaosim"),sg.Radio("não",'cartao',key="cartaonao")],
            [sg.Text("Velocidade")],
            [sg.Slider(range=(0,255),default_value=0,orientation="h",size=(15,20),key='slidervelocidade')],
            [sg.Button("Enviar dados")],
            [sg.Output(size=(30,20))]
        ]
        #janela
        self.Janela = sg.Window("Dados do Usuario").layout(Layout)
        
        
    
    def iniciar(self):
        while True:
            #extrair dados 
            self.button,self.values = self.Janela.Read()

            nome = self.values["nome"]
            idade = self.values["idade"]
            aceita_gmail = self.values["Gmail"]
            aceita_outlook = self.values["Outlook"]
            aceita_yahoo = self.values["Yahoo"]
            cartaosim = self.values['cartaosim']
            cartaonao = self.values['cartaonao']
            velocidade = self.values['slidervelocidade']


            print(f"NOME: {nome}")
            print(f"IDADE:{idade}")
            print(f"GMAIL:{aceita_gmail}")
            print(f"OUTLOOK:{aceita_outlook}")
            print(f"YAHOO:{aceita_yahoo}")
            print(f"ACEITA CARTÃO:{cartaosim}")
            print(f"NÃO ACEITA CARTÃO: {cartaonao}")
            print(f"velocidade: {velocidade}")

tela = TelaPython()
tela.iniciar()