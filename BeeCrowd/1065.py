n1,n2,n3,n4,n5 = map(input, ["","","","",""])
nums = map(int, [n1, n2, n3, n4, n5])
pares = 0
for n in nums:
    if n % 2 == 0:
        pares += 1
print ("{} valores pares".format(pares))