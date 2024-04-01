dados = {}
dados["nome"] = str(input("Nome"))
nasc = int(input("Ano de nascimento"))
dados["idade"] = 2024-nasc
dados["ctps"] = int(input("Numero da ctps(se não tiver, 0"))
if dados["ctps"] != 0:
    dados["salario"] = float(input("Salario"))
    dados["contratação"] = int(input("Ano de contratação"))
    dados["Aposentadoria"] = dados["idade"]+((dados["contratação"]+35)-2024)
for k, v in dados.items():
    print(f"  -{k}:{v}")