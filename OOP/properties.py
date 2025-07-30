class Product():

    def __init__(self, name, price):
        self.name = name

        if price >=0:
            self._price = price
        else:
            raise ValueError("Negatif bir fiyat girilemez.")
        
    def __str__(self):
        return f"{self.name} - {self._price} TL"
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value >=0:
            self._price = value
        else:
            raise ValueError("Negatif bir fiyat girilemez.")

pr1 = Product("Bilgisayar",45)
print (pr1)
pr1.price = -98
print(pr1)