import requests
from requests.api import request

class Github:

    def __init__(self):
        self.api_url = 'https://api.github.com'
        self.token = '...'        #kendi tokenını koy 

    def getUser(self, username):
        response = requests.get(self.api_url+'/users/'+username)
        return response.json()          #api üzerinden kullanıcı bilgisi

    def getRepositories(self, username):
        response = requests.get(self.api_url+'/users/'+username+'/repos')
        return response.json()          #api üzerinden respository bilgisi

    def createRepositories(self, name):
        response = requests.post(self.api_url+'/user/repos', headers={
            "Authorization":f"token {self.token}"
        }, json = {
            "name": name,
            "description": "This is your first repository.",       #api üzerinden respository yaratma
            "homepage": "https://github.com",
            "private": False,
        })

        return response.json()

github = Github()

while True:
    secim = input("1- Find User\n2- Get Repositories\n3- Create Repositories\n4- Exit\nSeçiminiz: ")
    
    if secim == '4':
        break
    else:
        if secim  == '1':
            username = input("Username: ")
            result = github.getUser(username)
            print(f"Name: {result['name']} Public Repositories: {result['public_repos']} Followers: {result['followers']}") 
        elif secim == '2':
            username = input("Username: ")
            result = github.getRepositories(username)
            for repo in result:
                print(repo['name'])

        elif secim == '3':
            name = input("Repository Name: ")
            result = github.createRepositories(name)
            print(result)
        else:
            print("Hatalı seçim yaptınız.")