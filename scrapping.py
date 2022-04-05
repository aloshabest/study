import requests, csv
from bs4 import BeautifulSoup


def scrap():
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



def add_student(name, last_name, age):
    with open("students.csv", "a") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([name, last_name, age])

# add_student('Jane', 'White', '25')
# add_student('Lil', 'Wane', '28')
# add_student('Mary', 'Brown', '20')



def print_students():
    with open("students.csv") as file:
        csv_reared = csv.reader(file)
        for student in csv_reared:
            if student != []:
                print(*student)

print_students()