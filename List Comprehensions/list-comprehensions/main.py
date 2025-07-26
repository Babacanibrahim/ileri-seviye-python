# Normal Yazım
sayilar = []

for i in range(5):
    sayilar.append(i)

print (sayilar)

#List comp
sayilar2 = [i*3 for i in sayilar]

print(sayilar2)

kurum = "btk akademi"

sonuc = [i.upper() for i in kurum]

print(sonuc)