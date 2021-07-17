students={}                          #tüm hepsi studentsın içine

no1=input('Öğrenci numaranı: ')
name1=input('Adınız: ')
surname1=input('Soyadınız: ')
phone1=input('Telefon numaranız: ')

no2=input('Öğrenci numaranız: ')             #Burada kullanıcılardan bilgilerini alıyoruz.
name2=input('Adınız: ')
surname2=input('Soyadınız: ')
phone2=input('Telefon numaranız: ')

no3=input('Öğrenci numaranız: ')
name3=input('Adınız: ')
surname3=input('Soyadınız: ')
phone3=input('Telefon numaranız: ')


students[no1]={
    'Ad':name1,
    'Soyad':surname1,                    #Aldığın bilgileri students dictionarysine no1 olarak onunda alt başlığı olarak
    'Telefon':phone1                      #diğer bilgileri inputluyoruz
}

students[no2]={
    'Ad':name2,
    'Soyad':surname2,
    'Telefon':phone2
}

students[no3]={
    'Ad':name3,
    'Soyad':surname3,
    'Telefon':phone3
}

print(students)

studentsno=input('Öğrenci no giriniz: ')    #nnumaraya özel bilgi alma 
student=students[studentsno]
print(student)
