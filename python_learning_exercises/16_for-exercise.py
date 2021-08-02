#1 numbers listesindeki hangi sayılar 3'ün katıdır?
#2 numbers listesindeki sayıların toplamı kaçtır?
#3 numbers listesindeki tek sayıların karesini alınız.

numbers=[1,3,5,7,9,12,19,21]


#1
# for num3 in numbers:         
#     if (num3%3==0):
#         print(num3)  
   



#2 
# total=0
# for num in numbers:
#     total += num
# print('toplam:', total)        #eğer for bloğundan çıkarmazsak printi bir sürü toplam çıkıyor





#3
# for num in numbers:
#     if (num%2==1):
#         print(num**2)





cities=['kocaeli', 'istanbul', 'ankara', 'izmir', 'rize']

#4 şehirlerden hangisi en fazla 5 harflidir?

# for city in cities:
#     if (len(city)<=5):
#         print(city)
    



telephone= [
    {'name':'samsung s6', 'price':3000},
    {'name':'samsung s7', 'price':4000},
    {'name':'samsung s8', 'price':5000},
    {'name':'samsung s9', 'price':6000},
    {'name':'samsung s10', 'price':7000},
]

#5 Ürünlerin toplam fiyatı nedir?
# total=0
# for dictionary in telephone:
#     total += dictionary['price']        #döngüden sadece fiyatları aldık
# print(total)
    
#6 Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz.

for mobile in telephone:
    if (mobile['price']<=5000):
        print(mobile['name'])

