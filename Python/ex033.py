x = float(input("Diga um numero"))
y = float(input("Diga um numero"))
z = float(input("Diga um numero"))
if x>y>z:
    print("O maior é \033[31m{}\033[m e o menor \033[35m{}\033[m".format(x,z))
if x>z>y:
    print("O maior é \033[31m{}\033[m e o menor \033[35m{}\033[m".format(x,y))
if y>x>z:
    print("O maior é \033[31m{}\033[m e o menor \033[35m{}\033[m".format(y,z))
if y>z>x:
    print("O maior é \033[31;m{}\033[m e o menor \033[35m{}\033[m".format(y,x))
if z>x>y:
    print("O maior é \033[31;m{}\033[m e o menor \033[35m{}\033[m".format(z,y))
if z>y>x:
    print("O maior é \033[31m{}\033[m e o menor \033[35m{}\033[m".format(z,x))
