import random

randomnum=random.randint(1,100)          

live=int(input("Kaç hak istiyorsunuz: "))           
tryTime=live   #tryTime ı kaç canımız kaldığını hesaplarken live i puan hesaplarken kullandım
playtime=0   #puan hesaplaması için

while tryTime>0:
    tryTime-=1
    playtime+=1
    guess=int(input("Tahmin yapın: "))

    if guess==randomnum:
        print(f"Tebrikler {playtime}. defa da bitirdiniz. Toplam puanınız: {100-(100/live)*(playtime-1)}")
        break
    elif guess>randomnum:
        if tryTime==0:
            print(f"Hakkınız kalmadı. Sayı {randomnum}'idi. Tekrar oynayın.")
        else:
            print("Daha küçük bir sayı deneyiniz.")
    else:
        if tryTime==0:
            print(f"Hakkınız kalmadı. Sayı {randomnum}'idi. Tekrar oynayın.")
        else:
            print("Daha büyük bir sayı deneyiniz.")
    

        
