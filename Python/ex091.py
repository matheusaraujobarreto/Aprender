from random import randint
from time import sleep
from operator import itemgetter
d = {"Jogador1":randint(1,6),
     "Jogador2":randint(1,6),
     "Jogador3":randint(1,6),
     "Jogador4":randint(1,6)}
rank = {}
for k, v in d.items():
    print(f"O {k} tirou {v}")
    sleep(1)
rank = sorted(d.items()),
#não da pra fazer esse