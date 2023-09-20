valor_inicial = saque = int(input())

cedulas_100 = saque // 100
saque = saque % 100
cedulas_50 = saque // 50
saque = saque % 50
cedulas_20 = saque // 20
saque = saque % 20
cedulas_10 = saque // 10
saque = saque % 10
cedulas_5 = saque // 5
saque = saque % 5
cedulas_2 = saque // 2
saque = saque % 2
cedulas_1 = saque // 1
saque = saque % 1

print(valor_inicial)
print("{} nota(s) de R$ 100,00".format(cedulas_100))
print("{} nota(s) de R$ 50,00".format(cedulas_50))
print("{} nota(s) de R$ 20,00".format(cedulas_20))
print("{} nota(s) de R$ 10,00".format(cedulas_10))
print("{} nota(s) de R$ 5,00".format(cedulas_5))
print("{} nota(s) de R$ 2,00".format(cedulas_2))
print("{} nota(s) de R$ 1,00".format(cedulas_1))