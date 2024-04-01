x = float(input("Digite um numero"))
y = float(input("Digite outro"))
print("Digite 1 para +\nDigite 2 para o maior\nDigite 3 para x\nDigite 4 para /\nOu\n5 para nada")
n = int(input("O que quer saber?"))
maior = 0
if n == 1:
    print("A soma é {}".format(x+y))
elif n == 2:
    if x > y:
        maior = x
    else:
        maior = y
    print("o maior é {}".format(maior))
elif n == 3:
    print("A multiplicação é {}".format(x*y))
elif n == 4:
    x = float(input("Digite um numero"))
    y = float(input("Digite outro"))
    print("Digite 1 para +\nDigite 2 para o maior\nDigite 3 para x\nDigite 4 para /\nOu\n5 para sair")
    n = int(input("Qual operação?"))
    if n == 1:
        print("A soma é {}".format(x + y))
    elif n == 2:
        if x > y:
            maior = x
        else:
            maior = y
        print("o maior é {}".format(maior))
    elif n == 3:
        print("A multiplicação é {}".format(x * y))
while n == 4:
    if n == 1:
        print("A soma é {}".format(x + y))
    elif n == 2:
        if x > y:
            maior = x
        else:
            maior = y
        print("o maior é {}".format(maior))
    elif n == 3:
        print("A multiplicação é {}".format(x * y))
    elif n == 4:
        x = float(input("Digite um numero"))
        y = float(input("Digite outro"))
        print("Digite 1 para +\nDigite 2 para o maior\nDigite 3 para x\nDigite 4 para /\nOu\n5 para sair")
        n = int(input("Qual operação?"))
        if n == 1:
            print("A soma é {}".format(x + y))
        elif n == 2:
            if x > y:
                maior = x
            else:
                maior = y
            print("o maior é {}".format(maior))
        elif n == 3:
            print("A multiplicação é {}".format(x * y))
else:
    print("Ok, tenha um bom dia")
