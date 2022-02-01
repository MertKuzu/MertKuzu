def main():
    i,k=2,0
    while True:
        n = prime_number(i)
        if n==0:        #prime number counter
            k += 1
        if k==10001:
            print(f"10001st prime number is {i}")
            break
        i+=1
        
def prime_number(num):
    i,k=2,0
    while i<num:
        if(num%i==0):
            k=1
            break
        else:
            k=0
        i+=1
    return k

main()