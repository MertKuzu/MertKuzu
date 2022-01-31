import mysql.connector 

def insertStudent(student):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "*****",
        database = "schooldb"
    )

    cursor = mydb.cursor()

    sql = "INSERT INTO student(studentNumber,name,surName,birthDate,gender) VALUES(%s,%s,%s,%s,%s)"
    values = (student)

    cursor.executemany(sql,values)

    try:
        mydb.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi.")
        print(f"Eklenen son ürünün id numarası: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("hata",err)

    finally:
        print("Kayıt tamamlandı.")
        mydb.close()
        print("Database bağlantısı kapatıldı.")


students = []
while True:
    studentNumber = int(input("Öğrenci numarası: "))
    name = input("Öğrenci adı: ")
    surname = input("Öğrenci soyadı: ")
    birthDay = input("Doğum tarihi: ")
    gender = input("Cinsiyeti: ")

    students.append((studentNumber,name,surname,birthDay,gender))

    result = input("Başka kayıt etmek istediğiniz bir öğrenci daha var mı? (e/h)")

    if result == "h":
        print("Kayıt işlemi tamamlanıyor...")
        print(students)
        insertStudent(students)
        break

    



