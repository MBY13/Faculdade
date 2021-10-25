A=[]
B=[]
x=0

while x < 5:
    A.append(int(input("Digite um numero:")))
    x+=1
x=0
while x < 5:
    B.append(int(input("Digite um numero:")))
    x+=1
d = (A+B)

print(*set(d))