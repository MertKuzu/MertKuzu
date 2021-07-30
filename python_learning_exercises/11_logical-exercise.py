#1 Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz

# num=int(input("Sayı: "))
# result=(num>0) and (num<100)
# print(result)





#2 Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.

# num=int(input("Sayı: "))
# result=(num>=0) and (num%2==0)
# print(result)





#3 Email ve parola bilgileriyle giriş kontrolü yapınız

# emaildb="email@mertkuzu.com"
# passwrdb="abc123"
# email=input("E-mail: ").lower().strip()                             #if result is false, user info is false
# password=input("Password: ")
# isTrue=(emaildb==email) and (passwrdb==password)
# print(isTrue)





#4 Girilen 3 sayıyı büyüklük olarak sıralayınız

# numbers=[]

# num1=int(input("1. Sayı: "))
# numbers.append(num1)
# num2=int(input("2. Sayı: "))
# numbers.append(num2)
# num3=int(input("3. Sayı: "))
# numbers.append(num3)
# numbers.sort()
# print(numbers)





#5 Kullanıcıdan 2 vize (%60) ve 1 final (%40) notunu alıp ortalama yazdırın.
# Eğer ortalama 50 üstündeyse geçti altındaysa kaldı yazdırın
# a) Ortalama 50 olsa bile final notu en az 50 olmalıdır
# b) Finalden 70 alındığında ortalamanın önemi olmasın


vize1=float(input("1. Vize Notu: "))
vize2=float(input("2. Vize Notu: "))
final=float(input("Final Notu: "))
average=(((vize1+vize2)/2)*0.6)+(final*0.4)

result=((final>50) and (average>=50)) or (final>=70)

print(f"Dersi geçme durumunuz: {result}")






