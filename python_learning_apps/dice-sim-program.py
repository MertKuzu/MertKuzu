import random

def dice():
    diceNum=['1','2','3','4','5','6']
    print(random.choice(diceNum))

while True:
    diceRoll=input('Zar at! (e)/ Çıkış yap! (q)')
    if diceRoll=='e':
        dice()
    elif diceRoll=='q':
        exit()
    else:
        print('Hata!')