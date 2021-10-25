print("\nVamos descobrir quantos degraus tem na escada\n")

A = float(input("Digite quanto de altura tem cada degrau(cm):"))
B = float(input("Digite qual a altura total da escada(cm):"))

X = int(float(round((B / A),0)))

print(f"\nNo total terá {X} Degraus ")