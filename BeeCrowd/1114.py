senha = "2002"
while True:
    try:
        num = input()
        if num == senha:
            print ("Acesso Permitido")
            break
        else:
            print ("Senha Invalida")
    except EOFError:
        break