import ex107moedas
n = float(input("Digite o valor"))
r = str(input("Quer aumentar ou diminuir esse valor?S/N"))
if r in "Ss":
    p = int(input("Quantos %?Apenas o valor"))
    if p > 100:
        print(f"O valor de R${ex107moedas.dobro(n)[0]} com aumento de {p-100}% é R${ex107moedas.porcentagem(n, p)[1]}")
    else:
        print(f"O valor de R${ex107moedas.dobro(n)[0]} com diminuição de {100-p}% é R${ex107moedas.porcentagem(n, p)[1]}")
    print(f"O dobro de R${ex107moedas.dobro(n)[0]} é R${ex107moedas.dobro(n)[1]}")
    print(f"A metade de R${ex107moedas.dobro(n)[0]} é R${ex107moedas.metade(n)[1]}")
else:
    print(f"O dobro de R${ex107moedas.dobro(n)[0]} é R${ex107moedas.dobro(n)[1]}")
    print(f"A metade de R${ex107moedas.dobro(n)[0]} é R${ex107moedas.metade(n)[1]}")
