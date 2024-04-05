# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que você já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

# Este código demonstra o uso dos operadores lógicos 'and' e a avaliação de curto-circuito

# Avaliação de curto circuito
print(True and False and True)  # Resultado: False
# Aqui, todas as condições precisam ser verdadeiras para que o resultado seja True.
# Como uma das condições é False, o resultado final é False.

# Avaliação de curto circuito
print(True and 0 and True)  # Resultado: 0
# O operador 'and' realiza uma avaliação de curto-circuito.
# Assim que um operando falso é encontrado, a expressão é imediatamente interrompida
# e esse valor falso é retornado. Nesse caso, 0 é considerado falso.

# Solicita ao usuário que insira a opção de entrada e a senha, armazenando as entradas como strings
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

# Define a senha permitida
senha_permitida = '123456'

# Verifica se a opção de entrada é "E" e se a senha digitada corresponde à senha permitida
if entrada == 'e' and senha_digitada == senha_permitida:
    # Se ambas as condições forem verdadeiras, imprime "Acesso concedido"
    print('Acesso concedido')
else:
    # Se qualquer uma das condições for falsa, imprime "Acesso negado"
    print('Acesso negado')

