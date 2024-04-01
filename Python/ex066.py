c = 0
s = 0
while True:
    n = int(input("Digite um numero"))
    if c == 1:
        print("Para parar coloque 999")
    if n == 999:
        break
    c += 1
    s += n
print(f"A soma de todos os {c} numeros foi {s}.")
