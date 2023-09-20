n = int(input())
for i in range(n):
  n1 = input()
  soma = 0
  for c in n1:
    if c == '1':
      soma += 2
    elif c == '2':
      soma += 5
    elif c == '3':
      soma += 5
    elif c == '4':
      soma += 4
    elif c == '5':
      soma += 5
    elif c == '6':
      soma += 6
    elif c == '7':
      soma += 3
    elif c == '8':
      soma += 7
    elif c == '9':
      soma += 6
    elif c == '0':
      soma += 6
  print (f"{soma} leds")