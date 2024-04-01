v = int(input("Diga sua velocidade"))
if v>80:
    print("\033[1;31mVoce foi multado em {}{}\033[m \033[1;31mreais".format('\033[4;33m',(v-80)*7))
else:
    print("\033[36mEstá dentro do limite")
