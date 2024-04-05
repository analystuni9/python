# Interpolação básica de strings
# s - string
# d e i - int
# f - float
# x e X - Hexadecimal (ABCDEF0123456789)

# Define uma string e um valor de preço
nome = 'Luiz'
preco = 1000.95897643

# Utiliza a formatação antiga para interpolar os valores na string
# '%s' é substituído pelo valor de 'nome' e '%.2f' é substituído pelo valor de 'preco' com duas casas decimais
variavel = '%s, o preço é R$%.2f' % (nome, preco)
# Isso resultará em "Luiz, o preço é R$1000.96"

# Imprime a variável formatada
print(variavel)

# Utiliza a formatação antiga para imprimir um número em hexadecimal
# '%d' é substituído pelo valor de 1500 e '%08X' formata esse valor como um número hexadecimal de 8 dígitos preenchido com zeros à esquerda
print('O hexadecimal de %d é %08X' % (1500, 1500))
# Isso resultará em "O hexadecimal de 1500 é 000005DC"
