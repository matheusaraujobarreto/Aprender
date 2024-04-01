from time import sleep
d = {}
l = []
while True:
    d.clear()
    d["nome"] = str(input("Nome"))
    d["jogos"] = int(input("Quantas partidas?"))
    g = []
    for c in range(0,d["jogos"]):
        g.append(int(input(f"Quantos gols fez na {c+1}ª partida?")))
    print("-="*20)
    d["gols"] = g[:]
    d["totgols"] = sum(g)
    l.append(d.copy())
    r = str(input("Outro jogador?S/N"))
    if r in "Nn":
        break
print('    Ficha')
for k, v in enumerate(l):
    print(k )
    for s in v.values():
        print(f"{str(s)} ",end="")




#for k, v in d.items():
 #   print(f"{k}: {v}")
#print("-="*20)
#print(f"O jogador {d["nome"]} jogou {d["jogos"]} partidas e fez {d["totgols"]} gols, sendo:")
#for p, g in enumerate(d["gols"]):
 #   print(f"{g} gols na partida {p+1}")
  #  sleep(1)
#print("-="*20)
