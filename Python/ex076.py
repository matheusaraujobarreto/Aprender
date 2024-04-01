#p = "Lapiz", "Caderno", "Celular", "Computador", "Mochila"
#v = 0.50, 20, 2400, 5000, 100
#print("Tabela de preços")
#print("-"*20)
#print(f"{p[0]}",". "*10,f"R${v[0]:.2f}")
#print(f"{p[1]}",". "*10,f"R${v[1]:.2f}")
#print(f"{p[2]}",". "*10,f"R${v[2]:.2f}")
#print(f"{p[3]}",". "*10,f"R${v[3]:.2f}")
#print(f"{p[4]}",". "*10,f"R${v[4]:.2f}")
#print("-"*20)
#ou
pv = "Lapiz",0.50, "Caderno",20, "Celular",2400, "Computador",5000, "Mochila",100
print("-"*42)
print(f"{"Tabela de preços":^40}")
print("-"*42)
for p in range(0,len(pv)):
    if p % 2 == 0:
        print(f'{pv[p]:.<30}',end="")
    else:
        print(f" R$ {pv[p]:>.2f}")
print("-"*42)
#Coisa de gente que n tem oq fazer
