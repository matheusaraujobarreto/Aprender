v = float(input("Valor do produto"))
f = str(input("Forma de pagamento")).strip()
if f.title() in ("Debito cartão Credito Parcelado"):
    print("Você paga {} reais a vista com desconto, {} parcelando em 2x e {} em ate 3x com 20% de juros"
          .format(v*95/100,v,v*120/100))
elif f.title() in ("Dinheiro cheque"):
    print("Você paga {} reais com desconto".format(v*90/100))
else:
    print("Só trabalhamos com essas formas de pagamento")
