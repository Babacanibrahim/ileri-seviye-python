# Alıştırma 1
sayilar = [7,9,85,2,0,5,9,2,1,621,9,51,132]

print(sorted(sayilar, reverse=True))

# Alıştırma 2
notlar = [
    {"ad" : "web", "not":50},
    {"ad" : "algoritmalar", "not":80},
    {"ad" : "bilimsel hesaplama", "not":75}
]

sonuc = sorted(notlar, key=lambda x : x["not"],reverse=True)
sonuc = list (map(lambda x : x["ad"],sonuc))
print(sonuc)