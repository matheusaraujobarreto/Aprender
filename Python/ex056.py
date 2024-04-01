soma = 0
maioridadehomem = 0
nomevelho = ""
mulher20 = 0
for c in range(1,5):
    n = str(input("Seu nome")).strip().upper()
    i = int(input("Sua idade"))
    s = str(input("Seu sexom M ou F")).strip().upper()
    soma = soma + i
    if c == 1 and s == "M":
        maioridadehomem = i
        nomevelho = n
    if s == "M" and i > maioridadehomem:
        maioridadehomem = i
        nomevelho = n
    if s == "F" and mulher20 < 20:
        mulher20 += 1
media = soma / 4
print(media)
print("O homem mais velho é {} e tem {} anos.".format(nomevelho.title(),maioridadehomem))
print("{} mulheres com menos de 20 anos".format(mulher20))
#Bgl chato do krl