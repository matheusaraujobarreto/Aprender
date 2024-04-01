n = str(input("Fale seu nome")).strip()
s = n.split()
print("Seu primeiro nome é \033[0;36m{}\033[m e o ultimo é \033[0;36m{}\033[m"
      .format(s[0].title(), s[len(s)-1].title()))
