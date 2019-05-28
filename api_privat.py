import requests

response = requests.get("https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11")
print("response.txt:", response.text)