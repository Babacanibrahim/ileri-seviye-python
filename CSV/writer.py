import csv

# CSV DOSYASINA YAZMAK İÇİN (ama eski veriler silinip tekrar yazar)


# with open("arabalar.csv","w",newline="") as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerows([["Marka","Model"],["Renault","Clio"],["Yamaha ","R1"]])





# Eski verilerin üzerine yazar

# with open("arabalar.csv","a",newline="") as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerow(["Mondail","Drift L"])





# Bir dosyadan okuyup başka dosyaya yazdırma

# with open ("urunler.csv") as file:
#     csv_reader = csv.reader(file)
#     with open ("yeni-urunler.csv","w",newline="") as f:
#         csv_writer = csv.writer(f)
#         for urun in csv_reader:
#             csv_writer.writerow([i.upper() for i in urun])




# Aynı dosya üzerinde yazma (mesela fiyatlara zam geldi)

with open("yeni-urunler.csv","r+") as file:
    csv_reader = csv.reader(file)
    csv_writer = csv.writer(file)

    next(csv_reader)

    file.seek(0)

    csv_writer.writerow(["ID","NAME","PRICE","IS_ACTIVE","QUANTITY"])