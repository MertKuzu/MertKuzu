import mysql.connector 

def insertProduct(list):
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "*****",
        database = "node-app"
    )

    cursor = connection.cursor()

    sql = "INSERT INTO Product(name,price,imageUrl,description) VALUES(%s,%s,%s,%s)"   #added new value
    values = (list)

    cursor.executemany(sql,values)

    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi.")
        print(f"Eklenen son ürünün id numarası: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("hata: ", err)
    finally:
        connection.close()
        print("database bağlantısı kapandı")

list = []
while True:
    name = input("Ürün adı: ")
    price = float(input("Ürün fiyatı: "))
    imageUrl = input("Ürünün resminin adı: ")
    description = input("Ürünün açıklaması: ")
    list.append((name,price,imageUrl,description))

    result = input("Devam etmek istiyor musunuz? (e/h)")
    if result == "h":
        print("Kayıtlarınız yapılıyor...")
        print(list)
        insertProduct(list)
        break
    
    
    

insertProduct(name, price, imageUrl, description)