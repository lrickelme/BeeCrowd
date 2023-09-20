soma = 0
notas = 0

while notas < 2:
    n = float(input())
    if n >= 0 and n <= 10:
        soma += n
        notas += 1
    else:
        print ("nota invalida")
    ms = soma / 2
print (f"media = {ms}")