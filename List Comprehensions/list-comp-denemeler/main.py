# 12ye bölünebilen sayılar
mod12 = [i for i in range(1,101) if i%12 ==0]

print(mod12)

#Rakam bulma
text = "Hello 12345 World"

rakamlar = [int(i) for i in text if i.isdigit()]

print(rakamlar)

#Sıcaklıklar
sicakliklar = [20,15,0,-5,-2]
tehlike = [i if i>=4 else "donma tehlikesi" for i in sicakliklar]

print(tehlike)

#Nota göre dict yazdırma
ogrenciler = ["ali","ahmet","canan"]
notlar = [50,60,80]

liste = [(ogrenciler[i], notlar[i]) for i in range(len(ogrenciler)) if notlar[i]>50]

dict = { key : value for (key,value) in liste}


# Normal yazılanı list - comp ile yaz
sonuc = []
for x in range(3):
    for y in range(3):
        sonuc.append((x,y))

#list-comp
sonuc2 = [(x,y) for x in range(3) for y in range(3)]
print(sonuc2)