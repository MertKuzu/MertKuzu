def main():
    if(squaresum()<sumsquare()):
        result=sumsquare()-squaresum()
    else:
        result=squaresum()-sumsquare()
    print(f"Result is {result}")

def squaresum():     #calculate square of the sum
    i,total=1,0
    while(i<=100):
        total+=i*i
        i+=1
    return total

def sumsquare():     #calculate sum of the square
    i,total=1,0
    while(i<=100):
        total+=i
        i+=1
    total*=total
    return total

main()