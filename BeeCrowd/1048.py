salario = float(input())

R1 = salario * 0.15
R2 = salario * 0.12
R3 = salario * 0.1
R4 = salario * 0.07
R5 = salario * 0.04

S1 = salario + R1
S2 = salario + R2
S3 = salario + R3
S4 = salario + R4
S5 = salario + R5

if salario <= 400:
  print (f"Novo salario: {S1:.2f}")
  print (f"Reajuste ganho: {R1:.2f}")
  print ("Em percentual: 15 %")
elif salario <= 800:
  print (f"Novo salario: {S2:.2f}")
  print (f"Reajuste ganho: {R2:.2f}")
  print ("Em percentual: 12 %")
elif salario <= 1200:
  print (f"Novo salario: {S3:.2f}")
  print (f"Reajuste ganho: {R3:.2f}")
  print ("Em percentual: 10 %")
elif salario <= 2000:
  print (f"Novo salario: {S4:.2f}")
  print (f"Reajuste ganho: {R4:.2f}")
  print ("Em percentual: 7 %")
elif salario > 2000:
  print (f"Novo salario: {S5:.2f}")
  print (f"Reajuste ganho: {R5:.2f}")
  print ("Em percentual: 4 %")