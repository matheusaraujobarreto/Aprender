from time import sleep
d = {}
d["nome"] = str(input("Nome"))
d["jogos"] = int(input("Quantas partidas?"))
g = []
for c in range(0,d["jogos"]):
    g.append(int(input(f"Quantos gols fez na {c+1}ª partida?")))
print("-="*20)
d["gols"] = g[:]
d["totgols"] = sum(g)
print("    Ficha")
for k, v in d.items():
    print(f"{k}: {v}")
print("-="*20)
print(f"O jogador {d["nome"]} jogou {d["jogos"]} partidas e fez {d["totgols"]} gols, sendo:")
for p, g in enumerate(d["gols"]):
    print(f"{g} gols na partida {p+1}")
    sleep(1)
print("-="*20)
