#(idem exercício 12 dos slides) Implemente um programa que use a função valorPagamento
#para determinar o valor a ser pago por uma prestação de uma conta. O programa deverá solicitar ao
#usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função
#valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O
#programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a
#pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a
#prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a
#quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte
#forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de
#multa, mais 0,1% de juros por dia de atraso.

def valorPagamento(Valor, Dias):
    if Dias == 0:
        return Valor 
    else: 
        multa = (3 * 100) / Valor
        juros = (10 /  Valor) * Dias 

        parcela  = Valor + juros + multa
        return parcela  
################################################
cont = 0 
total = 0
while True : 

    print ("\nDigite 0 para encerrar ")
    Prest = float(input("Digite o valor da parcela R$"))
    
    if Prest == 0:
        break 
    
    atraso = int(input("Digite quantos dias teve de atraso:"))

    print (f"A parcela é de R${valorPagamento(Prest , atraso)}")
    
    cont += 1 
    total += valorPagamento(Prest, atraso)

print ("Pagamentos do dia")
print (f"Quantidade de pagamentos {cont}")
print (f"Valor total pago R${total}")