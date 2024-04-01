def dobro(p=0, forma=False):
    r = p * 2
    return r if not forma else m(r)


def metade(p=0, forma=False):
    r = p / 2
    return r if not forma else m(r)


def porcentagem(p=0, por=0, forma=False):
    r = p * por / 100
    return r if not forma else m(r)


def m(p=0, moeda="R$"):
    return f"{moeda}{p:.2f}".replace(".", ",")


def resumo(p=0, por=0, forma=False):
    print("~"*35)
    print("         Resumo do valor")
    print("~"*35)
    return print(f"O dobro de {m(p)} é {dobro(p,forma=True)}\nA metade de {m(p)} é {metade(p,forma=True)}\n"
                 f"E {por}% de {m(p)} é {porcentagem(p, por, forma=True)}"), print("~"*35)


def resumoplus(p=0, por=0, forma=False):
    p = float(input(f"{"Digite o valor"}").replace(",", ","))
    por = float(input("Quantos porcento?Apenas valor"))
    print("~"*35)
    print("         Resumo do valor")
    print("~"*35)
    return print(f"O dobro de {m(p)} é {dobro(p,forma=True)}\nA metade de {m(p)} é {metade(p,forma=True)}\n"
                 f"E {por}% de {m(p)} é {porcentagem(p, por, forma=True)}"), print("~"*35),
