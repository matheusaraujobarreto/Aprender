m = [[0,0,0],[0,0,0],[0,0,0]]
s = stc = sl = 0
for l in range(0,3):
    for c in range(0,3):
        m[l][c] = int(input(f"Digite um numero para posição [{l+1} e {c+1}]"))
        if m[l][c] % 2 == 0:
            s += m[l][c]
print("~="*25)
for l in range(0,3):
    for c in range(0,3):
        print(f"{m[l][c]}", end=" ")
    print()
print("~="*25)
for l in range(0,3):
    stc += m[l][2]
for c in range(0,3):
    if c == 0:
        sl = m[1][c]
    elif m[1][c] > sl:
        sl = m[1][c]
print(f"A soma dos valores pares é {s}\nA soma dos numeros da terceira coluna é {stc}\nO maior valor da 2 linha é {sl}.")
print("~="*25)
