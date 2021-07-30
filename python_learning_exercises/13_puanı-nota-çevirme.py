grade1=float(input("İlk yazılı notunuz: "))
grade2=float(input("İkinci yazılı notunuz: "))
grade3=float(input("Sözlü notunuz: "))
average=(grade1+grade2+grade3)/3

if (average<=24):
    print("Notunuz: 0")
elif (average>24 and average<=44):
    print("Notunuz: 1")
elif (average>44 and average<=54):
    print("Notunuz: 2")
elif (average>54 and average<=69):
    print("Notunuz: 3")
elif (average>69 and average<=84):
    print("Notunuz: 4")
elif (average>84 and average<=100):
    print("Notunuz: 5 Tebrikler")
else:
    print("Yanlış bilgi girdiniz.")