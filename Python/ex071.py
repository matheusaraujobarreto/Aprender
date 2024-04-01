c = 50
n = int(input("Qual valor a ser sacado?"))
s = n
t = 0
while True:
    if s >= c:
        s -= c
        t += 1
    else:
        print(f"{t} cedulas de {c} R$")
        if c == 50:
            c = 20
        elif c == 20:
            c = 10
        elif c == 10:
            c = 1
        t = 0
        if s == 0:
            break
#Essa é fudida
