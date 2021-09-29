num=int(input("Bir sayı girin: "))
isPrime=True     #First of all every number is prime.

if num==1:
    isPrime=False

for i in range(2,num):
    if (num%i==0):
        isPrime=False    #If number is not a prime number variable will change false

if isPrime:
    print(f"{num} bir asal sayıdır.")
else:
    print(f"{num} bir asal sayı değildir.")

