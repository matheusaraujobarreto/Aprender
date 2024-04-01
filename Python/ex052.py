n = int(input("Diga um numero"))
t = 0
for c in range(1, n+1):
    if n % c == 0:
        t += 1
if t == 2 or t == 1:
    print('{} é primo'.format(n))
else:
    print("{} não é primo".format(n))
