import requests

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

data = response.json()
earth_lst = data['features']
for i in range(len(earth_lst)):
        print(f"{i}. Place: {earth_lst[i]['properties']['place']}, Magnitude: {earth_lst[i]['properties']['mag']}.")