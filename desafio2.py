import math

def eh_primo(n):
    """Função que verifica se um número é primo."""
    if n < 2:
        return False  # Números menores que 2 não são primos
    for i in range(2, int(math.sqrt(n)) + 1):  # Testa até a raiz quadrada de n
        if n % i == 0:
            return False  # Se for divisível por i, não é primo
    return True  # Se não encontrou divisores, é primo

# Entrada do usuário com tratamento de erro
try:
    num = int(input("Digite um número inteiro positivo: "))
    if num < 0:
        print("Erro! Digite um número inteiro positivo.")
    elif eh_primo(num):
        print(f"O número {num} é primo!")
    else:
        print(f"O número {num} não é primo.")
except ValueError:
    print("Erro! Entrada inválida. Digite um número inteiro.")
