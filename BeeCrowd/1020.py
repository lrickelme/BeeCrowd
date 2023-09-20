x = int(input())
anos= x//365
sobra = x%365
meses = sobra //30
dias = sobra%30
print("%i ano(s)"%anos)
print("%i mes(es)"%meses)
print("%i dia(s)"%dias)