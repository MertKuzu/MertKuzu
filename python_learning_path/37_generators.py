def cube():
    for i in range(5):
        yield i**3           #yield ile bellekte yer tutmuyoruz sadece ihtiyacımız olduğunda kullanılıyor ve siliniyor bilgi

for i in cube():
    print(i)



generator = (i**3 for i in range(5))       #veya bu şekilde de yapılabilir köşeli yerine normal parantez 

for i in generator:
    print(i)