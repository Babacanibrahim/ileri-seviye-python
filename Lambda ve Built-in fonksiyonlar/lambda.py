kareAl=lambda a: a*a

kupAl=lambda a:a**3

toplama = lambda a,b,c: a+b+c

def ikiSayiCarpim(n):
    return lambda a: a*n

carpma2 = ikiSayiCarpim(2)
carpma3 = ikiSayiCarpim(3)
carpma5 = ikiSayiCarpim(5)
carpma10 = ikiSayiCarpim(10)

print(carpma2(5))
print(carpma3(5))
print(carpma5(5))
print(carpma10(5))