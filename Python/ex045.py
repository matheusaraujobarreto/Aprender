import random
j = str(input("Vamos jogar pedra, papel e tesoura, escolha"))
l = ['pedra','papel','tesoura']
c = random.choice(l)
if j == c:
    print("Deu empate")
elif j == "tesoura" and c == "papel" or j == "pedra" and c == "tesoura" or j == "papel" and c == "pedra":
    print("Você ganhou, escolhi {}".format(c))
else:
    print("Eu ganhei, {} ganha de {}".format(c,j))
