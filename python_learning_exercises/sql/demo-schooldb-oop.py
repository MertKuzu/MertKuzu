import mysql.connector
from datetime import datetime
from connection import mydb 

class Student:
    connection = mydb
    mycursor = connection.cursor()

    def __init__(self, id, studentnumber, name, surname, birthdate, gender):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.studentnumber = studentnumber
        self.name = name
        self.surname = surname
        self.birthdate = birthdate 
        self.gender = gender

    def saveStudent(self):
        sql = "INSERT INTO student(studentNumber,name,surName,birthDate,gender) VALUES(%s,%s,%s,%s,%s)"
        values = (self.studentnumber,self.name,self.surname,self.birthdate,self.gender)
        Student.mycursor.execute(sql,values)

        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt eklendi.")
        except mysql.connector.Error as err:
            print("Hata", err)
        finally:
            Student.connection.close()
            print("Bağlantı kapandı.")

    @staticmethod
    def saveStudents(students):
        sql = "INSERT INTO student(studentNumber,name,surName,birthDate,gender) VALUE(%s,%s,%s,%s,%s)"
        values = students
        Student.mycursor.executemany(sql,values)

        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt eklendi.")
        except mysql.connector.Error as err:
            print("Hata", err)
        finally:
            Student.connection.close()
            print("Bağlantı kapandı.")

    @staticmethod
    def getStudents():
        # sql = "select * from student"
        # sql = "select * from student LIMIT 3"
        # sql = "select studentnumber,name,surname from student"
        # sql = "select name,surname from student where gender='K'"
        # sql = "SELECT * FROM student WHERE YEAR(birthdate) = '2003'"
        # sql = "SELECT * FROM student WHERE YEAR(birthdate) = '2005' and name = 'Ali'"
        # sql = "SELECT * FROM student WHERE name LIKE '%an%' or surName LIKE '%an%'"
        # sql = "SELECT COUNT(gender) FROM student WHERE gender = 'E'"
        sql = "SELECT * FROM student WHERE gender = 'K' Order By name, surName"
        Student.mycursor.execute(sql)
        result = Student.mycursor.fetchall()   
        for student in result:
            print(student)  
          
    @staticmethod
    def getStudentById(id):
        sql = "SELECT * FROM student WHERE id=%s"
        value = (id,)

        Student.mycursor.execute(sql,value)

        try:
            obj = Student.mycursor.fetchone()
            return Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5])
        except mysql.connector.Error as err:
            print("Error", err)

    def updateStudent(self):
        sql = "UPDATE student SET studentNumber=%s,name=%s,surName=%s,birthDate=%s,gender=%s WHERE id=%s"
        values=(self.studentnumber,self.name,self.surname,self.birthdate,self.gender,self.id)
        Student.mycursor.execute(sql,values)

        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt güncellendi.")
        except mysql.connector.Error as err:
            print("Error", err)

    
    @staticmethod
    def updateStudents(liste):
        sql = "UPDATE student SET studentNumber=%s,name=%s,surName=%s,birthDate=%s,gender=%s WHERE id=%s"
        values = []
        order = [1,2,3,4,5,0]

        for item in liste:
            item = [item[i] for i in order]
            values.append(item)

        Student.mycursor.executemany(sql,values)


        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kayıt güncellendi')
        except mysql.connector.Error as err:
            print('Hata:',err)


    @staticmethod
    def getStudentsGender(gender):
        sql = "SELECT * FROM student WHERE gender = %s"
        value = (gender, )

        Student.mycursor.execute(sql,value)

        try:
            return Student.mycursor.fetchall()
        except mysql.connector.Error as err:
            print('Error', err) 





students = Student.getStudentsGender('E')

print(students)

liste = []
for std in students:
    std = list(std)
    std[2] = 'Mr '+std[2]
    liste.append(std)

Student.updateStudents(liste)

# student = Student.getStudentById(3)
# student.name = 'Çınar'
# student.surname = 'Turan'

# student.updateStudent()


# a = Student("301","Ahmet","Yılmaz",datetime(2005,5,17),"E")
# a.saveStudent()



# students = [
#     ("401","Mert","Kuzu",datetime(2001, 5, 17),"E"),
#     ("302","Ali","Can",datetime(2005, 6, 17),"E"),
#     ("303","Canan","Tan",datetime(2005, 7, 7),"K"),
#     ("304","Ayşe","Taner",datetime(2005, 9, 23),"K"),
#     ("305","Bahadır","Toksöz",datetime(2004, 7, 27),"E"),
#     ("306","Ali","Cenk",datetime(2003, 8, 25),"E")
# ]

# #Student.saveStudents(students)

# Student.getStudents()




    