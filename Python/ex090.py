aluno = {"Nome":str(input("Nome")).title(), "Media":int(input("Média")), "Situação":""}
if aluno["Media"] <= 3:
    aluno["Situação"] = "Reprovado"
elif 3 < aluno["Media"] < 6:
    aluno["Situação"] = "Recuperação"
elif aluno["Media"] >= 6:
    aluno["Situação"] = "Aprovado"
print(f"{aluno["Nome"]} teve média de {aluno["Media"]}, logo está {aluno["Situação"]}")
