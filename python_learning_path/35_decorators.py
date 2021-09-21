# def my_decorator(func):
#     def wrapped(name):
#         print("Fonksiyondan önceki işlemler")
#         func(name)
#         print("Fonksiyondan sonraki işlemler")
#     return wrapped

# @my_decorator
# def sayHello(name):
#     print("Hello", name)

# sayHello("ali")




# def greeting():
#     print("greeting")

# sayHello = my_decorator(sayHello)
# sayHello()
# # greeting = my_decorator(greeting)
# # greeting()





import math
import time

def calculate_time(func):
    def inner(*args,**kwargs):
        start = time.time()
        time.sleep(1)
        func(*args,**kwargs)
        finish=time.time()
        print("Fonksiyon "+ func.__name__+" "+str(finish-start))

    return inner

@calculate_time
def pow(a,b):
    print(math.pow(a,b))

@calculate_time
def factorial(num):
    print(math.factorial(num))


pow(3,4)
factorial(5)