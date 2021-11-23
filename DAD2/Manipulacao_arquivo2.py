# Estudantes: Samuel T. Fitzlaff, Matheus H. E. Stelzner,
# Luis F. dos S. Pires, Alex Bassani.

class CadLivro:
    def __init__(self):
        self.FileName = input("Digite o nome do arquivo: ")  # Input do nome do arquivo

    def Cadastra(self):
        File = open(self.FileName + ".txt", "a")  # Abre o arquivo no modo append. O arquivo será criado caso não exista
        wr = True
        while wr:  # Salva o livro no arquivo aberto separando cada item por ";"
            Id = input("Digite o id do livro: ")
            Titulo = input("Digite o nome do livro: ")
            Genero = input("Digite o genero do livro: ")
            Ano = input("Digite o ano de publicação: ")
            Editora = input("Digite o nome da editora: ")
            Autor = input("Digite o nome do autor: ")
            File.write(Id + ";" + Titulo + ";" + Genero + ";" + Ano + ";" + Editora + ";" + Autor + "\n")

            wr = False
            Continua = input("Deseja cadastrar mais um livro? (Y/N)\n")
            if Continua == "Y" or Continua == "y":  # Caso o usuario digite "y", mais um livro será cadastrado
                wr = True

        File.close()  # Fecha o arquivo

    def Imprime(self):
        File = open(self.FileName + ".txt", "r")  # Abre o arquivo no modo read
        FileText = File.read()  # Salva o conteudo do arqivo em uma variável

        print("Livros:\n\n" + FileText.replace(";", " - "))  # Imprime substituindo os ";" por " - "

        File.close()  # Fecha o arquivo

        input("Pressione a tecla enter para continuar")  # Aguarda input do usuário para retornar

    def Pesquisa(self):
        TestID = int(input("Digite o id do livro: "))  # Input do id desejado

        File = open(self.FileName + ".txt", "r")  # Abre o arquivo no modo read
        FileText = File.read()  # Salva o conteudo do arqivo em uma variável

        FileSplit = FileText.splitlines()  # Salva cada linha do arquivo numa posição em um vetor

        FoundID = False
        for out in FileSplit:  # Loop que passa por cada linha
            if int(out.partition(";")[0]) == TestID:  # Compara o id salvo no arquivo com o input do usuário
                print(out.replace(";", " - "))  # Imprime a linha encontrada substituindo os ";" por " - "
                FoundID = True
                break

        if FoundID is False:  # Caso não for encontrado um id no arquivo
            print("\nID não cadastrado!")

        File.close()  # Fecha o arquivo
        input("Pressione a tecla enter para continuar")  # Aguarda input do usuário para retornar

#####

cad = CadLivro()

m = True
while m:  # Menu
    try:
        print("\n\n1 para cadastrar livro\n2 para imprimir lista de livros\n3 para pesquisar livro\n4 para sair\n")
        sw = int(input("Digite a opção: "))

        if sw == 1:
            cad.Cadastra()  # Cadastra livro no arquivo
        elif sw == 2:
            cad.Imprime()  # Imprime o cadastro
        elif sw == 3:
            cad.Pesquisa()  # Pesquisa por id
        else:
            m = False  # sai do menu

    except Exception:  # exceção caso o usuário digite algum valor incorreto
        print("Erro Desconhecido\n")
        input("Pressione a tecla enter para continuar")  # Aguarda input do usuário para retornar

