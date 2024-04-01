n = int(input("Diga o primeiro termo da PA"))
r = int(input("Diga a razão da PA"))
N10 = n + (10-1) * r #Usando a formula de PA: An = A1 + (n-1)*r
for c in range(n, N10+r, r):
    print('{} '.format(c), end="> ")
print("FIM")
