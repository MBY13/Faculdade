val = float(input('Valor produto: '))
qua = int(input('Quantidade de produtos comprados '))

if qua <= 5:

    print("Esse é o valor para ser pago" ,val - (qua*val)*(3/100))

if qua > 5 and qua <= 10 :

    print("Esse é o valor para ser pago" ,val - (qua*val)*(5/100))

if qua > 10:

    print("Esse é o valor para ser pago" ,val - (qua*val)*(7/100)) 