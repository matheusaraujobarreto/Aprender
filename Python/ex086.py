m = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        m[l][c] = int(input(f"Digite um numero para posição [{l+1} e {c+1}]"))
print(m[0])
print(m[1])
print(m[2])
#ou pra deixar bonito
for l in range(0,3):
    for c in range(0,3):
        print(f"{m[l][c]}", end=" ")
    print()