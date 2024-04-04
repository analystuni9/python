"""
DocString
Python = Linguagem de programação
Tipo de tipagem = Dinâmica / Forte
str -> string -> texto
Strings são textos que estão dentro de aspas
"""

# Este código Python demonstra diferentes maneiras de usar aspas para representar strings e o uso do caractere de escape.

# Impressão do número 1234
print(1234)

# Aspas simples: Usadas para representar uma string que pode conter aspas duplas sem escapar.
print('Danilo Brito')
print(1, 'Danilo Brito"')

# Aspas duplas: Usadas para representar uma string que pode conter aspas simples sem escapar.
print("Danilo Brito")
print(2, "Danilo Brito'")

# Escape: O caractere de escape \ é usado para escapar aspas dentro de uma string.
print("Danilo \"Brito\"")

# r: O prefixo r antes da string indica uma string "bruta", na qual os caracteres de escape são tratados como literais.
print(r"Danilo \"Brito\"")
