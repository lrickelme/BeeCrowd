x = int(input())
y = int(input())

if y>x:
    temp = x
    x = y
    y = temp
soma = 0
for i in range(y+1,x):
    if i % 2 != 0:
        soma += i
print (soma)