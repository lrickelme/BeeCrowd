N = int(input())
h = N / 3600
r = N % 3600
m = r / 60
s = r  % 60
print ("%i:%i:%i"%(h,m,s))