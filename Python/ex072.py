e = ("Zero", "Um", "Dois", "Tres", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez"
     , "onze", "Doze", "Treze", "Quatorse", "Quinze", "Deseseis", "Dezessete", "Dezoito", "Dezenove", "Vinte")
while True:
    n = int(input("Diga um numero de 0 a 20"))
    if 0<=n<=20:
        break
print(f"Você digitou o numero {e[n]}")
