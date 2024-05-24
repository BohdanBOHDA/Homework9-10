# Завдання 1

from bs4 import BeautifulSoup
import requests

url = "http://books.toscrape.com"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

print("Всі назви книг:")
quotes = soup.find_all("h3")
for quote in quotes:
    print(quote.text)

# Завдання 2
print("Всі ціни:")

quotes_1 = soup.find_all("p", {"class": "price_color"})
for quote_1 in quotes_1:
    print(quote_1.text)


