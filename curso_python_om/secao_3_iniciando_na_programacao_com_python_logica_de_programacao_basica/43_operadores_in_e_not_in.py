# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1

# Exemplos de uso dos operadores 'in' e 'not in' com strings

# Solicita ao usuário que insira seu nome e a substring a ser encontrada
nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

# Verifica se a substring está presente no nome
if encontrar in nome:
    # Se a substring estiver presente, imprime que foi encontrada
    print(f'{encontrar} está em {nome}')
else:
    # Se a substring não estiver presente, imprime que não foi encontrada
    print(f'{encontrar} não está em {nome}')
