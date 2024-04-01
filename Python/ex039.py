import datetime
a = int(input("Ano de nascimento"))
i = datetime.date.today().year - a
if i < 18:
    print("Faltam {} anos para se alistar".format(18-i))
elif i == 18:
    print("Está na hora de se alistar")
else:
    print("\033[1:31mCuidado\033[m! Já se passaram {} ano/s de você se alistar".format(i-18))
