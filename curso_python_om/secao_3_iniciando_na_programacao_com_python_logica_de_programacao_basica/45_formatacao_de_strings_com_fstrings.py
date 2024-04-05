# Formatação básica de strings
# s - string
# d - int
# f - float
# .<número de dígitos>f
# x ou X - Hexadecimal
# (Caractere)(><^)(quantidade)
# > - Esquerda
# < - Direita
# ^ - Centro
# = - Força o número a aparecer antes dos zeros
# Sinal - + ou -
# Ex.: 0>-100,.1f
# Conversion flags - !r !s !a 

# Define uma variável string
variavel = 'ABC'

# Imprime a variável com uma formatação simples
print(f'{variavel}')
# Isso resultará em "ABC"

# Imprime a variável com uma formatação para alinhamento à direita em uma largura de campo de 10 caracteres
print(f'{variavel: >10}')
# Isso resultará em "       ABC"

# Imprime a variável com uma formatação para alinhamento à esquerda em uma largura de campo de 10 caracteres, seguido de um ponto
print(f'{variavel: <10}.')
# Isso resultará em "ABC       ."

# Imprime a variável com uma formatação para alinhamento central em uma largura de campo de 10 caracteres, seguido de um ponto
print(f'{variavel: ^10}.')
# Isso resultará em "   ABC    ."

# Imprime um número com uma formatação específica para sinal, largura de campo, número de dígitos após o ponto decimal e separadores de milhares
print(f'{1000.4873648123746:0=+10,.1f}')
# Isso resultará em "+1,000.5"

# Imprime um número em hexadecimal com um prefixo 0x e zero preenchido à esquerda até 8 dígitos
print(f'O hexadecimal de 1500 é {1500:08X}')
# Isso resultará em "O hexadecimal de 1500 é 000005DC"

# Imprime a representação textual (repr) da variável
print(f'{variavel!r}')
# Isso resultará em "'ABC'"
