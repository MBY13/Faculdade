#A prefeitura do Rio de Janeiro abriu uma linha de crédito para os funcionários
#estatutários. O valor máximo da prestação não poderá ultrapassar 30% do salário
#bruto. Fazer um algoritmo que permita entrar com o salário bruto e o valor da
#prestação e informar se o empréstimo pode ou não ser concedido.

sb = float(input("Digite seu salario bruto R$"))
vp = float(input("Digite o valor da prestação R$"))

p = ((sb * 30)/100)

if vp <= p:
    print("SERA CONCEDIDO O EMPRESTIMO")
else:
    print("NÃO SERA CONCEDIDO O EMPRESTIMO")