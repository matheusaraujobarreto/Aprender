n = int(input("Digite um numero"))
r = int(input("Digite a razão da PA"))
t = n
c = 1
while c <= 10:
    print("{} + {} = >".format(t,r),end="")
    c += 1
    t += r
print(t)
