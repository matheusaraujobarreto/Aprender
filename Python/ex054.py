from datetime import date
a = date.today().year
maior = 0
menor = 0
for p in range(0,7):
    n = int(input("Ano de nascimento"))
    i = a - n
    if i >= 18:
        maior += 1
    else:
        menor += 1
print("{} pessoas são de maior e {} de menor".format(maior,menor))
