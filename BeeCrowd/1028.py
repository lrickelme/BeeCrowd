import math

n = int(input())
for i in range(n):
    f1, f2 = map(int, input().split())
    mdc = math.gcd(f1, f2)
    print(mdc)
