# JSON VERİYİ DİCT ÇEVİRMEK İÇİN

import json

# Eğer bir dosyadan okuyorsak load kullanıyoruz.
with open("product.json") as file:
    data = json.load(file)

# print(data)
# print(type(data))
print(data["title"])


# Eğer dosyadan okumuyorsak örneğin;

json_verisi = """{
    "id": 2,
    "title": "İphone 16",
    "price": 50000,
    "category": "Telefon",
    "rating": "4.2",
    "colors": [
        "Red",
        "Blue",
        "Black"
    ]
}"""

data2 = json.loads(json_verisi)


# print(data2)
# print(type(data2))
print(data2["price"])