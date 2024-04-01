from time import sleep
h = m = c = m20 = 0
while True:
    i = int(input("Sua idade"))
    sexo = str(input("Qual seu sexo?M/F")).strip().upper()[0]
    if sexo in "M":
        h += 1
    if sexo in "F":
        m += 1
    if i > 18:
        c += 1
    if sexo in "F" and i < 20:
        m20 += 1
    sleep(0.5)
    r = str(input("Mais pessoas?")).strip().upper()
    if r in "N":
        break
print(f"{c} pessoas tem mais de 18 anos,{h} homens foram cadastrados e {m20} mulheres tem menos de 20 anos")
