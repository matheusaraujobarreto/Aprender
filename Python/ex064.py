n = int(input("Digite um numero"))
print("Para parar coloque 999" if n != 999 else "Ok")
c = 1
s = n
if n == 999:
    s = 0
while n != 999:
    n = int(input("Digite um numero"))
    if n == 999:
        s -= 999
    c += 1
    s += n
print("A soma de todos os {} numeros foi {}.".format(c-1, s))
