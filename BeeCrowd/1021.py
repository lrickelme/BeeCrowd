valor = float(input())
notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.5, 0.25, 0.1, 0.05, 0.01]
qtd_notas = []
qtd_moedas = []

for nota in notas:
    qtd = int(valor / nota)
    qtd_notas.append(qtd)
    valor -= qtd * nota

for moeda in moedas:
    qtd = int(round(valor, 2) / moeda)
    qtd_moedas.append(qtd)
    valor = round(valor - qtd * moeda, 2)

print("NOTAS:")
for i in range(len(notas)):
    print("{} nota(s) de R$ {:.2f}".format(qtd_notas[i], notas[i]))

print("MOEDAS:")
for i in range(len(moedas)):
    print("{} moeda(s) de R$ {:.2f}".format(qtd_moedas[i], moedas[i]))