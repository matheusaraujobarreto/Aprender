l = []
for c in range(0,5):
    n = int(input("Digite um valor"))
    if c == 0 or n > l[-1]:
        print("Adicionado na ultima posição")
        l.append(n)
    else:
        p = 0
        while p < len(l):
            if n <= l[p]:
                l.insert(p,n)
                print(f"Adicionado na posição {p}")
                break
            p += 1
print(l)
