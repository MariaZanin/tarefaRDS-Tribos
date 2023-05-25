from conexaoDB import conectar

# chama a função conectar
conn = conectar()

# criando um objeto cursor para executar as consultas SQL
cursor = conn.cursor()

raca = input("Digite a raça do animal: ")
quantidade = input("Digite o número de animais encontrados: ")
extincao = input("Digite se o anima se encontra em extinção: (sim ou nao): ")
area = input("Digite a área geográgica onde se encontra o animal: (norte,sul, leste ou oeste): ")


# Inserindo na tabela
sql = "INSERT INTO animais (raca, quantidade, extincao, area) VALUES (%s,%s,%s,%s)"
val = (raca, quantidade, extincao, area)
cursor.execute(sql, val)

# Efetuando as mudanças no banco de dados
conn.commit()

print(cursor.rowcount, "registro(s) inserido(s) com sucesso.")

# Fechar a conexão e o cursor
conn.close()
