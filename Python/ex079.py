n = []
while True:
    v = int(input("Digite um valor"))
    if v not in n:
        n.append(v)
    else:
        print("Valor duplicado não adicionado")
    r = str(input("Quer mais algum?S/N")).strip().upper()
    if r == "N":
        break
n.sort()
print(n)
