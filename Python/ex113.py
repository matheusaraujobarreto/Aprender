def leiaint():
    while True:
        try:
            v = int(input("Digite um numero inteiro"))
        except (ValueError,TypeError):
            print("\033[31mErro,numero digitado não é inteiro\033[m")
            continue
        except KeyboardInterrupt:
            print("\nNenhum dado informado pelo usuário")
            return "Nenhum"
        else:
            return v



def leiafloat():
    while True:
        try:
            v = float(input("Digite um numero real"))
        except (ValueError, TypeError):
            print("\033[31mErro,numero digitado não é real\033[m")
            continue
        except KeyboardInterrupt:
            print("\nNenhum dado informado pelo usuário")
            return "Nenhum"
        else:
            return v


n = leiaint(),leiafloat()
print(f"O valor inteiro digitado foi {n[0]} e o numero real foi {n[1]}")
