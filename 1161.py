def fatorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

while True:
    try:
        m, n = map(int, input().split())
        fatm = fatorial(m)
        fatn = fatorial(n)
        fat = fatm + fatn
        print(fat)
    except EOFError:
        break
