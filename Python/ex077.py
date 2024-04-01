n = "Sarah", "Matheus", "Maria", "Hulda", "Overwatch"
for p in n:
    print(f"\nNa palavra {p.upper()} temos as vogais: ", end="")
    for l in p:
        if l.lower() in "aeiou":
            print(l, end="")
