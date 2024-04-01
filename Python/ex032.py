x = int(input("Diga um ano"))
if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
    print("O ano",x,"é bissexto")
else:
    print("O ano {} não é bissexto".format(x))
# Sim isso é ridiculo
