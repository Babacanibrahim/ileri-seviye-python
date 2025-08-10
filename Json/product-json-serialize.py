# DİCT VERİYİ JSON ÇEVİRME
import json

dict_verisi = {
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
}

with open("product2.json","w" , encoding="utf-8") as file:
    json.dump(dict_verisi, file, ensure_ascii=False)