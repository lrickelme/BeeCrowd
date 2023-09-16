soma_dos_valores_positivos = 0
quant_positivos = 0

while True:
    try:
        valor = float(input())
        if valor >= 0:
            quant_positivos += 1
            soma_dos_valores_positivos += valor
    except EOFError:
        break

media_dos_valores_positivos = soma_dos_valores_positivos / quant_positivos
print (f"{quant_positivos:d} valores positivos")
print (f"{media_dos_valores_positivos:.1f}")