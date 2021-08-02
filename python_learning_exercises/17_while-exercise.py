#1 numbers listesini while döngüsü ile ekrana yazdırın

# numbers=[1,3,5,7,9,12,19,21]

# i=0
# while i < len(numbers):
#     print(numbers[i])
#     i += 1
    

#2 Başlangıç ve bitiş sayılarını kullanıcıdan alıp arada kalan tüm tek sayıları ekrana yazdırın.


# num1=int(input("Başlangıç sayısı girin: "))
# num2=int(input("Bitiş sayısı girin: "))
# i=num1+1  

# while i<num2:   
#     if i%2==1:
#         print(i)
#     i+=1
    



#3 1-100 arasındaki sayıları azalan şekilde yazdırın.
# a=100
# while a>0:
#     print(a)
#     a-=1




#4 Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın.

numbers=[]

i=0
while i<5:
    num=int(input("Sayı girin: "))
    numbers.append(num)
    i+=1
numbers.sort()
print(numbers)
