import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "*****",
    database = "node-app"
)

def getProductInfo():
    cursor = mydb.cursor()

    #sql = "SELECT COUNT(*) FROM product"
    #sql = "SELECT AVG(Price) FROM product"
    #sql = "SELECT SUM(price) FROM product"
    #sql = "SELECT MIN(price) FROM product"
    #sql = "SELECT MAX(price) FROM product"
    sql = "SELECT name,price FROM product WHERE price = (SELECT MAX(price) FROM product)"


    cursor.execute(sql)

    result = cursor.fetchone()


    print(f"{result[0]} {result[1]}")



getProductInfo()