from dbmanager import Dbmanager
from student import Student
from teacher import Teacher
import datetime

class App:
    def __init__(self):
        self.db= Dbmanager()

    def initApp(self):
        msg = "*****\n1-Öğrenci Listesi\n2-Öğrenci Ekle\n3-Öğrenci Güncelle\n4-Öğrenci Sil\n5-Öğretmen Ekle\n6-Çıkış"
        while True:
            print(msg)
            islem = input("Seçim: ")
            if islem == '1':
                self.displayStudents()
            elif islem == '2':
                self.addStudent()
            elif islem == '3':
                self.editStudent()
            elif islem == '4':
                self.deleteStudent()
            elif islem == '5':
                self.addTeacher()
            elif islem == '6':
                print("İyi günler")
                break

    def displayClasses(self):
        classes = self.db.getClasses()
        for c in classes:
            print(f"{c.id}: {c.name}")


    def displayStudents(self):
        self.displayClasses()
        classid = int(input("Hangi sınıf: "))

        students = self.db.getStudentByClassId(classid)
        print("Öğrenci Listesi")
        for std in students:
            print(f"{std.id}-{std.name} {std.surname}")
        return classid

    def addStudent(self):
        self.displayClasses()

        classid = int(input("Hangi sınıf: "))
        number = input("Öğrenci numarası: ")
        name = input("Adı: ")
        surname = input("Soyadı: ")
        year = int(input("Yıl: "))
        month = int(input("Ay: "))
        day = int(input("Gün: "))
        birthdate = datetime.date(year,month,day)
        gender = input("Cinsiyet (E/K): ")

        student = Student(None, number, name, surname, birthdate, gender, classid)
        self.db.addStudent(student)

    def editStudent(self):
        classid = self.displayStudents()
        studentid = int(input("Öğrenci id: "))

        student = self.db.getStudentById(studentid)

        student[0].name = input('Adı: ') or student[0].name
        student[0].surName = input('Soyadı: ') or student[0].surname
        student[0].studentnumber = input('Öğrenci numarası: ') or student[0].studentnumber
        student[0].gender = input('Cinsiyeti (E/K): ') or student[0].gender
        student[0].classid = input('Sınıfı: ') or student[0].classid

        year =int(input("Yıl: "))
        month = int(input("Ay: "))
        day = int(input("Gün: ")) 

        student[0].birthdate = datetime.date(year,month,day)
        self.db.editStudent(student[0])

    def deleteStudent(self):
        classid = self.displayStudents()
        studentid = int(input("Hangi öğrenci: "))

        self.db.deleteStudent(studentid)

    def addTeacher(self):
        branch = input("Branşı: ")
        name = input("Adı: ")
        surname = input("Soyadı: ")
        year = int(input("Yıl: "))
        month = int(input("Ay: "))
        day = int(input("Gün: "))
        birthdate = datetime.date(year,month,day)
        gender = input("Cinsiyeti (E/K): ")

        teacher = Teacher(None, branch, name, surname, birthdate, gender)
        self.db.addTeacher(teacher)


app = App()
app.initApp()