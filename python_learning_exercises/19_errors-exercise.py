#1 liste elemanları içindeki sayısal değerleri yazdırın

# liste=["1","2","5a","10b","abc","10","50"]

# for i in liste:
#     try:
#         print(int(i))
#     except:
#         pass





#2 kullanıcı 'q' değerini girmedikçe aldığınız her inputun sayısal 
# bir değer olduğundan emin olunuz aksi halde hata mesajı yazın

# x = input('x: ')
# try:
#     print(int(x))
# except:
#     if x=='q':
#         exit()
#     else:
#         print('Yalnızca sayı')






#3 girilen parola içerisinde türkçe karakter hatası veriniz

# def check_password(psw):
#     import re
#     if re.search('[ı,ğ,ü,ş,ö,ç,İ]', psw):
#         print('Parolada türkçe karakter bulunamaz.')
#     else:
#         pass

# password='ç'

# check_password(password)
        




#4 faktöriyel fonksiyonu oluşturup fonksiyona gelen uygunsuz değer için hata mesajı verin. 

def factorial():
    import re
    import math
    x=input('x: ')
    try:   
        print(math.factorial(int(x)))
    except ValueError:
        print('Geçersiz bir değer girdiniz')
        
    

factorial()