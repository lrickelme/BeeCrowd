while True:
    try:
        velo, temp = map(int,input().split())
        afinal = (velo*temp)*2
        print (afinal)
    except EOFError:
        break