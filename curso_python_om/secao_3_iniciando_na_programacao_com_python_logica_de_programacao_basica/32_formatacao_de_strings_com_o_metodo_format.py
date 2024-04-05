# Definição das variáveis
a = 'AAAAA'
b = 'BBBBBB'
c = 1.1

# String de formatação com espaços reservados para substituição
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'

# Usando o método format() para substituir os espaços reservados pelos valores das variáveis
# Os nomes dentro dos espaços reservados devem corresponder aos nomes fornecidos no método format()
formato = string.format(
    nome1=a, nome2=b, nome3=c
)

# Imprimindo a string formatada
print(formato)
