# feito por Arthur Eduardo Good
# DAD II - 2021/01

import csv

def novo_cadastro():
    #criamos um objeto de armazenamento, que sera preenchido pelo usuario
    armazenamento = {
            "codigo": int(input("Insira o codigo para cadastro: ")),
            "nome": input("Insira o nome do meio de armazenamento: "),
            "tipo": input("É um meio volátil? (S/N): "),
            "custo": float(input("Insira o custo por GB: R$")),
        }
    #abrimos o arquivo com o argumento 'a' para criar um novo arquivo caso nao exista
    #mas ao mesmo tempo, ira apenas criar uma nova linha caso ja exista
    with open(nome_arquivo, 'a', encoding='UTF8', newline='') as f:
        file = csv.DictWriter(f, armazenamento.keys())
        #escreve o header do csv
        if f.tell() == 0:
            file.writeheader()
        #escreve o conteudo do csv
        file.writerow(armazenamento)

def buscar_armazenamento():
    try:
        pesquisa = input("Insira o codigo: ")
        with open(nome_arquivo, mode='r') as csv_file:
            line_count = 0
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                #checa se o valor do codigo é o mesmo da pesquisa
                if row[0] == pesquisa:
                    print(f'Codigo: {row[0]} Nome: {row[1]} Volatil: {row[2]} Custo por GB: R${row[3]}')
                else:
                    line_count += 1
        print("Numero de consultas antes do resultado - ", line_count)
    except:
        print("Nenhum meio cadastrado!")

def imprimir_cadastros():
    try:
        with open(nome_arquivo, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                #assim excluimos o header do csv na hora de imprimir
                if line_count > 0:
                    print(f'Codigo: {row[0]} Nome: {row[1]} Volatil: {row[2]} Custo por GB: R${row[3]}')
                line_count += 1
    except:
        print("Nenhum meio cadastrado!")

def encerrar():
    #encerra o programa
    exit()

def nao_opcao():
    #opcao padrao/default, caso nao seja selecionada uma opcao valida
    print("Opção inválida!")

#define o nome do arquivo
nome_arquivo = input('Qual é o nome do arquivo CSV que você deseja criar ou abrir? ') + ".csv"

while True:
    opcao = input('\nMenu\n1-Cadastrar meio de armazenamento.\n2-Buscar meio de armazenamento.\n3-Imprimir meios de armazenamento cadastrados.\n4-Encerrar.\nOpção: ')
    #objeto com as opcoes e suas respectivas chaves
    {
        "1":  novo_cadastro,
        "2":  buscar_armazenamento,
        "3":  imprimir_cadastros,
        "4":  encerrar,
    }.get(opcao, nao_opcao)()