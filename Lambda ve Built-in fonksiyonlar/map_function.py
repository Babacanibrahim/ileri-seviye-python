sayilar = [1,2,3,4,5]
sayilar_str = ["1","2","3","4","5"]
kullanicilar = [
    {"ad" : "ali", "soyad" : "yılmaz"},
    {"ad" : "ibrahim", "soyad" : "babacan"}
]
isimler = ["ibo","melisa","ahmet"]

sonuc = list(map(lambda sayi : sayi*sayi, sayilar))
sonuc2 = list(map(int, sayilar_str))
sonuc3 = list(map(lambda kullanici : kullanici["soyad"].upper(),kullanicilar))
sonuc4 = list(map(str.capitalize, isimler))

print(sonuc4)
