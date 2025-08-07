def dec_selamlama(count):
    def selamlama(fn):
        def inner(ad):
            for i in range(count):
                print("Hoşgeldiniz")
                fn(ad)
                print("Güle güle")
        return inner
    return selamlama

@dec_selamlama(3)
def gunaydın(ad):
    print("Günaydın", ad )

@dec_selamlama(2)
def tunaydin(ad):
    print("Tünaydın", ad)


tunaydin("Mehmet")