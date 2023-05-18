import mysql.connector

# Definir as informações de conexão
config = {
  'user': 'admin',
  'password': 'mlvz1993',
  'host': 'database-1.crgpplos0jpm.us-east-1.rds.amazonaws.com',
  'database': 'tribos'
}

# Estabelecer a conexão com o banco de dados
try:
    conn = mysql.connector.connect(**config)
    print("Conexão executada com sucesso.")
except mysql.connector.Error as err:
    print(f"Conexão falhou: {err}")

# Fechar a conexão
conn.close()