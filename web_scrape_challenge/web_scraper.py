from bs4 import BeautifulSoup
import requests

url = "https://books.toscrape.com"
response = requests.get(url)

html = response.content
soup = BeautifulSoup(html, "html.parser")

books = soup.findAll("article")

for book in books:
    title = book.h3.a["title"]
    rate = book.p["class"][1]
    price = soup.find("p", class_="price_color").text
    print(f"the title is {title} \n rate: {rate} stars out of five \n price: {price}")
