n = (int(input("Digite um numero")), int(input("Digite um numero")), int(input("Digite um numero")),
    int(input("Digite um numero")))
print(f"O valor 9 apareceu {n.count(9)} vezes")
if 3 in n:
    print(f"O 3 apareceu primeiro na posição {n.index(3)}")
else:
    print("O numero 3 não apareceu")
print("Os numeros pares foram")
for c in n:
    if n % 2 == 0:
        print(n)
#Os pares n ta dando
