#Escreva um programa que pergunte a distância que um passageiro deseja percorrer em
#km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200
#km, e R$ 0,45 para viagens mais longas.

km = float(input("Digite quantos KM tem a viagem : "))

if km <=200:
    soma = round((km * 0.50),2)
    print(f"Você tera que pagar R${soma}")
else:
    soma = round((km * 0.45),2)
    print(f"Você tera que pagar R${soma}")