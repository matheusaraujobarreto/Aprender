s = str(input("Qual seu sexo?")).strip().upper()[0] #lembrar de ler a 1 letra
while s not in "MF":
    str(input("Qual seu sexo?")).strip().upper()
if s == "M":
    print("Sexo masculino registrado")
else:
    print("Sexo femino registrado")
#Tem um problema que ele se repete se errar o primeiro
