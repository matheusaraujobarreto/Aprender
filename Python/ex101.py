def voto(i):
    print(f"Você nasceu em {i}, tem {2024-i} anos")
    if 2024-i < 16:
        return "Você não pode votar"
    if 16 <= 2024-i < 18 or 2024-i >= 60:
        return "Seu voto é opcional"
    if 18 <= 2024-i < 60:
        return "Seu voto é obrigatório"


ano = int(input("Em que ano você nasceu?"))
voto(ano)
