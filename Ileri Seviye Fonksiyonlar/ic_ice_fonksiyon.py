"""
 def usAlma(taban):
     def inner(us):
         return taban**us
     return inner

print(usAlma(2)(3))
taban = usAlma(3)
sonuc = taban(2)
print(sonuc)
"""

"""

def yetki_sorgulama(sayfa):
    def inner(role):
        if role =="Admin":
            return f"{role} kişisi {sayfa} sayfasına erişebilir."
        
        return f"{role} kişisi {sayfa} sayfasına erişemez."
    return inner

# print(yetki_sorgulama("Ürün Güncelleme")("Admin"))
# print(yetki_sorgulama("Ürün Güncelleme")("User"))
"""

def islem(islem_adi):
    def carpma(*args):
        carpim = 1
        for i in args:
            carpim *= i        
        return carpim

    def toplama(*args):
        toplam = 0
        for i in args:
            toplam += i            
        return toplam
        
    if islem_adi == "Toplama":
        return toplama
    
    elif islem_adi == "Çarpma":
        return carpma
    
sayilar_toplama = islem("Toplama")
print(sayilar_toplama(10,20,30))

sayilar_carpma = islem("Çarpma")
print(sayilar_carpma(10,20,30))
