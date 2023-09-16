while True:
    try:
        texto = input()
        aberturaI = True
        aberturaB = True
        textoSaida = ""
        for letra in texto:
            if letra == "_":
                if aberturaI:
                    textoSaida += "<i>"
                else:
                    textoSaida += "</i>"
                aberturaI = not aberturaI
            elif letra == "*":
                if aberturaB:
                    textoSaida += "<b>"
                else:
                    textoSaida += "</b>"
                aberturaB = not aberturaB
            else:
                textoSaida += letra

        print(textoSaida)
    except EOFError:
        break