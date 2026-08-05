import requests
import json
bozulandoviz = input("Bozulacak Döviz Kodunu Giriniz : ")
amount = int(input(f"Kaç adet {bozulandoviz} bozacaksınız"))
alinandoviz = input("Alınacak Döviz Kodunu Giriniz : ")

api = "a0b49a807a37344316e99206"
url = f"https://v6.exchangerate-api.com/v6/{api}/latest/{bozulandoviz}"
website = requests.get(url)
websitedict = json.loads(website.text)
odenecek = websitedict["conversion_rates"][alinandoviz]*amount


print(f"{amount} {bozulandoviz} {odenecek} {alinandoviz} ediyor.")
