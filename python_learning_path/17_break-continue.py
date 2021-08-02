# name= 'Mert Kuzu'

# for x in name:
#     if x=='t':
#         break
#     print(x)



# for x in name:
#     if x=='t':
#         continue
#     print(x)



# x=0
# while x<5:
#     x+=1
#     if x==3:
#         continue
#     print(x)





#1-100 e kadar tek sayıların toplamı

x=0
result=0

while x<=100:
    x+=1
    if x%2==0:
        continue
    result+=x
print(result)