from conexaoDB import conectar

# chama a função conectar
conn = conectar()

# criando um objeto cursor para executar as consultas SQL
cursor = conn.cursor()

# solicitando a entrada do usuário
busca = input("Digite o nome do animal que deseja editar: ")

# executando a consulta com LIKE para verificar se o registro existe
sql = "SELECT * FROM animais WHERE raca LIKE %s"
val = ("%" + busca + "%",)
cursor.execute(sql, val)

# obtendo o resultado
result = cursor.fetchone()

# print (result[0], result[1])

# se o resultado não for nulo, o registro existe e pode ser editado
if result:
    raca = result[1]
    nome_antigo = result[1]
    print(f"O nome atual da raça é '{nome_antigo}'.")
    novo_nome = input("Digite o novo nome da raça: ")

    # solicita as novas informações para o registro
    while not novo_nome:
        novo_nome = input("Digite o novo nome da raça: ")

    confirmacao = input(f"Tem certeza que deseja alterar o nome da raça '{nome_antigo}' para '{novo_nome}'? (s/n) ")

       # se a confirmação for positiva, atualiza o registro
    if confirmacao.lower() == "s":
        sql = "UPDATE animais SET raca = %s WHERE raca = %s"
        val = (novo_nome, raca)
        cursor.execute(sql, val)
        conn.commit()
        print(f"O nome da raça '{nome_antigo}' foi atualizado para '{novo_nome}' com sucesso!")
    else:
        print("Operação cancelada pelo usuário.")

# se o resultado for nulo, o registro não existe
else:
    print("Não foi encontrada nenhuma raça com o nome informado.")

# fechar a conexão e o cursor
conn.close()