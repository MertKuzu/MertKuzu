j,k,l = 1,1,1

def main():
    while True:
        if pythagorean() == 0:
            check()


def check():
    global j,k,l
    result = (j-1)+k+l
    if result == 1000:
        print((j-1)*k*l)
        exit()

#computing pythogorean digits
def pythagorean():
    global j,k,l      
    while True:
        while k<l:
            while j<k:
                result = j*j+k*k
                j += 1
                if result == l*l:
                    return 0
            k += 1
            j = 1
        l += 1
        k = 1

main()