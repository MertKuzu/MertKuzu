#1 Girilen 2 sayıdan hangisi büyüktür?
# a=int(input("Bir sayı giriniz: "))
# b=int(input("Bir sayı daha giriniz: "))
# result=(a>b)
# print(f"{a}, {b}'den büyüktür. {result}")

#2 Kullanıcıdan  vize (%60) ve final (%40) notunu alıp ortalama hesaplayın
# eğer ortalama 50den küçükse kaldı büyükse geçti yazsın

# c=float(input("İlk vize notunuzu giriniz: "))
# d=float(input("Final notunuzu giriniz: "))

# average=(((60/100)*c)+((40/100)*d))
# if (average >= 50):
#     print("Dersi Geçtiniz!")
# else:  print("Dersten Kaldınız Hadi baba geçmiş olsun!")

# print("Ortalamanız: ", average)
    
#3 girilen sayının tek mi çift mi 

# e=int(input("Bir sayı giriniz: "))  #if it is even result true if it is not result false
# oddeven=(e%2==0)
# print(oddeven)

#4 girilen sayı negatif mi pozitif mi

# num=int(input("Bir sayı girin: "))
# result=(num >= 0)                             #if it is positive result true if it is not result false
# print(result)

#5 parola ve e posta bilgilerini isteyip doğruluğunu kontrol ediniz.
emaildb="email@mertkuzu.com"
passworddb="abc123"

email=input("E-mail: ")
password=input("Parola: ")

result=(emaildb==email, passworddb==password)
print(result)
