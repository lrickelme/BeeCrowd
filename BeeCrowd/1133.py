x = int(input())
y = int(input())
if y>x:
    temp = x
    x = y
    y = temp
for i in range(y+1,x):
    if i%5 == 2 or i%5 == 3:
      print(i)