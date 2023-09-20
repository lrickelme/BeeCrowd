def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num_testes = int(input())

for _ in range(num_testes):
    x = int(input())
    if eh_primo(x):
        print(f"{x} eh primo")
    else:
        print(f"{x} nao eh primo")