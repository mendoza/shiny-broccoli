import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", passwd="root", database="PRUEBA"
)

mycursor = mydb.cursor()

mycursor.execute(
    "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
