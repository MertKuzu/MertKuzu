import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "****",
    database = "node-app"
)

def getProduct():
    mycursor = mydb.cursor()

    mycursor.execute("SELECT name,price From product")

    result = mycursor.fetchall()

    #print(result)

    for product in result:
        #print(f"name: {product[1]}, price: {product[2]}")
        print(f"name: {product[0]}, price: {product[1]}")

getProduct()