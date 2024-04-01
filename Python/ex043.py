p = float(input("Diga seu peso"))
a = float(input("Diga sua altura em metros"))
i = p/a**2
if i < 18.5:
    print("Seu imc é de {:.2f}, está abaixo do peso".format(i))
elif 18.5 < i <= 25:
    print("Seu imc é de {:.2f}, está com peso ideal".format(i))
elif 25 < i <= 30:
    print("Seu imc é de {:.2f}, está com sobrepeso".format(i))
elif 30 < i <= 40:
    print("Seu imc é de {:.2f}, está obeso".format(i))
else:
    print("Seu imc é de {:.2f}, está com obesidade morbida".format(i))
