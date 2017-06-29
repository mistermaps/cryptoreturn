#!/usr/bin/env python3

#bitcoin & ethereum ticker
#designed for status bar, i.e., i3blocks

import urllib.request
import json

#Total money spent per currency
ethTotal = 1234
btcTotal = 1234
totalSpent = ethTotal + btcTotal

#Amount of currency within wallet
ethAmount = 3.928935303107
btcAmount = 0.483952074

#uncomment these lines to make the program interactive
sel = input('Update values? (Y)es/(N)o\n').lower()
if sel == 'yes' or sel == 'y':
	btcChange = int(input('BTC added:'))
	ethChange = int(input('ETH added:'))
	
elif sel == 'no' or sel == 'n':
	print('Loading...')

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

#uncomment these lines if you'd to run this in a terminal
print('Current Bitcoin Price: $%.2f' % btcPrice)
print('Current BTC holdings: %.7f' % btcAmount)
print('Current Value: $%.2f' % btcValue)
print('Current BTC ROI:')
print('Current Ether Price: %.2f' % ethPrice)




#print value for status bar
print('BTC:  %.2f' % btcValue + ' ETH: %.2f' % ethValue + ' ROI: %s' % sym + '%.2f' % abs(totalSpent - totalValue))
