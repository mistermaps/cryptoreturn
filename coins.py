#!/usr/bin/env python 3
import urllib.request
import json

class Coins():
	def gnt(self):
		with urllib.request.urlopen("https://api.coinmarketcap.com/v1/ticker/golem-network-tokens/") as url:
			data = json.loads(url.read().decode())
			data = str(data).split()
			gntPrice = float(str(data[9][1:-2:]))
		return gntPrice

	def btc(self):
		with urllib.request.urlopen("https://api.kraken.com/0/public/Ticker?pair=XBTUSD") as url:
			data = json.loads(url.read().decode())
			btcPrice = data['result']['XXBTZUSD']['b'][0]
			btcPrice = float(btcPrice)
		return btcPrice
	def eth(self):
		with urllib.request.urlopen("https://api.kraken.com/0/public/Ticker?pair=ETHUSD") as url:
			data = json.loads(url.read().decode())
			ethPrice = float(data['result']['XETHZUSD']['b'][0])

		return ethPrice

	def ans(self):
		with urllib.request.urlopen("https://api.coinmarketcap.com/v1/ticker/antshares/") as url:
			data = json.loads(url.read().decode())
			data = str(data).split()
			ansPrice = float(str(data[9][1:-2:]))
		return ansPrice
