# Solicita ao usuário que insira dois números e armazena as entradas como strings
numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

# Converte as entradas do usuário (strings) em números inteiros
int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

# Imprime a soma dos números usando uma f-string
print(f'A soma dos números é: {int_numero_1 + int_numero_2}')
