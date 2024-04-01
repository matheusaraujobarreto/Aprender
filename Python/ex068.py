import random
from time import sleep
print("Vamos jogar par ou impar")
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s = 0
while True:
    c = random.choice(l)
    j = str(input("Escolha par ou impar. P/I")).upper()[0]
    n = int(input("Seu numero"))
    s = c + n
    if j == "P":
        if s % 2 == 0:
            print("E...")
            sleep(0.5)
            print(f"{c}+{n}={s} que é par")
        else:
            print("E...")
            sleep(0.5)
            print(f"{c}+{n}={s} que é impar")
            break
    if j == "I":
        if s % 2 != 0:
            print("E...")
            sleep(0.5)
            print(f"{c}+{n}={s} que é impar")
        else:
            print("E...")
            sleep(0.5)
            print(f"{c}+{n}={s} que é par")
            break
print("\033[31mGame Over\033[31m")