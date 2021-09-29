import requests
import json

from requests.models import Response 

class Archive:
    def __init__(self):
        self.api_url= "https://api.themoviedb.org"
        self.token = "..."


    def onTrend(self, page):
        response = requests.get(self.api_url+'/3/trending/movie/week?api_key='+self.token+"&page="+page)
        response = json.loads(response.text)
        for i in response["results"]:
            print(i["title"])

    def search(self, query, page):
        response = requests.get(self.api_url+"/3/search/movie?api_key="+self.token+"&query="+query+"&page="+page)
        response = json.loads(response.text)
        for i in response["results"]:
            print(i["title"])

    def topMovies(self, page):
        response = requests.get(self.api_url+"/3/movie/top_rated?api_key="+self.token+"&page="+page)
        response = json.loads(response.text)
        for i in response["results"]:
            print(i["title"])

    def nowPlaying(self, page):
        response = requests.get(self.api_url+"/3/movie/now_playing?api_key="+self.token+"&page="+page)
        response = json.loads(response.text)
        for i in response["results"]:
            print(i["title"])

    def upComming(self, page):
        response = requests.get(self.api_url+"/3/movie/upcoming?api_key="+self.token+"&page="+page)
        response = json.loads(response.text)
        for i in response["results"]:
            print(i["title"])

def goNext():
    while True:
        choose2=input("Başka işlem yapmak istiyor musunuz? (e/h): ")
        if choose2 == 'e':
            break
        elif choose2 == 'h':
            print("İyi günler.")
            exit()
        else:
            print("Hatalı tuşladınız. Lütfen tekrar deneyin.")


archive = Archive()

while True:
    print("Hoş Geldiniz".center(70,'*'))
    choose = input("1- Popüler Filmler\n2- En İyi Filmler\n3- Vizyondaki Filmler\n4- Vizyona Girecek Filmler\n5- Film Ara\n6- Çıkış\nYapmak istediğiniz işlem: ")
    if choose == '6':
        print("İyi Günler.")
        break
    else:
        if choose == '1':
            page = input("Kaçıncı sayfaya bakmak istiyorsunuz?: ")
            archive.onTrend(page)
            goNext()

        elif choose == '2':
            page = input("Kaçıncı sayfaya bakmak istiyorsunuz?: ")
            archive.topMovies(page)
            goNext()

        elif choose == '3':
            page = input("Kaçıncı sayfaya bakmak istiyorsunuz?: ")
            archive.nowPlaying(page)
            goNext()

        elif choose == '4':
            page = input("Kaçıncı sayfaya bakmak istiyorsunuz?: ")
            archive.upComming(page)
            goNext()       

        elif choose == '5':
            query = input("Aramak istediğiniz anahtar kelimeyi yazın: ")    
            page = input("Kaçıncı sayfaya bakmak istiyorsunuz?: ")  
            archive.search(query, page) 
            goNext()        

        else:
            print('Hatalı tuşladınız. Lütfen tekrar deneyin.')
