# try: 
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x/y)
# except ZeroDivisionError:
#     print('y 0 değeri yazılamaz')
# except ValueError:
#     print('Sayısal bir değer girmelisiniz')

while True:
    try:
        x = int(input("x: "))
        y = int(input("y: "))
        print(x/y)
    except Exception as error:
        print("Yanlış değer girdiniz", error)
    else:
        break
    finally:
        print("try except sonlandırıldı")
