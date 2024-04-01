f = str(input("Digite sua expressão"))
l = []
for s in f:
    if s == "(":
        l.append("(")
    elif s == ")":
        l.append(")")
if l.count("(") == l.count(")"):
    print("A expressão está correta")
else:
    print("A expressão está errada")
