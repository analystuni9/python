# Definição das variáveis de condição
condicao1 = True
condicao2 = True
condicao3 = True
condicao4 = True

# Verifica a primeira condição
if condicao1:
    # Se a condicao1 for True, executa este bloco de código
    print('Código para condição 1')
    print('Código para condição 1')

# Se a condicao1 não for satisfeita, verifica a segunda condição
elif condicao2:
    # Se a condicao2 for True, executa este bloco de código
    print('Código para condição 2')

# Se a condicao2 não for satisfeita, verifica a terceira condição
elif condicao3:
    # Se a condicao3 for True, executa este bloco de código
    print('Código para condição 3')

# Se nenhuma das condições anteriores for satisfeita, verifica a quarta condição
elif condicao4:
    # Se a condicao4 for True, executa este bloco de código
    print('Código para condição 4')

# Se nenhuma das condições anteriores for satisfeita, executa o bloco else
else:
    print('Nenhuma condição foi satisfeita.')

# Este é um bloco if isolado que não está relacionado ao bloco anterior
# Verifica se 10 é igual a 10
if 10 == 10:
    # Se for, imprime esta mensagem
    print('Outro if')

# Imprime esta mensagem, independentemente do resultado dos blocos condicionais anteriores
print('Fora do if')
