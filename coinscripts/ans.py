#!/usr/bin/env python3
import urllib.request
import json
def ans():
	with urllib.request.urlopen("https://api.coinmarketcap.com/v1/ticker/neo/") as url:
		data = json.loads(url.read().decode())
		data = str(data).split()
		ansPrice = float(str(data[9]).replace("'","").replace(',',''))
	return ansPrice

ansPrice = ans()
print("%.2f" % ansPrice)
