from conexao import conectar

# chama a função conectar
conn = conectar()

# criando um objeto cursor para executar as consultas SQL
cursor = conn.cursor()

nome_tribo = input("Digite o nome da tribo: ")
num_habitante = input("Digite o número de habitantes da tribo: ")
renda_mensal = input("Digite a média da renda mensal da tribo: ")
escolaridade = input("Digite o nível de escolaridade (fundamental, médio ou superior): ")
assalariado = input("Os habitantes possuem trabalho assalariado? Sim ou não somente. ")


# Inserindo na tabela
sql = "INSERT INTO tribo_nativa (nome_tribo, num_habitante, renda_mensal, escolaridade, assalariado) VALUES (%s,%s,%s,%s,%s)"
val = (nome_tribo, num_habitante, renda_mensal, escolaridade, assalariado)
cursor.execute(sql, val)

# Efetuando as mudanças no banco de dados
conn.commit()

print(cursor.rowcount, "registro(s) inserido(s) com sucesso.")

# Fechar a conexão e o cursor
conn.close()
