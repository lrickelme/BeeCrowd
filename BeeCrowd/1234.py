while True:
    try:
        ent = input()
        arr = []
        count = -1
        for letra in ent:
            if not letra == " ":
                count = count + 1
                
            if count % 2 == 0:
                arr.append(letra.upper())
            else:
                arr.append(letra.lower())
        
        sai = "".join(arr)
        
        print (sai)
    except EOFError:
        break