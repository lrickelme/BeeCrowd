a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
arr = [a,b,c,d,e]
par = 0
impar = 0
positivo = 0
negativo = 0

for i in arr:
    if i < 0:
        negativo += 1
    if i > 0:
        positivo += 1
    if i % 2 == 0:
        par += 1
    if i % 2 != 0:
        impar += 1
print (f"{par} valor(es) par(es)")
print (f"{impar} valor(es) impar(es)")
print (f"{positivo} valor(es) positivo(s)")
print (f"{negativo} valor(es) negativo(s)")