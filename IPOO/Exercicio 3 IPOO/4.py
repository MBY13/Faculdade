x = 0
y = 0
z = 0
soma = 0

while x<5 and y<10:
    x += 1
    y += 2

    nota1 = float(input("Digite a primeira nota:"))
    nota2 = float(input("Digite a segunda nota:"))

    media = round((nota1 + nota2)/2)
    soma = soma + media 

    if media >= 7.0:
        z +=1
    
    print(f"A media do aluno {x} é {media}\n")

soma1 = soma / 2 

print(f"Teve {z} alunos com media maior ou igual a 7 ")
print(f"E a media da turma foi {soma1}\n")