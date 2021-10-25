class No_fila:
    def __init__(self):
        self.__nome = None
        self.__proximo = None

    def get_nome(self):
        return self.__nome

    def get_proximo(self):
        return self.__proximo

    def set_nome(self, nome):
        self.__nome = nome

    def set_proximo(self, proximo):
        self.__proximo = proximo  

class Fila:
    def __init__(self):
        #self.__inicio = None
        self.__final = None

    def push(self,nome):
        temp_no = No_fila()
        if temp_no:
            temp_no.set_nome(nome)
            if self.__final:                  
                temp_no.set_proximo(self.__final.get_proximo())                  
                self.__final.set_proximo(temp_no)   
                self.__final = temp_no               
            else:                 
                temp_no.set_proximo(temp_no)                  
                # self.__inicio = self.__final = temp_no 
                self.__final = temp_no        
            self.print_all()         
        else:               
            print("Erro ao inserir.")            
        
    # def pop(self):        
    #     if self.__final:  
    #         nome = self.__inicio.get_nome()               
    #         if (self.__inicio == self.__final):                 
    #             self.__inicio = self.__final = None
    #         else:
    #             proximo = self.__inicio.get_proximo()
    #             self.__inicio = proximo
    #             self.__final.set_proximo(self.__inicio)
    #         print("Nome removido: ", nome)
    #         self.print_all()        
    #     else:
    #         print("Erro ao remover, fila vazia.")

    def pop2(self):        
        if self.__final:  
            nome = self.__final.get_proximo().get_nome()               
            if (self.__final.get_proximo() == self.__final):                
                self.__final = None
            else:
                proximo = self.__final.get_proximo().get_proximo()
                self.__final.set_proximo(proximo)
            print("Nome removido: ", nome)
            self.print_all()        
        else:
            print("Erro ao remover, fila vazia.")

    def print_all(self):
        if self.__final:       
            temp_no = No_fila()
            temp_no = self.__final.get_proximo()
            saida = " Fila circular:"  
            while temp_no != self.__final:   
                saida += str(temp_no.get_nome()) + "\t"   
                temp_no = temp_no.get_proximo()         
            print(saida, "\t", temp_no.get_nome())      
            primeiro = self.__final.get_proximo().get_nome()
            print("\nPrimeiro: ", primeiro)
            ultimo = self.__final.get_nome()
            print("Último: ", ultimo)    
        else:
            print("Erro ao imprimir, fila vazia.")

    def print_all3(self):
        if self.__final:       
            temp_no = No_fila()
            saida = "Fila circular:\n"
            contador = 0
            temp_no = self.__final.get_proximo()
            while temp_no != self.__final.get_proximo() or contador <3:   
                saida += str(temp_no.get_nome()) + "\t"   
                temp_no = temp_no.get_proximo()
                if temp_no == self.__final.get_proximo():
                    contador += 1  
                    saida += "\n"
            print(saida, "\t")      
            primeiro = self.__final.get_proximo().get_nome()
            print("\nPrimeiro: ", primeiro)
            ultimo = self.__final.get_nome()
            print("Último: ", ultimo)    
        else:
            print("Erro ao imprimir, fila vazia.")
def main():
    fila = Fila()
    while True:
        op = int(input("1 - Inserir\n"
                       "2 - Remover\n"
                       "3 - Imprimir\n"
                       "4 - Imprimir 3 vezes\n"
                       "5 - Sair"
                       "\n\nOpção:\n"))            
        if op == 1:
            nome = input("Informe o nome: \n")
            fila.push(nome)
        elif op == 2:
            fila.pop2()
        elif op == 3:
            fila.print_all()
        elif op == 4:
            fila.print_all3()
        elif op == 5:
            break
        else:
            print("Opcao invalida.")

if __name__ == '__main__':
    main() 