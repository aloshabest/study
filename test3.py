import json

with open("manager_sales.json", "r") as file:
    data = json.load(file)

print(data)

spisok = []
for d in data:
    spisok.append(d['manager']['first_name'])
    spisok.append(d['manager']['last_name'])

    # for j in d:
    #     if j == 'cars':
    #         for v in j:



print(spisok)
