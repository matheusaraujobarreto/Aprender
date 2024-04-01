n = str(input("Qual seu nome?")).strip()
print(n.upper(),n.lower()) # maisculas e minusculas
print(len(n)-n.count(' ')) # quantas letras tem sem os espaços
print(n.find(' ')) # quantas letras tem o primeiro nome
# OU
s = n.split()
print(s[0],len(s[0])) #separar o nome e colocar o elemento 0
