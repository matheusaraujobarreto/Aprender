def cont(i, f, p):
    if i <= f:
        c = i
        while c <= f:
            print(f"{c}", end="")
            c += p
        print("Fim")
    else:
        c = i
        while c >= f:
            print(f"{c} ", end="")
            c -= p
        print("Fim")


cont(1,10,1)
cont(10,0,2)
cont(int(input("Começo")), int(input("Fim")), int(input("Pulando de quanto em quanto?")))
