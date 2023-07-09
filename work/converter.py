import requests
def converter_to_usd(value):
    usd = requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/")
    usd_rate = float(usd.json()[0]["Rate"])
    print(usd_rate)
    converted = float(value / usd_rate)
    return converted