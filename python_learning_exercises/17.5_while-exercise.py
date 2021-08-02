# #5: Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız.

#    ** ürün sayısını kullanıcıya sorun.

#    ** dictionary listesi yapısı (name, price) şeklinde olsun.

#    ** ürün ekleme işlemi bittiğinde ürünleri ekranda for ile listeleyin.



urunler=[]
adet=int(input("Kaç adet ürün eklemek istiyorsunuz: "))

i=0
while i<adet:
    name=input("Ürün ismi: ")
    price=input("Ürün fiyatı: ")
    urunler.append({
        'name': name,
        'price': price,
    })
    i+=1

for urun in urunler:
    print(f"Ürünün ismi: {urun['name']}, Ürünün fiyatı: {urun['price']}")

