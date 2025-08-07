# 1 -  Online sipariş veren kişi sayısı
# 2 -  Öğrencileri listele
# 3 -  20-30 yaş aralığındaki kişilerin konum listeleri


import csv

# 1
with open ("onlinefoods.csv") as file:
    csv_reader = csv.reader(file)
    print(len(list(csv_reader))-1)  # İlk satır başlıklar olduğu için - 1


# 2 
with open ("onlinefoods.csv") as file:
    csv_reader = csv.DictReader(file)
    ogrenciler = [user for user in csv_reader if user["Occupation"] == "Student"]
    print(len(ogrenciler))


# 3
with open ("onlinefoods.csv") as file:
    csv_reader = csv.DictReader(file)
    yirmi_otuz_arasi = [user for user in csv_reader if int(user["Age"])>20 and int(user["Age"])<30]
    print(len(yirmi_otuz_arasi))
    for i in yirmi_otuz_arasi:
        print(i["latitude"], i["longitude"])



# 4 ek olarak hem öğrenci hem 20-30 yaş
with open ("onlinefoods.csv") as file:
    csv_reader = csv.DictReader(file)
    yirmi_otuz_arasi_ogrenciler = [user for user in csv_reader if int(user["Age"])>20 and int(user["Age"])<30 and user["Occupation"] == "Student"]
    print(len(yirmi_otuz_arasi_ogrenciler))