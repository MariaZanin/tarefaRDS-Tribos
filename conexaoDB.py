import mysql.connector

def conectar():
    mydb = mysql.connector.connect(
    host = '3.230.145.239',
    user ='admin',
    password = 'aula',
    database = 'animais_nativos_africanos'
)

    return mydb
