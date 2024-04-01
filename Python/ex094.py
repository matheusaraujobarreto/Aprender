d = {}
lm = []
mulheres = homens = 0
i = []
while True:
    d["nome"] = str(input("Nome"))
    d["idade"] = float(input("Idade"))
    i.append(d["idade"])
    d["Sexo"] = str(input("Sexo(M/F)"))
    if d["Sexo"] in "Ff":
        mulheres += 1
        lm.append(d["nome"])
    else:
        homens += 1
    r = str(input("Mais alguem?"))
    if r in "Nn":
        break
m = (sum(i))/len(i)
print(f"{len(i)} pessoas foram cadastradas")
print(f"A média de idade é {m}")
print(f"O nome das mulheres são {lm}")
print(f"{d["nome"]} tem idade maior que a média das pessoas" if d["idade"]>m else "Ninguem tem a idade acima da média")
