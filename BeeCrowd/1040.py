N1, N2, N3, N4 = map(float, input().split())

media = ((N1*2) + (N2*3) + (N3*4) + N4)/10

if media >=7:
    print (f"Media: {media:.1f}")
    print ("Aluno aprovado.")
elif media <5:
    print (f"Media: {media:.1f}")
    print ("Aluno reprovado.")
elif media >= 5 and media < 6.9:
    print (f"Media: {media:.1f}")
    print ("Aluno em exame.")
    nota = float(input())
    print (f"Nota do exame: {nota:.1f}") 
    median = (media + nota) / 2
    if median >= 5:
        print ("Aluno aprovado.")
    else:
        print ("Aluno reprovado.")
    print (f"Media final: {median:.1f}")