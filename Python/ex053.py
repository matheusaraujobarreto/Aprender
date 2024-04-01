f = str(input("Diga uma frase")).strip().upper()
p = f.split()
j = ''.join(p)
i = ""
for l in range(len(j)-1,-1, -1):
    i += j[l]
if i == j:
    print("A frase '{}', é um palíndromo".format(j))
else:
    print("A frase '{}', não é um palíndromo".format(j))
