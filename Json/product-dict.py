dict_verisi = {
    "1" :{
        "title" : "Samsung",
        "price" : 4500
    },

    "2" :{
            "title" : "Iphone",
            "price" : 45000
        }
}

import json

# Json dict olarak ekliyoruz
# with open("product-dict.json","w") as file:
#     json.dump(dict_verisi, file)


# Okumak için
with open("product-dict.json") as f:
    products = json.load(f)

print(products["2"])  # Normal dict gibi kullanabiliriz (id key olmuş oluyor)


# Başka bir veri eklemek için
products.update(
    {
        "3" :{
            "title" : "Xiamoi",
            "price" : 7000
        }
    }
) # Eğer veri yoksa ekler

with open("product-dict.json","w") as file:
    json.dump(products, file)

# Veri varsa günceller
products.update(
    {
        "3" :{
            "title" : "Huawei",
            "price" : 5600
        }
    }
)

with open("product-dict.json","w") as file:
    json.dump(products, file)

# Silmek için
products.pop("3")

with open("product-dict.json","w") as file:
    json.dump(products, file)