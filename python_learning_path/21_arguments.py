# def changeName(n):
#     n='ada'

# name='yiğit'

# changeName(name)
# print(name)

# def change(n):
#     n[0]='istanbul'

# sehirler=['ankara','izmir']
# #change(sehirler)

# change(sehirler[:])
# print(sehirler)



# def add(a,b):
#     return sum((a,b))

# print(add(10,20))


# def add(*params):
#     print(params[0])
#     print(params[1])
#     return sum((params))

# print(add(10,20))
# print(add(20,50,70,20))
# print(add(10,20,30,50,4,8,42))

def displayUser(**args):
    print(type(args))
    for key, value in args.items():
        print('{} is {}'.format(key,value))

displayUser(name='Çınar', age=2, city='İstanbul')
displayUser(name='Ada', age=12, city='kocaeli', phone='161651616')
displayUser(name='yiğit', age=14, city='ankara', phone='61516516261', email='yiğit@gmail.com')



def myFunction(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myFunction(10,5,6,52,87,62,45,12,31, key1='value1', key2='value2')
