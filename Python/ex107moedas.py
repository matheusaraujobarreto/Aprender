def dobro(num):
    return f"{num:.2f}".replace(".", ","), f"{num * 2:.2f}".replace(".", ",")


def metade(num):
    return f"{num:.2f}".replace(".", ","), f"{num / 2:.2f}".replace(".", ",")


def porcentagem(num, por=0):
    return f"{num:.2f}".replace(".", ","), f"{num * por/100:.2f}".replace(".", ",")


