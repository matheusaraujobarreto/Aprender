import random
a = str(input("Nome do aluno"))
b = str(input("Nome do aluno"))
c = str(input("Nome do aluno"))
d = str(input("Nome do aluno"))
L = [a,b,c,d]
print("O escolhido é \033[1;34m{}".format(random.choice(L)))
