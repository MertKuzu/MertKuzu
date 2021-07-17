fruits={'apple', 'lemon', 'orange'}

fruits.add('grape')
fruits.update(['strawberry', 'cherry'])


#print(fruits[2])  sets bilgisi indexlenemez

mylist=[1,2,2,3,4,4,4,4,5,6]
print(mylist)
print(set(mylist))    

fruits.remove('grape')
fruits.discard('cherry')
# fruits.clear()

print(fruits)