c1, n1, v1 = input().split()
c2, n2, v2 = input().split()

pago1 = int(n1) * float(v1)
pago2 = int(n2) * float(v2)
pagototal = pago1 + pago2
print ("VALOR A PAGAR: R$ %.2f"%pagototal)