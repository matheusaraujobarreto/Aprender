def fatorial(n, op=False):
    f = 1
    for c in range(n, 0, -1):
        if op:
            print(c, end="")
            if c > 1:
                print(" x ", end="")
            else:
                print(" = ", end="")
        f *= c
    if not op:
        return f"O fatorial de {n} é {f}"
    else:
        return f


# Codigo principal
n = int(input("Digite o valor"))
r = str(input("Quer ver o passo a passo?"))
if r in "Ss":
    r = True
else:
    r = False
print(fatorial(n, r))
