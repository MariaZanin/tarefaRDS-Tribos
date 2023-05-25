import mysql.connector

# Definir as informações de conexão
config = {
  'user': 'admin',
  'password': 'aula',
  'host': '3.230.145.239',
  'database': 'animais_nativos_africanos'
}

# Estabelecer a conexão com o banco de dados
try:
    conn = mysql.connector.connect(**config)
    print("Conexão executada com sucesso.")
except mysql.connector.Error as err:
    print(f"Conexão falhou: {err}")

# Fechar a conexão
conn.close()