i = 0
s = 0
for c in range(1,501):
    if c % 2 != 0 and c % 3 == 0:
        i += c
        s += 1
print("A soma dos {} numeros é {}.".format(s,i))
