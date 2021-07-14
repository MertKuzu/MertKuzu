website="http://www.sadikturan.com"
course="Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"

#1

s=" Hello World "
s=s.strip()
print(s)

#2

a=website.lstrip("http://www.").rstrip(".com")
print(a)

#3

b=course.lower()
print(b)

#4

c=website.count("a")
print(c)

#5

d=website.startswith("www")
e=website.endswith("com")
print(d)
print(e)

#6

f=website.find(".com")
print(f)

#7

g=course.isalpha()
print(g)

#8

h="Contents"
h=h.center(50,"*")
print(h)

#9

k=course.replace(" ","-")
print(k)

#10

j=s.replace("World","There")
print(j)

#11

u=course.split(" ")
print(u)