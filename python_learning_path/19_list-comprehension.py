numbers=[x*x for x in range(10) if x%2==0]
print(numbers)

myString="Hello"
myLetters=[]

for letter in myString:
    myLetters.append(letter)
print(myLetters)

myLetters=[letter for letter in myString]
print(myLetters)



result=[x if x%2==0 else 'TEK' for x in range(1,10)]
print(result)


result2=[]

for x in range(3):
    for y in range(3):
        result2.append((x,y))
print(result2)



number=[(x,y) for x in range(3) for y in range (3)]
print(number)