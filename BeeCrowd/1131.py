vitoria_inter = 0
vitoria_gremio = 0
empates = 0
contador = 0
while True:
  inter, gremio = map(int, input().split())
  contador += 1
  if gremio > inter:
    vitoria_gremio += 1
  elif gremio == inter:
    empates += 1
  else: 
    vitoria_inter += 1
  print ("Novo grenal (1-sim 2-nao)")
  novo = int(input())
  if novo == 2: 
    break
print (f"{contador} grenais")
print (f"Inter:{vitoria_inter}")
print (f"Gremio:{vitoria_gremio}")
print (f"Empates:{empates}")
if vitoria_gremio > vitoria_inter:
  print ("Gremio venceu mais")
elif vitoria_inter > vitoria_gremio:
  print ("Inter venceu mais")
else:
  print ("Não houve vencedor")