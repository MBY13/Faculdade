print("\nPrograma para descobrir minutos, horas e dias \n")

S = int(input("Entre com os segundos:"))

M = round((S/60), 2)
H = round((M/60),2)
D = round((H/24),2)

print(f"\n{S} Segundos é igual à")
print(f"\n{M} minuto")
print(f"\n{H} Hora")
print(f"\n{D} Dia")