# Solicita ao usuário que insira dois valores e armazena as entradas como strings
primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

# Convertendo os valores de entrada em números inteiros
# Isso é necessário para garantir que a comparação seja feita com base nos valores numéricos
primeiro_valor = int(primeiro_valor)
segundo_valor = int(segundo_valor)

# Compara os valores inseridos
if primeiro_valor >= segundo_valor:
    # Se o primeiro valor for maior ou igual ao segundo, imprime esta mensagem
    print(
        f'{primeiro_valor=} é maior ou igual '
        f'ao que {segundo_valor=}'
    )
else:
    # Se o segundo valor for maior que o primeiro, imprime esta mensagem
    print(
        f'{segundo_valor=} é maior '
        f'do que {primeiro_valor=}'
    )
