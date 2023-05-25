from conexao import conectar

conn = conectar()

cursor = conn.cursor()

busca = input('Digite o nome da tribo que deseja bsucar: ')

sql = 'SELECT * FROM tribo_nativa WHERE nome_tribo LIKE %s'
val = ('%'+busca+'%',)
cursor.execute(sql,val)

result = cursor.fetchone()
if result:
    nome_tribo = result[1]
    nome = result[1]
    confirmacao = input(f"Tem certeza que deseja deletar a tribo'{nome}'? (s/n)")
    if confirmacao.lower() == 's':
        sql = 'DELETE FROM tribo_nativa WHERE nome_tribo = %s'
        val = (nome_tribo,)
        cursor.execute(sql,val)
        conn.commit()
        print(f"A tribo'{nome}'foi deletada com sucesso!")
    else:
        print('Operação cancelada pelo usuário.')
else: 
 print('Não foi encontrada nenhuma tribo com o nome informado.')

conn.close()