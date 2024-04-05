# Definição das variáveis
nome = 'Danilo Brito'
altura = 1.80
peso = 95

# Cálculo do índice de massa corporal (IMC)
imc = peso / altura ** 2

# Utilizando f-strings para formatar a saída
# Aqui, estamos construindo a mensagem de saída usando f-strings.
# O f-string permite inserir variáveis e expressões dentro de uma string,
# facilitando a formatação.
output = f"{nome} tem {altura:.2f} de altura,\n" \
         f"pesa {peso} quilos e seu IMC é\n" \
         f"{imc:.2f}"

# Imprimindo a saída
print(output)
