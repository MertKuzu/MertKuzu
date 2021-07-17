x, y, z= 2, 5, 17
numbers= 1, 5, 7, 10, 6

#1 

a=float(input("İlk sayıyı giriniz: "))         # str değeri floata çevirip işleme soktum
b=float(input("İkinci sayıyı giriniz: "))

result=(a*b)-(x+y+z)

print(result)

#2 

# y//= x

# print(y)

#3 

c=(x+y+z)
xd=c%3
print(xd)

#4

# y**=x
# print(y)

#5 
x, *y, z= numbers
z**=3
print(z)

#6

#print(len(y))  #kaç tane y değeri var ona bakmak için y değerlerini kendi içinde toplayacaz

print(y[0]+y[1]+y[2])




