print("\nDigite os valores abaixo para que seja feito o calculo de quanto você tera de valor acumulado\n")

P = float(input("Valor depositado mensalmente R$"))
I = float(input("Digite o a taxa:"))
N = int(input("Digite o numero de meses:"))

VA = (((((1+I)**N)-1)/I)*P)

print(f'\nO valor acumulado em {N} meses será de R${VA}')