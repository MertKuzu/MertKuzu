cars=["BMW", "Mercedes", "Opel", "Mazda"]

#2 this is how many elements does have list

print(len(cars))

#3 what is first and last element in list

print(cars[0])
print(cars[3])

#4 change mazda value to toyota
cars[3]="Toyota"
print(cars)

#5 is mercedes element of the list?
a=cars.count("Mercedes")
print(a)
#if it's not, answer will be 0 or
result="Mercedes" in cars
print(result)
#if it's not, answer will be false

#6 what is -2 index value of the list
print(cars[-2])

#7 take first 3 element in the list
print(cars[0:3])


#8 change last 2 elements "toyota", "renault" 

cars[2:4]="Toyota","Renault"
print(cars)

#9 add "nissan" and "audi" valua in list

cars.append("Nissan")     #.append method is add an element to end of the list
cars.append("Audi")
print(cars)

#10 delete last element of the list

cars.remove("Audi")
print(cars)
#or
# del cars[-1]

#11 print reverse list

cars.reverse()
print(cars)

#or print(cars[::-1])

#12 

studentA=["Yiğit", "Bilgi", 2010, [70, 60, 70]]
studentB=["Sena", "Turan", 1999, [80, 80, 70]]
studentC=["Ahmet", "Turan", 1998, [80, 70, 90]]

students=[studentA+studentB+studentC]
float=(studentA[3][0] + studentA[3][1] + studentA[3][2])/3
limited_float=round(float, 3)       #this is for short float
print(f"{studentA[0]} {studentA[1]} {2021-studentA[2]} yaşında ve not ortalaması {limited_float}")