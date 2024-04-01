l = [[], []]
for c in range(0,7):
    n = int(input("Digite um valor"))
    if n % 2 == 0:
        l[0].append(n)
    else:
        l[1].append(n)
print(f"Os valores pares foram {l[0]}\nE os impares foram {l[1]}")
