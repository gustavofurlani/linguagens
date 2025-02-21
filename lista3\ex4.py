a = int(input("Digite o primeiro número do intervalo: "))
b = int(input("Digite o segundo número do intervalo: "))

if a > b:
    a, b = b, a  # Garante que A seja sempre menor que B

for i in range(a, b + 1):
    if i % 2 != 0:
        print(i)
