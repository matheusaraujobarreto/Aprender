c = float(input("Valor da casa"))
s = float(input("Salario"))
a = float(input("Quantos anos quer pagar?"))
p = c/a
print("Sua parcela é de {:.2f} reais".format(p))
if p > 30/100*s:
    print("\033[1:31mEmprestimo negado\033[m")
else:
    print("\033[1:34mCrédito liberado\033[m")
