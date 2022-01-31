import mysql.connector
from datetime import datetime
from connection import connection
from Class import Class
from student import Student
from teacher import Teacher



class Dbmanager:
    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()


    def getStudentById(self, id):
        sql = "SELECT * FROM student WHERE id = %s"
        value = (id,)

        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchone()
            return Student.createStudent(obj)
        except mysql.connector.Error as err:
            print("Error", err)

    def getStudentByClassId(self,classid):
        sql = "SELECT * FROM student WHERE classid = %s"
        value = (classid,)

        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchall()
            return Student.createStudent(obj)
        except mysql.connector.Error as err:
            print("Error", err)

    def addStudent(self, student: Student):
        sql = "INSERT INTO Student(studentNumber,name,surName,birthDate,gender,classid) VALUES (%s,%s,%s,%s,%s,%s)"
        value = (student.studentnumber,student.name,student.surname,student.birthdate,student.gender,student.classid)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt eklendi.")
        except mysql.connector.Error as err:
            print("Error: ", err)
        
    def deleteStudent(self,studentid):
        sql = "delete from student where id=%s"
        value = (studentid,)
        self.cursor.execute(sql,value)
        
        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt eklendi.')
        except mysql.connector.Error as err:
            print('hata:', err)

    def getClasses(self):
        sql = "select * from class"
        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchall()
            return Class.CreateClass(obj)
        except mysql.connector.Error as err:
            print('Error:', err)

    def editStudent(self, student: Student):
        sql = "update student set studentNumber=%s,name=%s,surName=%s,birthDate=%s,gender=%s,classid=%s where id=%s"
        value = (student.studentnumber,student.name, student.surname,student.birthdate,student.gender,student.classid,student.id)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt güncellendi.')
        except mysql.connector.Error as err:
            print('hata:', err) 

    def addTeacher(self, teacher: Teacher):
        sql = "INSERT INTO Teacher(branch,name,surname,birthdate,gender) VALUES(%s,%s,%s,%s,%s)"
        values = (teacher.branch,teacher.name,teacher.surname,teacher.birthdate,teacher.gender)
        self.cursor.execute(sql,values)

        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt eklendi.")
        except mysql.connector.Error as err:
            print("Error: ", err)


    def __del__(self):
        self.connection.close()
        print('db silindi')


