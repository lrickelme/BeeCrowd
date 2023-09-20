h1, m1, h2, m2 = map(int, input().split())

if h1 == h2 and m1 == m2:
    horas = 24
    minutos = 0
else:
    horas = h2 - h1
    minutos = m2 - m1
    if horas < 0:
        horas += 24
    if minutos < 0:
        minutos += 60
        horas -= 1
    if horas < 0:
        horas += 24
    
print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")