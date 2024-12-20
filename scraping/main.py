import requests
from bs4 import BeautifulSoup

url = "./index.hmtl"
page = requests.get("index.hmtl")
soup = BeautifulSoup(page.content, 'html.parser')

titles = soup.title.string
print(f"title : {titles}")


text = soup.find_all("h1", class_="gem-c-title__text")
print(f"text: {text}")

names_price_list = [soup.find_all("ul", class_="")]
