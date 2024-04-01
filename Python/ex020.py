import random
a = str(input("Nome do aluno"))
b = str(input("Nome do aluno"))
c = str(input("Nome do aluno"))
d = str(input("Nome do aluno"))
L = [a,b,c,d]
random.shuffle(L)
print("A ordem de apresentação é")
print(L)
