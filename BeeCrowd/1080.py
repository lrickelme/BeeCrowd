lista = []
for i in range (100):
    n = int(input())
    lista.append(n)
    maximo = max(lista)
    posicao = lista.index(maximo) + 1
print (maximo)
print (posicao)