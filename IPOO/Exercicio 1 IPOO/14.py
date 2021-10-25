print("\nVamos fazer calculos sobre sua promoção de 25%")

A = int(input("Digite quantos apartamentos tem no Hotel:"))
B = float(input("Digite o valor para o final de semana completo R$"))

D = ((B * 25)/100)
VP = (B - D)
VP100 = ( VP * A)
V70 = ((A*70/100))
VP70= (VP * V70)
D1 = (B * A)
VS = (VP100 - D1)

print(f"\nO valor da Diaria com promoção será de R${VP}")
print(f"O valor arrecadado com 100% de ocupação sera de R${VP100}")
print(f"O valor arrecadado com 70% de ocupação sera de R${VP70}")
print(f"Em virtude a promoção voce deixou de arrecadar R${VS}\n")