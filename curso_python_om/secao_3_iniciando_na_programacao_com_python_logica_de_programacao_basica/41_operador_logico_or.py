# Operadores lógicos
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira avalia toda a expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro, a expressão inteira será avaliada naquele valor.
# São considerados falsy (que você já viu)
# 0 0.0 '' False
# Também existe o tipo None que é usado para representar um não valor

# Este código demonstra o uso do operador lógico 'or' e a avaliação de curto-circuito

# Avaliação de curto circuito
senha = input('Senha: ') or 'Sem senha'
# Se a entrada para senha for uma string vazia (falsy), 'Sem senha' será atribuído a senha.
# Isso acontece devido à avaliação de curto-circuito, onde o Python retorna o primeiro valor verdadeiro encontrado.

print(senha)
