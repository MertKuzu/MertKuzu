
def calculateGrade(info):
    info = info[:-1]     #it deletes empty line
    liste = info.split(':')  
    studentName = liste[0]
    studentGrades = liste[1].split(',')
    grade1=int(studentGrades[0])
    grade2=int(studentGrades[1])
    grade3=int(studentGrades[2])

    average=(grade1+grade2+grade3)/3

    if average>=90 and average<=100:
        letter='AA'
    elif average>=85 and average<=89:
        letter='BA'
    elif average>=80 and average<=84:
        letter='BB'
    elif average>=70 and average<=79:
        letter='CB'
    elif average>=60 and average<=69:
        letter='CC'
    elif average>=50 and average<=59:
        letter='DC'
    elif average>=45 and average<=49:
        letter='DD'
    else:
        letter='FF'

    return studentName + ': ' + letter + '\n'   #it is returning to back with the information


def readGrade():
    with open("students_info.txt","r",encoding="utf-8") as file:
        for info in file:
            print(calculateGrade(info))


def enterGrade():
    name=input('Adı: ')
    surname=input('Surname: ')
    grade1=input('Not 1: ')
    grade2=input('Not 2: ')
    grade3=input('Not 3: ')
    with open("students_info.txt","a",encoding="utf-8") as file:
        file.write(name+' '+surname+':'+grade1+','+grade2+','+grade3+'\n')

def saveGrade():
    with open("students_info.txt","r",encoding="utf-8") as file:
        liste=[]

        for x in file:
            liste.append(calculateGrade(x))

        with open("results.txt","w",encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)

def goNext():
    while True:
        next=input('Başka işlem yapmak istiyor musunuz? (e/h)')
        if next=='e':
            break
        elif next=='h':
            print('İyi günler dileriz.')
            exit()   
        else:
            print('Hatalı tuşladınız. Tekrar deneyin.')  


while True:
    process=input("1- Notları Oku\n2- Not Gir\n3- Notları Kaydet\n4- Çıkış\n")

    if process == '1':
        readGrade()
        goNext()
    elif process == '2':
        enterGrade()
        goNext()
    elif process =='3':
        saveGrade()
        goNext()
    else:
        print('İyi günler')
        break
