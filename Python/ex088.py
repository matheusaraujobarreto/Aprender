from random import randint
from time import sleep
l = list()
c = 0
jogos = list()
nj = int(input("Quantos jogos da mega você quer?"))
t = 1
while t <= nj:
    c = 0
    while True:
        n = randint(1,60)
        if n not in l:
            l.append(n)
            c += 1
        if c >= 6:
            break
    l.sort()
    jogos.append(l[:])
    l.clear()
    t += 1
print(f"Sorteando {nj} jogos")
sleep(1)
for v, l in enumerate(jogos):
    print(f"Jogo {v+1}: {l}")
    sleep(1)
print("Boa sorte nos seus jogos")
