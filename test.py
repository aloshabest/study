import requests, csv
from bs4 import BeautifulSoup


response = requests.get('http://quotes.toscrape.com/')
html_data = BeautifulSoup(response.text)
quotes = html_data.find_all(class_='quote')

for quote in quotes:
    print(quote.find(class_='text').get_text())
    print(quote.find(class_='author').get_text())
    print(quote.find(class_='keywords')['content'])

with open("bs4.csv", "w") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['Text', 'Aithor', 'Keywords'])
    for quote in quotes:
        text = quote.find(class_='text').get_text()
        author = quote.find(class_='author').get_text()
        keywords = quote.find(class_='keywords')['content']
        csv_writer.writerow([text, author, keywords])