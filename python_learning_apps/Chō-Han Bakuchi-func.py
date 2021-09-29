import random

odd=False
even=False       #This is global variables i use in func
money=0             #this is starting money
betMoney=0         #this is betmoney
choiceBet=0         #odd or even   empty one

#rolling dice and calculate odd or even func
def dice():
    global odd
    global even
    d1=random.randint(1,6)
    d2=random.randint(1,6)
    dices=d1+d2
    if dices%2==0:
        even=True 
        odd=False    #this will use calculating the bet is win or lose
        print(f"Çift! Zarların toplamı: {dices}")
        
    else:
        odd=True
        even=False
        print(f"Tek! Zarların toplamı: {dices}")
        
#deposit money func
def deposit():
    global money
    while True:
        money=int(input('Oyuna girmek istediğiniz miktar para yatırın. (100$ - 50000$)'))
        if 100<=money<=50000:    #money limit
            print('Keyifli oyunlar.')
            break
        else:
            print('Lütfen belirtilen aralıkta para yatırın.')

    

#bet func
def bet():
    global money
    global betMoney
    
    while True:
        betMoney=int(input('Bahis miktarınızı girin: ').strip())  
        if betMoney>money:
            print(f'Yetersiz bakiye. Bakiye: {money}$')
        else:
            print('Şans sizinle olsun.')
            break

     
 #odd or even choosing func
def choiceMove():
    global choiceBet
    while True:
        choiceBet=input('Tek mi Çift mi? (t/ç): ').strip().lower()
        if choiceBet=='t':
            break
        elif choiceBet=='ç':
            break
        else:
            print('Hatalı oynadınız. Tekrar seçin.')

#this is checking the bet. Is the bet win or lose?

def check():
    global odd
    global even
    global choiceBet
    global money
    global betMoney

    if choiceBet=='ç' and even==True:
        money+=betMoney
        print(f"Tebrikler kazandınız! Bakiyeniz: {money}$")
    elif choiceBet=='t' and odd==True:
        money+=betMoney
        print(f"Tebrikler kazandınız! Bakiyeniz: {money}$")
    else:
        money-=betMoney
        print(f"Hay aksi! Bakiyeniz: {money}$")

#play all in or go home func xd

def goNext():
    global money
    while True:
        next=input('Bir el daha oynamak istiyor musunuz? (e/h): ').strip().lower()
        if next=='e':
            if money==0:
                while True:
                    choice2=input("Yeterli miktarda para bulunmamaktadır. Tekrar yatırmak istiyor musunuz? (e/h): ")
                    if choice2=='e':
                        deposit()
                        break
                    elif choice2=='h':
                        print("İyi günler dileriz.")
                        exit()
                    else:
                        print("Hatalı tuşladınız. Tekrar deneyin.")
            else:
                break
            break
        elif next=='h':
            print(f"{money}$ para ile masadan ayrıldınız. İyi günler dileriz.")
            exit()
        else:
            print("Hatalı tuşladınız. Tekrar deneyin.")



#game

while True:
    if money==0:
        deposit()
    else:
        bet()
        choiceMove()
        dice()
        check()
        goNext()

