n = int(input())
antes = 0
depois = 0 
lista = [0]*n
for i in range (0, n):
    if i <= 1:
         lista[i] = i
    else:
        lista[i] = lista[i - 1] + lista[i - 2]
        
    
    if i == n - 1:
        print((lista[i]), end='\n')
    else:
        print((lista[i]), end=' ')