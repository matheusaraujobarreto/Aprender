def ficha(nome="", gols=0):
    if nome == "" and gols != 0:
        print(f"O jogador desconhecido marcou {gols} gols.")
    if gols == 0:
        print(f"O jogador {nome} não marcou gols")
    if nome == "" and gols == "":
        print(f"O jogador desconhecido não marcou gols")
    if nome != "" and gols != 0:
        print(f"O jogador {nome} marcou {gols} gols.")


n = str(input("Nome do jogador"))
g = str(input("Quantos gols marcados?"))
ficha(n,g)
