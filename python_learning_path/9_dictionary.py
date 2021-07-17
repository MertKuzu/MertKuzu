plakalar={'Kocaeli': 41, 'İstanbul': 34}    #variable={key:value}
print(plakalar['İstanbul'])
print(plakalar['Kocaeli'])

plakalar['Ankara']=6    

print(plakalar)



users={
    'sadikturan': {
        'age':36,
        'roles':'user',
        'email':'sadik@gmail.com',
        'phone': '123456879',              #her bir bilgiyi ayrı tanımlayınca daha spesifik bilgiyi çekebiliyoruz
        'adress': 'Kocaeli',
    },
    'cinarturan': {
        'age':2,
        'roles':['admin', 'user'],
        'email':'cinar@gmail.com',
        'phone':'123654987',
        'adress':'İstanbul'
    }
}

print(users['cinarturan']['roles'][0])