# Alıştırma 1

sayilar =[1,9,87,5,69,25,36,18,7,42,54]

cift_mi = all(sayi %2==0 for sayi in sayilar)
pozitif_mi = all(sayi >0 for sayi in sayilar)
print(cift_mi)
print(pozitif_mi)
print(any(sayi %2 ==0 for sayi in sayilar))


# Alıştırma 2

isimler = ["ayşe","ali","ibrahim","melisa"]

ilk_harf_a_mi = any((isim[0]=="a" for isim in isimler))

print(ilk_harf_a_mi)
