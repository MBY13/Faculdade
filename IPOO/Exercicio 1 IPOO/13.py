print("\nVamos descobrir seu IMC\n")

P = float(input("Digite seu peso: "))
A = float(input("Digite sua Altura:"))

IMC = round((P/(A*A)),2)

print(f"\nSeu IMC é {IMC}\n")