#1
import math

# Solicitar o valor do raio ao usuário
raio = float(input("Digite o valor do raio do círculo: "))

# Calcular a área usando a fórmula área = π * raio²
area = math.pi * raio ** 2

# Exibir o resultado
print(f"A área do círculo com raio {raio} é: {area:.2f}")
