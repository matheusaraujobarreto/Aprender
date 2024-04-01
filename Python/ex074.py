from random import randint
maior = menor = 0
n = randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)
print(f"Os valores sorteados foram {n}")
print(f"O maior valor foi {sorted(n)[-1]} e o menor foi {sorted(n)[0]}")
#ou print(f"O maior valor foi {max(n)} e o menor foi {min(n)}")

