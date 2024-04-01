x = int(input("Diga um numero"))
s = str(x)
#print("Milhar {}\ncentena {}\ndezena {}\ne unidade {}".format(s[0],s[1],s[2],s[3]))
# porem da erro quando nao tem 4 numeros logo
print("Milhar {}\ncentena {}\ndezena {}\ne unidade {}".format(x//1000%10,x//100%10,x//10%10,x//1%10))
