from json.decoder import JSONDecodeError
import requests
import json

def foreign_exchange():
    try:   
        currency1 = input("Sahip olduğunuz paranın kodunu yazın: ")
        currency2 = input("Satın almak istediğiniz paranın kodunu yazın: ")
        money = int(input("Lütfen miktarı girin: "))
        wergi = 2/1000

        api_url = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/"

        result = requests.get(api_url+currency1+'.json')
        result = json.loads(result.text)

        print("{0} Tarihli Kur: {1}".format(result["date"], result[currency1][currency2]))
        print(f"Brüt Bakiyeniz: {money*result[currency1][currency2]}")
        print(f"Net Bakiyeniz: {money*result[currency1][currency2]-((money*result[currency1][currency2])*wergi)}")

    except JSONDecodeError as error:
        print("Hatalı para kodu girdiniz.", error)

    except ValueError as err:
        print("Lütfen miktarı girin bölümüne sayısal bir değer girin.", err)



def again():
    while True:
        a = input("Başka işlem yapmak istiyor musunuz? (e/h)")
        if a == 'e':
            break
        elif a == 'h':
            print("İyi günler dileriz.")
            exit()
        else:
            print("Hatalı tuşladınız. Tekrar deneyin.")


while True:
    foreign_exchange()
    again()