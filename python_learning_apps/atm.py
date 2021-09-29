#account list (actualy dict)
accounts={
    'mertkuzu':{
        'accountPassword':'abc123',
        'accountNo':'123456789',
        'money':4000,
        'creditLimit':2000
    },
    'iremyaman':{
        'accountPassword':'yaman123',
        'accountNo':'987654321',
        'money':6000,
        'creditLimit':3000
    },
    'despot':{
        'accountPassword':'12345',
        'accountNo':'159357456',
        'money':3000,
        'creditLimit':1500
    }
}

#Functions: I used username global because when we're inputting while login username i use that username variable everywhere
#login func:
def loginAccount():
    loginAttempt=3
    while not loginAttempt==0:
        global username
        username=input('Hesap adı: ').strip().lower()
        loginAttempt-=1    
        if username in accounts:
            password=input('Parola: ')
            if username in accounts and accounts[username]['accountPassword']==password:
                print('Giriş işlemi başarılı.')
                global login
                login=True
                break      
            elif loginAttempt>0:                   
                print(f'Girdiğiniz parola hatalı {loginAttempt} hakkınız kaldı lütfen tekrar deneyin.')
            else:
                print('Çok sayıda deneme yaptınız lütfen daha sonra tekrar deneyin.')
        elif loginAttempt>0:                
            print(f'Girdiğiniz hesap adı hatalı {loginAttempt} hakkınız kaldı lütfen tekrar deneyin.')
        else:
            print('Çok sayıda deneme yaptınız lütfen daha sonra tekrar deneyin.')
        

#showing money fucn:
def showMoney():
    global username
    print(f"Paranız: {accounts[username]['money']} TL")
    print(f"Kredi Limitiniz: {accounts[username]['creditLimit']} TL")


#withdraw func:
def withdraw():
    global username
    withdrawMoney=int(input('Çekmek istediğiniz tutarı girin: '))
    if withdrawMoney<=accounts[username]['money']:
        a=accounts[username]['money']-withdrawMoney
        print('Para çekme işleminiz başarılı.')
        accounts[username]['money']=a
    else:
        wannaDebt=input('Yetersiz bakiye. Kredi imkanlarından faydalanmak ister misiniz? (e/h):')
        if wannaDebt=='e' and accounts[username]['money']+accounts[username]['creditLimit']>=withdrawMoney:
            result=(withdrawMoney-accounts[username]['money'])
            ruSure=input(f"{result} tutarında kredi çekilecek. İşleme devam etmek istiyor musunuz? (e/h): ")
            if ruSure=='e':
                print('Para çekme işleminiz başarılı.')
                takeDebt=(result*(1.5/100))
                print(f'Bir sonraki ay ödemeniz gereken miktar: {takeDebt+result} TL')
                result2=accounts[username]['creditLimit']-result
                accounts[username]['money']=0
                accounts[username]['creditLimit']=result2
            else:
                print('İşleminiz iptal edildi.')
        elif wannaDebt=='e' and accounts[username]['money']+accounts[username]['creditLimit']<withdrawMoney:
            print('Kredi limitiniz yetersiz.')
        else:
            print('İşleminiz iptal edildi.')
            
#deposit func:            
def deposit():
    global username
    depositMoney=int(input('Yatırmak istediğiniz tutarı girin: '))
    totalMoney=depositMoney+accounts[username]['money']
    accounts[username]['money']=totalMoney
    print('Yatırma işlemi başarılı.')

#countinue func

def next():
    while True:
        next=input('Başka işlem yapmak istiyor musunuz? (e/h)')
        if next=='e':
            break
        elif next=='h':
            print('İyi günler dileriz.')
            exit()   
        else:
            print('Hatalı tuşladınız. Tekrar deneyin.')  


#atm
login=False
print("Lütfen giriş yapın.")
loginAccount()
if login==True:
    while True:
        print('''
        Hoş geldiniz. Lütfen yapmak istediğiniz işlemi seçin.

        [1]Bakiye sorgula
        [2]Para çek
        [3]Para yatır
        [q]Çıkış yap

        ''')
        islem=input('Yapmak istediğiniz işlem: ')
        if islem=='1':
            showMoney()  
            next()                           
        elif islem=='2':
            withdraw()
            next()               
        elif islem=='3':
            deposit()
            next()           
        elif islem=='q':
            print('İyi günler dileriz.')
            exit()
        else:
            print('Yanlış tuşladınız. Tekrar deneyin.')




