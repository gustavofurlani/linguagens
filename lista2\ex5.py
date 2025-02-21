lado1 = float(input("digite o lado1 do triangulo"))

lado2 = float(input("digite o lado2 do triangulo"))

lado3 = float(input("digite o lado3 do triangulo"))


if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print("Os valores formam um triângulo válido!")
else:
    print("Os valores NÃO formam um triângulo válido.")
