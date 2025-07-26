# Normal Yazım
urun_fiyatlari = [50,70,80,150,98,10,0,65,9,0]
vergiler = []
for i in urun_fiyatlari:
    if i >0:
        vergiler.append(i*1.20)


#List-Comp

urun_fiyatlari = [50,70,80,150,98,10,0,65,9,0]
vergiler = [i*1.20 for i in urun_fiyatlari if i>0]
print(vergiler)

#List comp koşul

urun_fiyatlari = [50,70,80,150,98,10,0,65,9,0]
vergiler = [i*1.20 if i>0 else "değer 0 olduğu için hesaplanmadı" for i in urun_fiyatlari]
print(vergiler)