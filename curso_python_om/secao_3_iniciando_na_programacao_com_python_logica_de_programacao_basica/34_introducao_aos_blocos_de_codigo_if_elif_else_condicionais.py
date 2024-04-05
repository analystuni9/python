# Solicita ao usuário que escolha entre 'entrar' e 'sair' e armazena a entrada
entrada = input('Você quer "entrar" ou "sair"? ')

# Verifica se a entrada é igual a 'entrar'
if entrada == 'entrar':
    # Se for, imprime uma mensagem indicando que o usuário entrou no sistema
    print('Você entrou no sistema')

    # Imprime um número qualquer (apenas para demonstração)
    print(12341234)

# Se a entrada não for 'entrar', verifica se é igual a 'sair'
elif entrada == 'sair':
    # Se for, imprime uma mensagem indicando que o usuário saiu do sistema
    print('Você saiu do sistema')

# Se a entrada não for 'entrar' nem 'sair', imprime uma mensagem indicando que a entrada não foi reconhecida
else:
    print('Você não digitou nem "entrar" e nem "sair".')

# Após a execução dos blocos if/elif/else, imprime 'FORA DOS BLOCOS'
print('FORA DOS BLOCOS')
