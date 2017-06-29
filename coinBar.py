#!/usr/bin/env python3
#bitcoin & ethereum ticker
#designed for status bar, i.e., i3blocks
#author: maps

import urllib.request
import json

#Total money spent per currency
ethTotal = 1234
btcTotal = 1234
totalSpent = ethTotal + btcTotal

#Amount of currency within wallet
ethAmount = 3.928935303107
btcAmount = 0.483952074

#currently uses kraken
#easily modified to have other exchanges, or other currencies
with urllib.request.urlopen("https://api.kraken.com/0/public/Ticker?pair=XBTUSD") as url:
	data = json.loads(url.read().decode())
	btcPrice = data['result']['XXBTZUSD']['l'][0]
	btcPrice = float(btcPrice)
with urllib.request.urlopen("https://api.kraken.com/0/public/Ticker?pair=ETHUSD") as url:
	data = json.loads(url.read().decode())
	ethPrice = data['result']['XETHZUSD']['l'][0]
	ethPrice = float(ethPrice)
#find current value of coin
btcValue = btcAmount * btcPrice
ethValue = ethAmount * ethPrice
totalValue = btcValue + ethValue
sym = ['+','-']
if totalValue > totalSpent:
	sym = sym[0]
elif totalValue < totalSpent:
	sym = sym[1]

#print value for status bar
print('BTC:  %.2f' % btcValue + ' ETH: %.2f' % ethValue + ' ROI: %s' % sym + '%.2f' % abs(totalSpent - totalValue))
