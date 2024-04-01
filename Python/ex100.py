from random import randint
l = []


def sorte():
    for c in range(0,5):
        l.append(randint(0,20))
    print("Os numeros sorteados foram", l)


def somapar():
    c = 0
    print("Os numeros pares são:")
    for n in l:
        if n % 2 == 0:
            print(f"{n} ", end="")
            c += n
    print(f" e a soma deles é {c}")

sorte()
somapar()
