import requests
import json

data = requests.get("https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=BTC,USD,EUR").json()

print(data['BTC'])
