p = ""
c = maior = menor = s = 0
while p !="n":
    n = int(input("Digite um numero"))
    c += 1
    s += n
    p = str(input("Quer continuar?S/N"))
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
m = s/c
print("O maior foi {}, menor {}, dentre os {} numeros e sua média foi {}".format(maior, menor, c, m))
