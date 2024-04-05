# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True

# Este código demonstra o uso do operador lógico 'not'

# Exemplos de uso do operador 'not'

# Invertendo o valor de expressões booleanas
print(not True)  # Resultado: False
print(not False)  # Resultado: True

# Verificando se uma string está vazia
string_vazia = ''
print(not string_vazia)  # Resultado: True
# A expressão 'not string_vazia' avalia para True, pois a string_vazia é considerada falsa.

# Verificando se uma lista está vazia
lista_vazia = []
print(not lista_vazia)  # Resultado: True
# A expressão 'not lista_vazia' avalia para True, pois a lista_vazia é considerada falsa.

# Verificando se um número é diferente de zero
numero = 5
print(not numero)  # Resultado: False
# A expressão 'not numero' avalia para False, pois o número 5 é considerado verdadeiro.

# Invertendo o resultado de uma comparação
valor = 10
print(not (valor == 10))  # Resultado: False
# A expressão 'not (valor == 10)' avalia para False, pois a comparação 'valor == 10' é verdadeira.
