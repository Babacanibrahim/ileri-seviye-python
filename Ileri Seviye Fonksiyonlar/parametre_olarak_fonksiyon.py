def my_filter(fnc , liste):
    sonuc = []

    for i in liste:
        if fnc(i):
            sonuc.append(i)

    return sonuc

def is_even(sayi):
    return sayi % 2 == 0

def is_odd(sayi):
    return sayi % 2 == 1

def is_positive(sayi):
    return sayi >= 0

sayilar = [1,9,5,8,8,6,2,1,58,13,2,-9,-5,1,-9,8,7,0,98]

print(my_filter(is_even,sayilar))
print(my_filter(is_odd,sayilar))
print(my_filter(is_positive,sayilar))