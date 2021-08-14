
# class Person: 
#     #class
#     adress='no info'
#     #constructor
#     def __init__(self, name, year):
#         self.name=name
#         self.year=year 
#         print('init çalıştı')

#     def intro(self):
#         print('Hello there.')

#     def calculateAge(self):
#         return 2021 - self.year

# p1=Person('mert', 2001)

# #update

# p1.adress='istanbul'

# print(f'name: {p1.name} year: {p1.year} adress: {p1.adress}')

# p1.intro()

# print(f'Yaş: {p1.calculateAge()} İsim: {p1.name}')


class Circle:
    #class object attiribute
    pi=3.14

    def __init__(self, yarıcap=1):
        self.yarıcap=yarıcap

    #methods

    def cevre_hesapla(self):
        return 2 * self.pi * self.yarıcap
    
    def alan_hesapla(self):
        return self.pi*(self.yarıcap**2)


c1=Circle()  #yarıçap 1 
c2=Circle(5)

print(f"c1: alan: {c1.alan_hesapla()} çevre: {c1.cevre_hesapla()}")
print(f"c2: alan: {c2.alan_hesapla()} çevre: {c2.cevre_hesapla()}")
