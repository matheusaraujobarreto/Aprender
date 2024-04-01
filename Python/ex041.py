from datetime import date
a = int(input("Seu ano de nascimento"))
i = date.today().year - a
if i <= 9:
    print("Tens {} anos, vai para a mirim".format(i))
elif 9 < i <= 14:
    print("Tens {} anos, vai para a infantil".format(i))
elif 14 < i < 19:
    print("Tens {} anos, vai para a junior".format(i))
elif 19 < i < 20:
    print("Tens {} anos, vai para a senior".format(i))
else:
    print("Tens {} anos, vai para a master".format(i))
