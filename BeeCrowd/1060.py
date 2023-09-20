quant_positivos = 0

while True:
    try:
        valor = float(input())
        if valor >= 0:
            quant_positivos += 1
            
    except EOFError:
        break

print (f"{quant_positivos:d} valores positivos")