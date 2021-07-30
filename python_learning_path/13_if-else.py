username=input("Kullanıcı adınızı giriniz: ").strip()
password=input("Parolanızı giriniz: ")

if (username=='uranyum'):
    if (password=='12345'):
        print("Hoş Geldiniz")
    else:
        print("Parolanızı yanlış girdiniz lütfen tekrar deneyiniz.")
else:
    print("Kullanıcı adınızı yanlış girdiniz lütfen tekrar giriniz.")
