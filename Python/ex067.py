print("Tabuadas")
print("-"*20)
while True:
    n = int(input("Quer saber a tabuada do que?"))
    print("-" * 20)
    if n < 0:
        print("\033[31mFalha\033[m")
        break
    for c in range(1,11):
        print(f"{n} x {c} = {n*c}")
    print("-"*20)
