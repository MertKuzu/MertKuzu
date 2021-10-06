import numpy as np
from numpy.core.shape_base import vstack

#1- (10, 15, 30, 45, 60) değerlerine sahip numpy dizisi oluşturunuz.

result = np.array([10,15,30,45,60])


#2- (5-15) arasındaki sayılarla numpy dizisi oluşturunuz. 

result = np.arange(5,15)


#3- (50-100) arasında 5'er 5'er artarak numpy dizisi oluşturunuz.

result = np.arange(50,100,5)


#4- 10 elemanlı sıfırlardan oluşan bir dizi oluşturunuz.

result = np.zeros(10)


#5- 10 elemanlı birlerden oluşan bir dizi oluşturunuz.

result = np.ones(10)


#6- (0-100) arasında eşit aralıkta 5 sayı üretin.

result = np.linspace(0,100,5)


#7- (10-30) arasında rastgele 5 tamsayı üretin.

result = np.random.randint(10,30,5)


#8- [-1 ile 1] arasında rastgele 10 adet sayı üretin.

result = np.random.randn(10)


#9- (3x5) boyutlarında [10-50] arasında rastgele bir matris oluşturun.

result = np.random.randint(10,50,15).reshape(3,5)


#10- Üretilen matrisin satır ve sütun sayıları toplamlarını hesaplayınız.

result2 = result.sum(axis=1)
result3 = result2.sum(axis=0)

#11- Üretilen matrisin en büyük, en küçük değeri ve ortalaması nedir?

result2 = result.max()
result3 = result.min()
result4 = result.mean()



#12- Üretilen matrisin en büyük değerinin indeksi kaçtır?

result2 = result.argmax()


#13- (10-20) arasındaki sayıları içeren dizinin ilk 3 elemanını seçiniz.

numbers = np.arange(10,20)
#numbers = numbers[:3]



#14- Üretilen dizinin elemanlarını tersten yazdırınız.

numbers = numbers[::-1]



#15- Üretilen matrisin ilk satırını seçiniz.

result2 = result[:1]


#16- Üretilen matrisin 2. satır 3. sütundaki elemanı hangisidir?

result2 = result[1,2]


#17- Üretilen matrisin tüm satırlardaki ilk elemanı seçiniz.

result2 = result[:,0]


#18- Üretilen matrisin her bir elemanının karesini alınız.

result2 = result ** 2


#19- Üretilen matris elemanlarının hangisi pozitif çift sayıdır?
#       aralığı (-50,50) arasında yapınız.

result = result[result % 2 == 0]












print(result)
#print(result2)
# # print(result3)
# # print(result4)
#print(numbers)