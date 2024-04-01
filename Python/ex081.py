l = []
c = 0
while True:
    v = int(input("Digite um valor"))
    c += 1
    r = str(input("Mais um?S/N"))
    if r[0] in "Ss":
        l.append(v)
    else:
        l.append(v)
        break
l.sort(reverse=True)
print(f"Foram digitados os tais {c} numeros\n",l)
if 5 in l:
    print("O valor 5 aparece na lista")
else:
    print("O valor 5 não aparece na lista")
