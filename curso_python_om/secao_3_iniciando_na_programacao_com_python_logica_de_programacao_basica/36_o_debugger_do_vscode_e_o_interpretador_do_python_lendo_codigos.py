# Definição das variáveis de condição
condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = True

# Verifica a primeira condição
if condicao1:
    # Como condicao1 é False, este bloco não será executado
    print('Código para condição 1')
    print('Código para condição 1')

# Verifica a segunda condição
elif condicao2:
    # Como condicao2 é False, este bloco não será executado
    print('Código para condição 2')

# Verifica a terceira condição
elif condicao3:
    # Como condicao3 é True, este bloco será executado
    print('Código para condição 3')

# Verifica a quarta condição
elif condicao4:
    # Como condicao4 é True e a condição anterior foi satisfeita, este bloco não será executado
    print('Código para condição 4')

# Se nenhuma das condições anteriores for satisfeita, executa o bloco else
else:
    print('Nenhuma condição foi satisfeita.')

# Este é um bloco if isolado que não está relacionado ao bloco anterior
# Verifica se 10 é igual a 10
if 10 == 10:
    # Como 10 é igual a 10, este bloco será executado
    print('Outro if')

# Imprime esta mensagem, independentemente do resultado dos blocos condicionais anteriores
print('Fora do if')
