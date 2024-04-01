x = int(input("Medida do lado do triângulo"))
y = int(input("Medida do lado do triângulo"))
z = int(input("Medida do lado do triângulo"))
if x + y > z and x + z > y and y + z > x:
    print("Pode ser feito um triângulo")
else:
    print("Não pode ser feito um triângulo")
