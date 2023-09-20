x = int(input())
y = int(input())
soma = 0
if y>x:
    temp = x
    x = y
    y = temp
for i in range(y,x+1):
    if i % 13 != 0:
        soma += i
print(soma)