s = 0
for c in range(0,6):
    n = int(input("Diga um numero inteiro"))
    if n % 2 == 0:
        s = s + n
print("A soma dos numeros pares é {}".format(s))
