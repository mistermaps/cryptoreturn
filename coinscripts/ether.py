#! /usr/bin/env python3

#simple script for displaying ether price
#author: maps

import urllib.request
import json
def eth():
	with urllib.request.urlopen("https://api.kraken.com/0/public/Ticker?pair=ETHUSD") as url:
		data = json.loads(url.read().decode())
		ethPrice = data['result']['XETHZUSD']['b'][0]
	return ethPrice

ethPrice = eth()
print('%.2f' % float(ethPrice))
