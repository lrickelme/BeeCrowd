idade = 0
contador = 0

while True:
    try:
        entrada = int(input())
        if entrada < 0:
            break
        else:
            idade += entrada
            contador += 1
    
    except EOFError:
        break

if contador > 0:
    media = idade / contador
    print(f"{media:.2f}")
else:
    print("Nenhum dado foi inserido.")