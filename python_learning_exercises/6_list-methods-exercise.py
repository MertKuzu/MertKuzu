names=['Ali', 'Yağmur', 'Hakan', 'Deniz']
years=[1998, 2000, 1998, 1987]

#1 add "cenk" end of the list

names.append("Cenk")

#2 add "sena" head of the list

names.insert(0, "Sena")

#3 remove "Deniz"

names.pop(4)

# or names.remove("Deniz")

#4 what is "hakan" index

a=names.index('Hakan')

print(a)

#5 Is ali element of the list
b="Ali" in names
print(b)

#6 reverse list elements

names.reverse()

#7 this is alphabetic order of the list

names.sort()

print(names)

#8 order years list >

years.sort()
years.reverse()

#9 str="Chevrolet, Dacia" convert string to list

str="Chavrolet, Dacia"
print(str.split())

#10 what is big and small element in years list

c=min(years)
d=max(years)
print(c, d)


#11 how many 1998 elements does have in years list

k=years.count(1998)
print(k)

#12 delete all elements in years list

years.clear()


print(years)

 



