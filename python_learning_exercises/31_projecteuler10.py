#this can't find the answers in a short time 
#31.5_projecteuler10.py is the fastest than this.
def main():
    i,total=2,0
    while i<2000000:
        total += prime(i)
    print(total)

#calculating prime numbers
def prime(n):
    i,k=2,1
    while i<n:
        if n%i==0:
            k=0
            break
        else:
            k=1
    if k==0:
        return 0
    else:
        return n

main()
