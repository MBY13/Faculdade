import sys
import json
from Data import Data
##################################################

## Questo 03: (Crie o cdigo necessrio para gravar os dados em arquivo JSON
##              Salvar os dados em um arquivo com nome: "Banco_Alunos.json.txt")

try:
    print("Gravando arquivo: 'Banco_Alunos.json.txt'...")
    with open('Banco_Alunos.json.txt', 'w') as outfile:
        json.dump(Data, outfile, indent=4)
    print("Ok.")
except FileNotFoundError as error:
    print("Erro1: Arquivo no encontrado: %s" % error)
except IOError as error:
    print("Erro2: Erro de entrada e sada: %s" % error)
except Exception as ex:
    print("Erro3: Erro inexperado: %s" % ex)

## Questo 04: (Crie o cdigo necessrio para encerrar o programa)
sys.exit(0)


##################################################