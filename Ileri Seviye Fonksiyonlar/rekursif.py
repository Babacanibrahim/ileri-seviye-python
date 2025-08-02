def faktoriyel(sayi):

    if not isinstance(sayi, int):
        raise TypeError("Değer bir sayı olmalı")
    
    if not sayi >=0:
        raise ValueError("Negatif sayı kabul edilemez")

    def inner_faktoriyel(sayi):
        if sayi <= 1:
            return 1
        else:
            return sayi * inner_faktoriyel(sayi-1)
    
    return inner_faktoriyel(sayi)

try:
    print(faktoriyel("A"))
except Exception as e:
    print(e)