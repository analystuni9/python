# Solicita ao usuário que insira seu nome e idade
nome = input('Digite o seu nome: ')
idade = input('Digite sua idade: ')

# Verifica se tanto o nome quanto a idade foram fornecidos pelo usuário
if nome and idade:
    # Se ambos os campos estiverem preenchidos, imprime o nome e realiza operações com ele
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    # Verifica se o nome contém espaços em branco
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome NÃO contém espaços')

    # Calcula o comprimento do nome
    print(f'Seu nome tem {len(nome)} letras')
    # Imprime a primeira letra do nome
    print(f'A primeira letra do seu nome é {nome[0]}')
    # Imprime a última letra do nome
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    # Se algum dos campos estiver vazio, imprime uma mensagem de erro
    print("Desculpe, você deixou campos vazios.")
