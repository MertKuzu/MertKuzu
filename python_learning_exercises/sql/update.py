import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Laj49f8j9wq6r9g6*",
    database = "node-app"
)

def updateProduct(id, name, price):
    cursor = connection.cursor()

    sql = "UPDATE product SET name =%s, price =%s WHERE id =%s"
    values = (name,price,id)

    cursor.execute(sql,values)

    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt güncellendi.")
        print(f"Eklenen son ürünün id numarası: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("hata: ", err)
    finally:
        connection.close()
        print("database bağlantısı kapandı")

updateProduct(4,'Iphone 13',15000)