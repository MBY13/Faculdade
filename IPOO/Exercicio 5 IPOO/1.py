#Escreva uma função que retorne o maior de dois números.
#Exemplo de valores esperados:
#maior(5,6) = 6
#maior(2,1) = 2
#maior(7,7) = 7

def maiorvalor (x,y):
    if x>=y:
        return x
    else:
        return y

num = int(input("Digite um numero:"))
num2 = int(input("Digite um numero:"))

maior = maiorvalor(num,num2)

print(f"O maior numero digitado foi {maior}")