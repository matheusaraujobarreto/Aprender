x = int(input("Medida do lado do triângulo"))
y = int(input("Medida do lado do triângulo"))
z = int(input("Medida do lado do triângulo"))
if x + y > z and x + z > y and y + z > x and x == y != z or x == z != y or y == z != x:
    print("Pode ser feito um triângulo, e esse triangulo é isosceles")
elif x + y > z and x + z > y and y + z > x and x == y == z:
    print("Pode ser feito um triângulo, e esse triangulo é equilatero")
elif x + y > z and x + z > y and y + z > x and x != y != z:
    print("Pode ser feito um triângulo, e esse triangulo é escaleno")
else:
    print("Não pode ser feito um triângulo")
