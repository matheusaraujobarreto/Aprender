s = c = b = 0
pb = ""
while True:
    p = str(input("Qual produto"))
    v = float(input("Valor do produto"))
    r = str(input("Quer continuar"))
    if v > 1000:
        c += 1
    if c == 1:
        b = v
        pb = p
    else:
        if v < b:
            b = v
            pb = p
    s += v
    if r in "Nn":
        break
print(f"\033[04;31mO total foi {s}, {c} produtos custavam mais de 1000 reais e o mais barato é {pb} que custou {b}\033[m")
