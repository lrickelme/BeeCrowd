S = 0
divisor = 1
for i in range(1, 39,2):
    S += i / divisor
    divisor *= 2
print(f"{S:.2f}")