import datetime

day=input("Araç hangi tarihte trafiğe çıktı (2019/8/7): ")      #Kullanıcıdan tarih bilgisini alıyoruz
day=day.split("/")           #Aldığımız tarih bilgisini bölüyoruz
now=datetime.datetime.now()     #şimdiki zamanın tarihi
traffic=datetime.datetime(int(day[0]), int(day[1]), int(day[2]))    #böldüğümüz string tarihi işleme sokulur tarih haline getiriyoruz 
repairTime=now-traffic     #şimdiki zamandan kullanıcıdan aldığımızı çıkardık
days=repairTime.days

if days<365:
    print("1. Bakım")
elif days>365 and days<=365*2:
    print("2. Bakım")
elif days>365*2 and days<=365*3:
    print("3. Bakım")
else:
    print("Sat yenisini al")