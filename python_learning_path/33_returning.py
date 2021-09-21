
# def usalma(number):

#     def inner(power):
#         return number ** power
    
#     return inner

# two = usalma(2)   
# print(two(3))    # 2^3

# three = usalma(3)
# print(three(4))    # 3^4




# def yetki_sorgula(page):

#     def inner(role):
#         if role == 'Admin':
#             return '{0} rolü {1} sayfasına ulaşabilir.'.format(role, page)
#         else:
#             return '{0} rolü {1} sayfasına ulaşamaz.'.format(role, page)

#     return inner

# user1=yetki_sorgula('Product Edit')
# print(user1('Admin'))
# print(user1('User'))



def islem(islem_adi):

    def toplama(*args):
        toplam = 0
        for i in args:
            toplam+=i
        return toplam

    def carpma(*args):
        carpım=1
        for i in args:
            carpım*=i
        return carpım

    if islem_adi == 'toplama':
        return toplama
    else:
        return carpma

toplama=islem('toplama')
print(toplama(2,3,4))
carpma=islem('carpma')
print(carpma(2,3))