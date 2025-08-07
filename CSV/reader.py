import csv

with open("urunler.csv") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    liste = list(csv_reader) 
    print(liste[0][1])

    for i in liste:
        print(i)
