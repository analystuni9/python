# Nesta expressão, a ordem de precedência dos operadores é respeitada:

# Primeiro, os parênteses internos (0.5 + 0.5) são resolvidos, resultando em 1.0.
# Em seguida, a função int() converte 1.0 em um inteiro, resultando em 1.
# Depois, (1 + 1) é resolvido, resultando em 2.
# Então, (5 + 5) é resolvido, resultando em 10.
# Em seguida, 2 ** 10 é calculado, resultando em 1024.
# Portanto, o valor final de conta_1 é 1024.

# Ordem de precedência dos operadores:
# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -

# Expressão matemática seguindo a ordem de precedência:
# - Primeiro, os parênteses internos (0.5 + 0.5) são resolvidos, resultando em 1.0.
# - Em seguida, a função int() converte 1.0 em um inteiro, resultando em 1.
# - Depois, (1 + 1) é resolvido, resultando em 2.
# - Então, (5 + 5) é resolvido, resultando em 10.
# - Em seguida, 2 ** 10 é calculado, resultando em 1024.

# Atribuição do resultado da expressão à variável conta_1
conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)
# Impressão do resultado da expressão
print(conta_1)  # Imprime o resultado da conta_1

# Exemplo 1:
resultado_1 = 2 * 3 ** 2 + 4  # Primeiro, 3 ** 2 é calculado (9), depois 2 * 9 (18), e finalmente 18 + 4 (22)
print(resultado_1)  # Imprime 22

# Exemplo 2:
resultado_2 = 10 / 2 * 3  # Primeiro, 10 / 2 é calculado (5), depois 5 * 3 (15)
print(resultado_2)  # Imprime 15

# Exemplo 3:
resultado_3 = 5 + 10 // 2  # Primeiro, 10 // 2 é calculado (5), depois 5 + 5 (10)
print(resultado_3)  # Imprime 10

# Exemplo 4:
resultado_4 = 2 + 10 % 4  # Primeiro, 10 % 4 é calculado (2), depois 2 + 2 (4)
print(resultado_4)  # Imprime 4
