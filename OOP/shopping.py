class CartItem:
    discount_rate = 0.1
    item_count = 0

    @classmethod
    def display_item_count(cls):
        return f"{cls.item_count} tane ürün oluşturuldu"
    
    @classmethod
    def create_item(cls, data_str):
        name, price , quantity = data_str.split(",")
        return cls(name, price , quantity)
    
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        CartItem.item_count +=1

    def calculate_total(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price =  self.price * (1-CartItem.discount_rate)
    
item1 = CartItem("Bilgisayar", 50000, 1)
item2 = CartItem("Telefon", 10000, 5)
item3 = CartItem("Kitap", 500, 10)


class ShoppingCart:
    coupon = 0

    def __init__(self, liste):
        self.liste = liste

    def add_item(self,item):
        self.liste.append(item)

    def display_items(self):
        for item in self.liste:
            print(item.name)
        
    def calculate_totals(self):
        total = 0
        for item in self.liste:
            total +=item.price * item.quantity
        return total

    def remove_item(self, item):
        self.liste.remove(item)

    def clear(self):
        self.liste.clear()

    def apply_coupon(self, code):
        self.code = code

        if code =="code1":
            return self.calculate_totals() * 0.9
        
        elif code =="code2":
            return self.calculate_totals() * 0.8
        
    
sc = ShoppingCart([item1,item2])
sc.display_items()
sc.add_item(item3)
sc.display_items()
print()
print(sc.calculate_totals())
sc.remove_item(item1)
sc.display_items()
print(sc.calculate_totals())
sc.clear()
print()
sc.display_items()
print(sc.calculate_totals())