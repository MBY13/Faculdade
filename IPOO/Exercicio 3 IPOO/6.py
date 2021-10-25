print ("\nm = Masculino")
print ("f = Feminino")
print ("fim = encerra")

fem = 0

sexo = input("\nDigite qual o sexo da pessoa:")

while sexo != "fim":
    if sexo == "f":
        fem +=1
    sexo = input("\nDigite qual o sexo da pessoa:")

if sexo == "fim":
    print("\nO programa foi encerrado")
    print(f"Foi digitados {fem} pessoas do sexo feminino")