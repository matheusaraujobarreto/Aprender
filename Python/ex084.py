l = []
d = []
c = 0
maior = menor = 0
while True:
    d.append(str(input("Nome")))
    d.append(int(input("Peso")))
    if c == 0:
        maior = menor = d[1]
    else:
        if d[1] > maior:
            maior = d[1]
        if d[1] < menor:
            menor = d[1]
    c += 1
    r = str(input("Mais alguem?"))
    l.append(d[:])
    d.clear()
    if r in "Nn":
        break
print(f"{c} pessoas cadastradas")
print("As pessoas mais pesadas foram ",end="")
for p in l:
    if p[1] == maior:
        print(f'{p[0]} com {p[1]}KG')
print("As pessoas mais leves foram ",end="")
for p in l:
    if p[1] == menor:
        print(f"{p[0]} com {p[1]}KG")
