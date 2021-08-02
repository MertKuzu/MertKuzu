num=int(input("Bir sayı girin: "))
isPrime=True     #her sayı asal kabul ediliyor aşağıda şartlar

if num==1:
    isPrime=False

for i in range(2,num):
    if (num%i==0):
        isPrime=False    #eğer kalansız bölüm varsa asal değil

if isPrime:
    print(f"{num} bir asal sayıdır.")
else:
    print(f"{num} bir asal sayı değildir.")

