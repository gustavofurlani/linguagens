n = int(input("Quantos termos da sequência de Fibonacci deseja ver? "))

a, b = 0, 1  # Inicia os dois primeiros termos

for _ in range(n):
    print(a, end=" ")  # Imprime os termos na mesma linha
    a, b = b, a + b  # Atualiza os valores

print()
