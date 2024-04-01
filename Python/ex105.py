def notas(n=0, s=""):
    d = []
    maior = menor = 0
    while True:
        n = int(input("Notas do aluno"))
        d.append(n)
        s = str(input("Quer saber a situação"))
        if s in "Ss":
            if n < 6:
                print("O aluno está de recuperação")
            else:
                print("Aluno aprovado")
        print("~"*20)
        r = str(input("Mais algum aluno?"))
        if r in "Nn":
            break
    print(f"{len(d)} notas foram lidas")
    m = sum(d) / len(d)
    print(f"A média das notas foi {m}")
    print(f"A maior nota foi \033[34m{max(d)}\033[m e a menor foi \033[31m{min(d)}\033[m")
    return d


notas()
