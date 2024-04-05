"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

# Solicita ao usuário que digite um número
numero_str = input('Vou dobrar o número que você digitar: ')

try:
    # Tenta converter a entrada do usuário em um número float
    numero_float = float(numero_str)
    # Se a conversão for bem-sucedida, imprime o dobro do número com duas casas decimais
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    # Se ocorrer um erro durante a conversão, imprime uma mensagem informando que a entrada não é um número
    print('Isso não é um número')
