#1 gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız.

# def yazdir(kelime, adet):
#     print(kelime*adet)

# yazdir('Merhaba\n', 10)



#2 Kendine gönderilen sınırsız sayıdaki parametreyi bir liteye çeviren fonksyion yazınız.

# def infinteList(*args):
#     liste=[]
#     for arg in args:
#         liste.append(arg)
#     return liste

# result= infinteList(10,20,30,40,50, 'abo', 'xd')
# print(result)



#3 Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.

# def primeNum(num1, num2):
#     for num in range(num1,num2+1):
#         if num>1:
#             for i in range(2,num):
#                 if (num%i==0):
#                     break
#             else:
#                 print(num)

# num1=int(input('1. Sayı: '))
# num2=int(input('2. Sayı: '))       

# primeNum(num1, num2)




#4 Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürün.

def integer(number):
    integerList=[]
    for i in range(2,number):
        if number%i==0:
            integerList.append(i)
    return integerList

number=int(input("Bir sayı girin: "))

result=integer(number)
print(result)