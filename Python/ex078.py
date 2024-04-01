l = [int(input("Digite um valor")),
     int(input("Digite um valor")),
     int(input("Digite um valor")),
     int(input("Digite um valor")),
    int(input("Digite um valor"))]
print(f"O maior foi {max(l)} nas posições ", end="")
for i, v in enumerate(l):
    if v == max(l):
        print(f"{i}...",end="")
print(f"\nO menor foi {min(l)} nas posições ", end="")
for i, v in enumerate(l):
    if v == min(l):
        print(f"{i}...", end="")
