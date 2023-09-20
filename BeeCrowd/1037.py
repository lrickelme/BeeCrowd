num1 = float(input())
if num1 >= 0 and num1 <= 25:
    print("Intervalo [0,25]")
elif num1 > 25 and num1 <= 50:
    print("Intervalo (25,50]")
elif num1 > 50 and num1 <= 75:
    print("Intervalo (50,75]")
elif num1 > 75 and num1 <= 100:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")