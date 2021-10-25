from typing import List

class Estudante:
   def __init__(self,matricula,nota1,nota2,nota3):
      self.__Matricula = matricula
      self.__Nota1 = nota1
      self.__Nota2 = nota2
      self.__Nota3 = nota3
      self.Media()

   def set_matricula(self,matricula):
      self.__Matricula = matricula
   def get_matricula(self):
      return self.__Matricula

   def Media(self):
      self.media = (self.__Nota1 + self.__Nota2 + self.__Nota3)/3
      return self.media
      

def main():
   operacao = "0"
   Lista = []

   while True:
      operacao = input("\n\nOpções disponiveis:\n"
                           "1-Inserir as Informações do Aluno\n"
                           "2-Lista dos estudantes aprovados\n"
                           "3-Lista dos estudantes em exame\n"
                           "4-Ordena estudantes em ordem crescente por média\n"
                           "5:\n"
                              "    A- Estudante com maior média\n"
                              "    B- Estudante com menor média\n"
                           "6-Sair\n"
                           "Digite a operação:")
      if operacao == "1":

         matricula = int(input("Digite a matrícula do aluno(Digite 0 para encerrar):"))
         while matricula > 0:
            nota1 = float(input("Digite a 1º Nota(com .00):"))
            nota2 = float(input("Digite a 2º Nota(com .00):"))
            nota3 = float(input("Digite a 3º Nota(com .00):"))

            aluno = Estudante(matricula,nota1,nota2,nota3)
            Lista.append(aluno)
            matricula = int(input("Digite a matrícula do aluno(Digite 0 para encerrar):"))

      elif operacao == "2":
         for estudante in Lista:
            if estudante.Media() >= 7 :
               print(estudante.get_matricula() , "-" , estudante.Media())

      elif operacao == "3":
         for estudante in Lista:
            if estudante.Media() < 7 :
               print(estudante.get_matricula() , "-" , estudante.Media())

      elif operacao == "4":
         n = len(Lista)-1
         for i in range(n):
            for j in range(n):
               if Lista[j].Media() > Lista[j + 1].Media():
                  auxiliar = Lista[j]
                  Lista[j] = Lista[j + 1]
                  Lista[j + 1] = auxiliar
            n -= 1
      
      elif operacao == "5":
         operacao = input("A- Estudante com maior média\n"
                          "B- Estudante com menor média\n"
                          "Digite a operação:")
         if operacao == "A" or operacao == "a":
             print(f"Aluno com a maior média:  {Lista[-1].get_matricula()} Média = {Lista[-1].Media()}\n")
                       
         if operacao == "B" or operacao == "b":
            print(f"Aluno com a menor média:  {Lista[0].get_matricula()} Média = {Lista[0].Media()}\n")  

      elif operacao == "6":
         break

      else:
         print("Digite uma opção valida")

if __name__ == '__main__':
    main()