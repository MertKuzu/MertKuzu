website="http://www.sadikturan.com"
course="Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"

#1 65

print(len(course))

#2 

print(website[7:10])

#3

print(website[22:25])

#4

print(course[:15]) 
print(course[-15:])

#5

print(course[::-1])

name, surname, age, job= "Bora", "Yılmaz", 32, "engineer"

#6

print("My name is {} {}, i am {} years old and i am {}.".format(name, surname, age, job)) 
#or
print(f"My name is {name} {surname}, i am {age} years old and i am {job}.")

#7

s="Hello world"
a=s[:6]+"W"+s[-4:]
print(a)

#8 

s="abc"

print(s+s+s)