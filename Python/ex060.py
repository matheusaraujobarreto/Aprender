# Use o import ou
from time import sleep
n = int(input("Fale um numero"))
c = n
f = 1
print("Calculando {}! = ".format(n),end="",)
while c > 0:
    print(c,end="")
    print("x" if c > 1 else "=", end="")
    f *= c
    c -= 1
sleep(1)
print(f)
