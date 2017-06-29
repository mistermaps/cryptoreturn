#!/usr/bin/env python3

#bitcoin & ethereum ROI calculator

import urllib.request
import json

#Total money spent per currency
ethTotal = 1234.56
btcTotal = 9876.54

#Amount of currency within wallet
ethAmount = 3.84
btcAmount = 3.8464240649291983

#uncomment these lines to make the program interactive
sel = input('Update values? (Y)es/(N)o\n').lower()
if sel == 'yes' or sel == 'y':
	btcChange = float(input('BTC added: '))
	if btcChange > 0:
		btcTotal += float(input('Cost: $'))
	ethChange = float(input('ETH added: '))
	if ethChange > 0:
		ethTotal += float(input('Cost: $'))
	print('Loading...')
	btcAmount += btcChange
	ethAmount += ethChange

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
totalSpent = ethTotal + btcTotal


def eval(a, b):
	global sym 
	if a > b:
		return '+'
	elif a < b:
		return '-'
	#return sym
#if totalValue > totalSpent:
#	sym = sym[0]
#elif totalValue < totalSpent:
#	sym = sym[1]



#uncomment these lines if you'd to run this in a terminal
print('Current Bitcoin Price: \n\t\t\t$%.2f' % btcPrice)
print('Current BTC holdings: \n\t\t\t%.7f' % btcAmount)
print('Total Bitcoin Spending: \n\t\t\t$%.2f' % btcTotal)
print('Current Value: \n\t\t\t$%.2f' % btcValue)
change = eval(btcValue, btcTotal)
print('Current BTC ROI: \n\t\t\t%s' % str(change) + '$%.2f' % (btcTotal - btcValue))
print()
print('Current Ether Price: \n\t\t\t$%.2f' % ethPrice)
print('Current ETH holdings: \n\t\t\t%.7f' % ethAmount)
print('Total Ether Spending : \n\t\t\t$%.2f' % ethTotal)
print('Current Value: \n\t\t\t$%.2f' % ethValue)
change = eval(ethValue, ethTotal)
print('Current ETH ROI: \n\t\t\t%s' % str(change) + '$%.2f' % (ethTotal - ethValue))
print()

print('Total Spent: \n\t\t\t$%.2f' % totalSpent)
print('Current Value: \n\t\t\t$%.2f' % totalValue)
change = eval(totalValue, totalSpent)
print('Current total ROI: \n\t\t\t%s' % str(change) + '$%.2f' % abs(totalSpent - totalValue))
#print('BTC $:  %.2f' % btcValue + ' ETH $: %.2f' % ethValue + ' ROI: %s' % change + '%.2f' % abs(totalSpent - totalValue))
