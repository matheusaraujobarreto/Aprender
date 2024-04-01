t = ("Pal","Gre","Atl-MG","Fla","Bot","Brag","Flu","Atl-PR","Inter","Fort","Sp","Cui","Cori","Cruz","Vas","Bah",
    "San","Goi","Cor","Amg")
print(f"Os cinco primeiros times da tabela são \n{t[0]}\n{t[1]}\n{t[2]}\n{t[3]}\n{t[4]}")
print("-"*30)
print(f"Os cinco ultimos times da tabela são {t[-1]}\n{t[-2]}\n{t[-3]}\n{t[-4]}\n{t[-5]}")
print("-"*30)
print("Em ordem alfabetica\n",sorted(t))
print("-"*30)
print('O Fortaleza está na posição',t.index("Fort"))