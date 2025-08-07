import csv

with open("urunler.csv") as file:
    csv_reader = csv.DictReader(file)
    #print(list(csv_reader))

    for i in csv_reader:
        if i["is_active"] == "True":
            print(f"Ürün adı : {i["name"]} ürün fiyatı : {i["price"]}")

"""
Eğer virgül yerine başka bir ayraçla gelirse 
csv_reader = csv.DictReader(file) bu satırda 
csv_reader = csv.DictReader(file, delimiter = "|") gibi ayırabiliriz
"""
