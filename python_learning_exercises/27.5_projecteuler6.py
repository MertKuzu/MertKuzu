def compute():
    n=100
    sumSquare=sum(i for i in range(1,n+1))        #calculate sum of the square
    squareSum=sum(i**2 for i in range(1,n+1))     #calculate square of the sum
    return (sumSquare**2-squareSum)

def main():
    print(f"Result is {compute()}")

main()