import requests

key = "dd73aa1f09d446e7bc8114004251008"
url = "http://api.weatherapi.com/v1/current.json"

konum = input("Hava durumunu öğrenmek istediğiniz şehir :")
try:
    response = requests.get(url, params={
        "key" : key,
        "q" : konum,
        "lang" : "tr"
    })

    response = response.json()
    sehir = response["location"]["name"]
    derece = response["current"]["temp_c"]
    durum = response["current"]["condition"]["text"]

    print(f"{sehir} ilinde şu an hava {derece} °C. Ve hava {durum.lower()}.")

except Exception as e:
    print(e, " Yanlış bir şehir ismi kullandınız veya türkçe karakter kullandınız.")