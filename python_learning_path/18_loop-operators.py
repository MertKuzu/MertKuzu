#range
# for item in (range(2,50,10)):
#     print(item)

# print(list(range(2,50,5)))




#enumerate

# index=0
# greeting='Hello'

# for letter in greeting:
#     print(f'index: {index}, harf: {letter}')
#     index+=1


# greeting='Hello'

# for index,letter in enumerate(greeting):
#     print(f"index: {index} harf: {letter}")


#zip

list1=[1,2,3,4,5]
list2=['a','b','c','d','e']
list3=[100,200,300,400,500]

for item in zip(list1, list2, list3):
    print(item)

for a,b,c in zip(list1, list2, list3):
    print(a,b,c)