def sayHello(name='user'):
    return "Hello "+ name

msg=sayHello("kUZU")
print(msg)

def birthDay(birthday):
    return 2021-birthday

yearsOld=birthDay(int(input("Doğum yılınızı girin: ")))
#print(birthday)


def emeklilik(birthday):
    age2=birthDay(birthday)
    retired=65-age2

    if retired>0:
        print(f"Emekliliğinize {retired} yıl kalmıştır.")
    else:
        print("Zaten emeklisiniz.")

emeklilik(20)
