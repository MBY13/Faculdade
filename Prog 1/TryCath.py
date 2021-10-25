Vect_Str=[]

try:
     with open("./texto.txt", "r") as file:
         Data=file.readlines()

     for line in Data:
         Vect_Str.append("%s" % line.replace("\n", ""))
except FileNotFoundError as error:
     print("Erro1: Arquivo não encontrado: %s" % error)
except IOError as error:
     print("Erro2: Erro de entrada e saída: %s" % error)
except Exception as ex:
     print("Erro3: Erro inexperado: %s" % ex)

for i in range(0, len(Vect_Str),1):
     print("Vect_Str[%d] --> %s" % (i, Vect_Str[i])) #O comando print já põe um \n