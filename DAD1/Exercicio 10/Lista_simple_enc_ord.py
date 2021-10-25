class No_lista:
  def __init__(self):
    self.__codigo = 0
    self.__nome = None
    self.__proximo = None

  def get_codigo(self):
    return self.__codigo
  def set_codigo(self, codigo):
    self.__codigo = codigo

  def get_nome(self):
    return self.__nome
  def set_nome(self, nome):
    self.__nome = nome

  def get_proximo(self):
    return self.__proximo
  def set_proximo(self, proximo):
    self.__proximo = proximo

class Minha_lista_encadeada_ordenada:
  def __init__(self):
    self.__inicio = None

  def push(self, codigo, nome):
    novo = No_lista()
    if novo:
      novo.set_codigo(codigo)
      novo.set_nome(nome)
      if self.__inicio:
        if novo.get_codigo() <= self.__inicio.get_codigo():
          novo.set_proximo(self.__inicio)    
          self.__inicio = novo                
        else:
          proximo = self.__inicio            
          while True:
            if proximo.get_proximo():
              if novo.get_codigo() <= proximo.get_proximo().get_codigo():
                novo.set_proximo(proximo.get_proximo())
                proximo.set_proximo(novo)
                break
              proximo = proximo.get_proximo()        
            else:
              proximo.set_proximo(novo)     
              break
      else:
        novo.set_proximo(None)
        self.__inicio = novo        

  def pop(self, cod_remover):
    if self.__inicio:
      temp = self.__inicio
      if cod_remover is temp.get_codigo():
        self.__inicio = temp.get_proximo()
        print("inicio", self.__inicio.get_codigo())
        return
      while temp.get_proximo():
        if cod_remover is temp.get_proximo().get_codigo(): 
          temp.set_proximo(temp.get_proximo().get_proximo())
          return
        temp = temp.get_proximo()
      print("Código", cod_remover, "não encontrado.")
    else:
      print("Lista vazia, não pode remover.")

  def print_all(self):
    if self.__inicio:
      saida = "\n\nLista: \n"
      aux = self.__inicio
      while aux:
        saida += str(aux.get_codigo()) + ") " + aux.get_nome() + "\n"
        aux = aux.get_proximo()
      print(saida, "\n\n")
    else: 
      print("Não há estudantes na lista.")

  def pop_all(self):
    if not self.__inicio:
      print("\n\nLista já está vazia: \n")
      return
    self.__inicio = None
    print("Lista está vazia agora")

  def consultar(self, nome_consultado):
    if self.__inicio:
      saida = None
      lista_aux = self.__inicio
      while lista_aux:
        if lista_aux.get_nome().upper() == nome_consultado:
          saida = lista_aux.get_codigo()
        lista_aux = lista_aux.get_proximo()
    else: 
      print("Não há estudantes na lista.")
    return saida

def main():
  op = 0 
  lista = Minha_lista_encadeada_ordenada()
  while True:
    op = int(input("Opções:\n"
                   "1 - Inserir Cliente.\n"
                   "2 - Excluir Cliente.\n"
                   "3 - Consultar lista de clientes.\n"
                   "4 - Esvaziar a lista.\n"
                   "5 - Adicionar cadastros automaticamente para teste.\n"
                   "6 - Sair.\n\n"
                   "Informe opção: \n"))
    
    if op == 1:
      codigo = input("Informe o código do cliente:\n")
      nome = input("Informe o nome do cliente:\n")
      lista.push(codigo, nome)
      
    elif op == 2:
      cod_estudante = int(input("Informe o código do cliente que deseja remover:\n"))
      lista.pop(cod_estudante)
    elif op == 3:
       lista.print_all()
    elif op == 4:
         lista.pop_all()

    elif op == 5:
      lista.push(3, "Teste1")
      lista.push(2, "Teste2")
      lista.push(1, "Teste3")
      lista.push(4, "Teste4")
      lista.push(6, "Teste5")
      lista.push(5, "Teste6")
      
    elif op == 6:
      break
    else:
      print("Opção inválida.")

if __name__ == '__main__':
  main()