from time import sleep
li = []
ln = []


def menu():
    while True:
        print("-" * 35)
        print("          \033[33mMenu principal\033[m")
        print("-" * 35)
        print("\033[34m1\033[m - \033[33mCadastrar nova pessoa\033[m")
        print("\033[34m2\033[m - \033[33mVer pessoas cadastradas\033[m")
        print("\033[34m3\033[m - \033[33mSair do programa\033[m")
        try:
            o = int(input("\033[33mOpção:\033[m"))
        except:
            print("\033[31mOpção inválida, tente de novo\033[m")
            continue
        if o == 3:
            print("Volte sempre")
            break
        elif o == 2:
            sleep(0.5)
            print("-" * 35)
            print(f"             \033[33mOpção {o}\033[m")
            print("-" * 35)
            sleep(0.5)
            for nome in range(0, len(ln)):
                print(f"{ln[nome]:<30}{li[nome]:>3}")
        elif o == 1:
            sleep(0.3)
            print("-" * 35)
            print(f"             \033[33mOpção {o}\033[m")
            print("-" * 35)
            sleep(0.3)
            n = str(input("\033[34mNome para cadastro\033[m"))
            ln.append(n)
            i = int(input(f"\033[34mIdade do(a) {n}\033[m"))
            li.append(i)
            print("\033[34mDados cadastros\033[m")
        if o != 1 and o != 2 and o != 3:
            print("\033[31mOpção inválida, tente de novo\033[m")


menu()
