inicial  = float(input("\nDigite o valor inicial de deposito:"))
taxa = float(input("Digite a taxa de juros (%):"))
x= 0
mes = inicial

while x <=12:
    x+=1
    juros = ((mes * taxa)/100)
    mes = round ((inicial + juros),2) 
    print(f"\nNo mes {x} seu saldo é de {mes}")

ano = round ((mes - inicial))    
print(f"\nNo final de um ano o usuario teve {ano} de juros\n")