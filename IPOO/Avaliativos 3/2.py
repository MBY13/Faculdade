#Exercício 2) (parecida com exercício 11 dos slides) Implemente um programa que converta da notação
#de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M.
#Outro exemplo, converte 8:30 em 8:30 A.M. A entrada é dada em dois inteiros (horas e minutos).
#Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as
#vezes que desejar.

def Horas(H,M):
    if H < 12:
        print (f"O Horáro convertido é {H}:{M} A.M") 
    else:
        h = 12 - H 

        h = h *-1
        print (f"O Horário convertido é {h}:{M} P.M")
######################################################

while True :

    horas = int(input("Digite as horas:"))
    minutos = int(input("Digite os minutos:"))

    Horas(horas,minutos)

    cont = input("Digite N para encerrar e S para continuar:")

    if cont == "N":
        break
    if cont == "n":
        break