# x = 10

# if x > 5:
#     raise Exception("x 5 den büyük olamaz")


def check_password(psw):
    import re
    if len(psw) < 8:
        raise Exception("Parola en az 8 karakterli olmalıdır.")
    elif not re.search("[a-z]", psw):
        raise Exception("Parola küçük harf içermelidir.")
    elif not re.search("[A-Z]", psw):
        raise Exception("Parola büyük harf içermelidir.")
    elif not re.search("[0-9]", psw):
        raise Exception("Parola rakam içermelidir.")
    elif re.search("\s", psw):
        raise Exception("Parola boşluk içermemelidir.")
    else:
        print("Geçerli parola")

password = '12345678aB'

try:
    check_password(password)
except Exception as error:
    print(error)
else:
    print("Geçerli parola: else")
finally:
    print("validation complete.")



class Person:
    def __init__(self, name):
        if len(name)>10:
            raise Exception("İsim bilgisi 10 karakterden uzun olamaz")
        else:
            self.name = name

a=Person('kuzuuuuuuuuuuuuu')