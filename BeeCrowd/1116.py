n = int(input())
for i in range(n):
    x, y = map(int,input().split())
    if y == 0:
      print ("divisao impossivel")
    else:
        divisao = x/y
        if divisao > 0 or divisao < 0 :
            print (divisao)
        else:
            print ("0.0")