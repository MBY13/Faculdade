print("\nVamos ver o percentual de cada candidato\n")

T = int(input("Digite o total de eleitores: "))
A = int(input("Quantos votaram no primeiro? "))
B = int(input("Quantos votaram no segundo? "))
C = int(input("Quantos votaram NULO? "))

PA = int(float((100*A)/T))
PB = int(float((100*B)/T))
PC = int(float((100*C)/T))

if(A+B+C==T):
    print(f"\nO candidato A teve {PA}% dos votos")
    print(f"O candidato B teve {PB}% dos votos")
    print(f"E teve {PC}% Nulos\n")
else:
    print("\nO numero de votantes não esta igual\n")