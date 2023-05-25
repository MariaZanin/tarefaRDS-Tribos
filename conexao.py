import mysql.connector

def conectar():
    mydb = mysql.connector.connect(
    host = 'database-1.crgpplos0jpm.us-east-1.rds.amazonaws.com',
    user ='admin',
    password = 'mlvz1993',
    database = 'tribos'
)

    return mydb