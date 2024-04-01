import ex107moedas
n = float(input("Digite o valor"))
r = str(input("Quer aumentar ou diminuir esse valor?S/N"))
if r in "Ss":
    p = int(input("Quantos %?Apenas o valor"))
    print(f"O valor {n} vezes {p}% é {ex107moedas.porcentagem(n,p)}")
else:
    print(f"O dobro de {n} é {ex107moedas.dobro(n)}")
    print(f"A metade de {n} é {ex107moedas.metade(n)}")
