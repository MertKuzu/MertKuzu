
import requests
from bs4 import BeautifulSoup

#i take information what i need from html with web scraping without api

url = "https://www.n11.com/bilgisayar/masaustu-bilgisayar"

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")
list = soup.find_all("li",{"class":"column"})

for li in list:
    try:
        name = li.find_all("a")[1].h3.text            
        oldPrice = li.find_all("a")[1].find("del").text
        newPrice = li.find_all("a")[1].find("ins").text
        print(f"Ürün İsmi: {name}  Eski Fiyatı: {oldPrice}  Yeni Fiyatı: {newPrice}")
    except AttributeError as error:
        pass
        

    


