import requests
import sqlite3

url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'

response = requests.get(url, headers={'Accept': 'application/json'}, params={
        'format': 'geojson',
        'starttime': '2019-01-01',
        'endtime': '2019-05-01',
        'latitude': '51.51',
        'longitude': '-0.12',
        'maxradiuskm': '2000',
        'minmagnitude': '4'
    })


def sql_earthquakes(lst):
        conn = sqlite3.connect("earthquakes.db")
        c = conn.cursor()
        c.execute("CREATE TABLE earthquakes (place TEXT, magnitude TEXT);")
        c.executemany("INSERT INTO earthquakes VALUES (?, ?)", lst)
        conn.commit()
        conn.close()

def print_sql_earthquakes():
        conn = sqlite3.connect("earthquakes.db")
        c = conn.cursor()
        c.execute("SELECT * FROM earthquakes;")
        for row in c:
                print(row)
        conn.commit()
        conn.close()


data = response.json()
earth_lst = data['features']
lst = []
for i in range(len(earth_lst)):
        place = earth_lst[i]['properties']['place']
        mag = earth_lst[i]['properties']['mag']
        lst.append((place, mag))
        print(f"{i}. Place: {place}, Magnitude: {mag}.")

sql_earthquakes(lst)
print()
print_sql_earthquakes()