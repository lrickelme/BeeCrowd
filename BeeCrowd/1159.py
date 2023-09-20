x = int(input())
while x != 0:
    contador = 0
    for i in range(x, x+10):
        if i%2 == 0:
            contador += i
    print (contador)
    x = int(input())