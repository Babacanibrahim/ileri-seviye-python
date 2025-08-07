"""
def selamlama(fn):
    def inner (ad):
        print("Hoşgeldiniz,")
        fn(ad)
        print("Güle güle !")
    return inner

@selamlama
def gunaydin(ad):
    print("Günaydın ", ad)

@selamlama
def tunaydın(ad):
    print("Tünaydın " ,ad)


gunaydin("İbrahim")
print("*****************")
tunaydın("Mehmet")
"""

# def double(fn):
#     def inner(*args, **kwargs):
#         fn(*args, **kwargs)
#         return fn(*args, **kwargs)
#     return inner

# @double
# def merhaba(isim):
#     print("Merhaba ", isim)

# @double
# def selamlama():
#     return "Selam"

# @double
# def gulegule():
#     print("Güle güle")


# gulegule()
# merhaba("İbrahim")
# print(selamlama())