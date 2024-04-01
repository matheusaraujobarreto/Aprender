def leiaint(msg):
    ok = False
    v = 0
    while True:
        n = str(input("Digite um numero"))
        if n.isnumeric():
            v = int(n)
            ok = True
        else:
            print(f"\033[31mErro! Não é um numero\033[m")
        if ok:
            break
    return v


v = leiaint("Digite um numero")
print(f"Você digitou o numero {v}")
