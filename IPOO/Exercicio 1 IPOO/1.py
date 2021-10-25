# Faça um programa que leia quatro números informados pelo usuário e que depois imprima a média ponderada, sabendo-se
#que os pesos são respectivamente: 1, 2, 3 e 4:

print ("\n Abaixo digite as notas para que seja feita a media ponderada do aluno\n")

nota1 = float(input("Digite a Nota 1º:"))
nota2 = float(input("Digite a Nota 2º:"))
nota3 = float(input("Digite a Nota 3º:"))
nota4 = float(input("Digite a Nota 4º:"))

media = float((((nota1 * 1)+(nota2 * 2)+(nota3 * 3)+(nota4 * 4) ) / (1+2+3+4) ))

print ("A media ponderada foi:" , media)