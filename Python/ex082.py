l = []
p = []
i = []
while True:
    l.append(int(input("Digite um valor")))
    r = str(input("Quer outro?S/N"))
    if r[0] in "Nn":
        break
for v in l:
    if v % 2 == 0:
        p.append(v)
    else:
        i.append(v)
l.sort()
print(f"Você escreveu os numeros {l}\nOs pares são {p}\nE os impares são {i}")