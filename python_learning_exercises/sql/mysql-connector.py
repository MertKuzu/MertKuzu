import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "****",
    database = "mydatabase"
)

mycursor = mydb.cursor()

# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#     print(x)

mycursor.execute("CREATE TABLE customers(name VARCHAR(255), adress VARCHAR(255))")


#print(mydb)