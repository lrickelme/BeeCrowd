n = int(input())
cont_d = 0
cont_f = 0
for i in range(n):
    x = int(input())
    if x >= 10 and x <=20:
        cont_d +=1
    else:
        cont_f +=1
        
print (f"{cont_d} in")
print (f"{cont_f} out")