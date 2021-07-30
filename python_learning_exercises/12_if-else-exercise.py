name=input("Adınız: ")
age=int(input("Yaşınız: "))
edu=input("Eğitim durumunuz: ").lower().strip()  #kullanıcı büyük harf kullanırsa falan hatayı engellemek için metod

if (edu=="lise" or edu=="üniversite") and (age>18):
    print(f"{name}, ehliyet alabilirsin.")
else:
    print(f"{name}, ehliyet alamazsın.")


