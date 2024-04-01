l = []
while True:
    nome = str(input("Nome"))
    n1 = int(input("Nota 1"))
    n2 = int(input("Nota 2"))
    media = (n1 + n2)/2
    l.append([nome, [n1, n2], media])
    r = str(input("Mais alguem?"))
    if r[0] in "Nn":
        break
for n, a in enumerate(l):
    print(f"As notas de {a[0]} foram {a[1]} e sua média foi de {a[2]}.")
while True:
    aluno = int(input("Qual aluno quer saber a nota? 999 Para nenhum"))
    if aluno == 999:
        break
    if aluno <= len(l)-1:
        print(f"Notas de {l[aluno][0]} são {l[aluno][1]}")
        