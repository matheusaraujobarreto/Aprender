from time import sleep


def ajuda():
    while True:
        print("~"*30)
        print("    Manual de python")
        print("Para sair escreva 'fim'")
        print("~"*30)
        msg = str(input("Digite o codigo que tem duvida"))
        print("~"*30)
        print(f"\033[7;40mAqui está tudo sobre\033[m \033[34m{msg}\033[m")
        print("~"*30)
        sleep(1)
        print(f"\033[31m{help(msg)}\033[m")
        r = str(input("Mais alguma dúvida?"))
        if r in "FIM":
            break


ajuda()
# Deixar o programa mais bonito
