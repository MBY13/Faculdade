# Victor Alves, Thiago A. B. Da Silva, 
# Leonardo de J. Piechontcoski, Gabriel Augustin

print("\n")
codigo = input("Digite o código do livro:\n")
autor = input("Digite o autor do livro:\n")
titulo = input("Digite o titulo do livro:\n")
arquivo = open('Arquivo.txt','a')
arquivo.write(codigo + "\n")
arquivo.write(autor + "\n")
arquivo.write(titulo + "\n\n\n\n\n\n")
print("Cadastro salvo no arquivo " + arquivo.name + " usando o modo de acesso " + arquivo.mode)
arquivo.close()