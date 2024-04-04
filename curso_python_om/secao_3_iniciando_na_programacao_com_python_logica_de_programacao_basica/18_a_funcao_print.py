# Este código Python demonstra o uso dos argumentos sep e end na função print():

# sep: Especifica o separador a ser usado entre os argumentos impressos. Por padrão, o separador é um espaço em branco.
# end: Especifica o que deve ser impresso no final da saída. Por padrão, é uma nova linha (\n).

# Na primeira chamada de print(), os números 12, 34 e 1011 são impressos juntos sem espaços entre eles, seguidos por # como o final da saída.
print(12, 34, 1011, sep="", end='#')

# Na segunda chamada de print(), os números 56 e 78 são impressos com um hífen - entre eles, seguidos por uma nova linha.
print(56, 78, sep='-', end='\n')

# Na terceira chamada de print(), os números 9 e 10 são impressos com um hífen - entre eles, seguidos por uma nova linha.
print(9, 10, sep='-', end='\n')
