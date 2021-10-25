print("\nVamos ver como ter lucro no teatro ")

CE = float(input("Digite o custo do espetaculo R$"))
PE = float(input("Digite o valor do ingresso R$"))

QC = int(float(CE / PE))
A = ((CE * 23)/100)
ACE = (CE + A)
QCA = int(float(ACE / PE))

print(f"\nVocê terá que vender {QC} ingressos para não ter prejuizo")
print(f"\nVocê terá que vender {QCA} ingressos para ter um lucro de 23%")