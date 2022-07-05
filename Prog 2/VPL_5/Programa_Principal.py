import sys
import json

##################################################

## Questão 01: (Crie o código necessário para ler os dados do arquivo JSON
##              O arquivo já é fornecido e possui o nome: "Banco_Alunos.json.txt")

## Questão 02: (Crie o código necessário para imprimir na tela os dados das cidades)

## Questão 03: (Crie o código necessário para imprimir na tela os dados dos alunos)

## Questão 04: (Crie o código necessário para encerrar o programa)

##################################################
try:
    with open('Banco_Alunos.json.txt', 'r') as json_file:
        Data = json.load(json_file)
    for p in Data['Cidade']:
        print('Cidade_Key: ' + p['Cidade_Key'])
        print('Cidade_Nome: ' + p['Cidade_Nome'])
        print('Cidade_Abrev: '+ p['Cidade_Abrev'])
        print('')
    for p in Data['Aluno']:
        print('Aluno_Key: ' + p['Aluno_Key'])
        print('Cidade_Key: ' + p['Cidade_Key'])
        print('Aluno_Nome: ' + p['Aluno_Nome'])
        print('Aluno_Idade: '+ p['Aluno_Idade'])
        print('') 
except FileNotFoundError as error:
    print("Erro1: Arquivo no encontrado: %s" % error)
except IOError as error:
    print("Erro2: Erro de entrada e sada: %s" % error)
except Exception as ex:
    print("Erro3: Erro indesperado: %s" % ex)
sys.exit(0)
                