#!/usr/bin/env python3
import json
import urllib.request

def btc():
	with urllib.request.urlopen("https://api.kraken.com/0/public/Ticker?pair=XBTUSD") as url:
		data = json.loads(url.read().decode())
		btcPrice = data['result']['XXBTZUSD']['b'][0]
		btcPrice = float(btcPrice)
	return btcPrice

btcPrice = btc()
print('%.2f' % btcPrice)
