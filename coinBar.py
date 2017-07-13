#!/usr/bin/env python3

#bitcoin, ethereum, and other altcoin ticker
#designed for status bar, i.e., i3blocks
#part of CryptoReturn suite
#requires coins.py & values.csv
#author: maps

import urllib.request
import json
import csv
from coins import Coins
import os
#function that reads from file an populates array with contents
def parse():
	global values
	USER = os.path.expanduser('~')
	csv.register_dialect('crypto', delimiter=',')
	#this iteration is specifically formulated for i3blocks, with either:
	#both this file, coins.py, and a filled values.csv copied within the cryptoreturn directory
	#i.e., run the main program, then copy the files
	#with open(USER + '/.i3/values.csv', 'r+') as f:

	#or: this file, coins.py, and values.csv within the Cryptoreturn repo
	#with the i3blocks configuration file pointing to it
	#uncomment for this configuration
	with open(USER + '/cryptoreturn/values.csv','r+') as f:
		reader = csv.reader(f, dialect='crypto')
		values = []
		for row in reader:
			values = str(row).split(":")
			values = str(values).split(',')

#function for determining positive or negative ROI
def eval(a, b):
	global sym
	if a > b:
		return '+'
	elif a < b:
		return '-'
	if not a: return ''
def getPrices():
	#requires coins.py
	#uses Kraken for BTC & ETH
	#uses CoinMarketCap for NEO/ANS and GNT
	#easily modified to have other exchanges, or other currencies
	coins = Coins()
	global btcPrice
	global ethPrice
	global gntPrice
	global ansPrice
	btcPrice = coins.btc()
	ethPrice = coins.eth()
	gntPrice = coins.gnt()
	ansPrice = coins.ans()
def read():
	parse()
	read.btcAmount = float(values[1][2:-1:])
	read.btcTotal = float(values[3][2:-1:])
	read.ethAmount = float(values[5][2:-1:])
	read.ethTotal = float(values[7][2:-1:])
	read.gntAmount = float(values[9][2:-1:])
	read.gntTotal = float(values[11][2:-1:])
	read.ansAmount = float(values[13][2:-1:])
	read.ansTotal = float(values[15][2:-1:])	

def roi():
	btcAmount = read.btcAmount
	btcTotal = read.btcTotal
	ethAmount = read.ethAmount
	ethTotal = read.ethTotal
	gntAmount = read.gntAmount
	gntTotal = read.gntTotal
	ansAmount = read.ansAmount
	ansTotal = read.ansTotal

	btcValue = btcAmount * btcPrice
	ethValue = ethAmount * ethPrice
	gntValue = gntAmount * gntPrice
	ansValue = ansAmount * ansPrice
	totalValue = btcValue + ethValue + gntValue + ansValue
	totalSpent = ethTotal + btcTotal + gntTotal + ansTotal
	
	btcROI = eval(btcValue, btcTotal)
	ethROI = eval(ethValue, ethTotal)
	gntROI = eval(gntValue, gntTotal)
	ansROI = eval(ansValue, ansTotal)
	totalROI = eval(totalValue, totalSpent)
	
	#print value for status bar
	#there are several formats; see README for examples
	#uncomment (delete #) desired format

	#displays amount of coins held as well as current value & total ROI
	#print('BTC: ' + '%.4f' % btcAmount + ' @ $' + '%.2f' % btcValue + '|ETH: '   + '%.4f' % ethAmount + ' @ $' + '%.2f' % ethValue + '|GNT: '  + '%.4f' % gntAmount + ' @ $' + '%.2f' % gntValue + '|ANS: '  + '%.4f' % ansAmount + ' @ $' + ' %.2f' % ansValue + '||ROI:  %s' % totalROI + '%.2f' % abs(totalSpent - totalValue))
	
	#displays just current value & total ROI
	#print('BTC: ' + '%.2f' % btcValue + '|ETH: '   + '%.2f' % ethValue + '|GNT: '  + '%.2f' % gntValue  + '|ANS: '  + '%.2f' % ansValue + '||ROI:  %s' % totalROI + '%.2f' % abs(totalSpent - totalValue))
	
	#displays current value and coin-specific ROI & Total Roi
	#print('BTC: ' + '%.2f' % btcValue + '|ROI: %s' % btcROI + '%.2f' % abs(btcValue - btcTotal) +'||ETH: '   + '%.2f' % ethValue + '|ROI: %s' % ethROI + '%.2f' % abs(ethValue - ethTotal) + '||GNT: '  + '%.2f' % gntValue  + '|ROI: %s' % gntROI + '%.2f' % abs(gntValue - gntTotal) + '||ANS: '  + '%.2f' % ansValue + '|ROI: %s' % ansROI + '%.2f' % abs(ansValue - ansTotal) + '||Total ROI:  %s' % totalROI + '%.2f' % abs(totalSpent - totalValue))
	
	#displays just ROI per coin and total ROI
	print('BTC ROI: %s' % btcROI + '%.2f' % abs(btcValue - btcTotal) +'||ETH ROI: %s' % ethROI + '%.2f' % abs(ethValue - ethTotal) + '||GNT ROI: %s' % gntROI + '%.2f' % abs(gntValue - gntTotal) + '||ANS ROI: %s' % ansROI + '%.2f' % abs(ansValue - ansTotal) + '||Total ROI:  %s' % totalROI + '%.2f' % abs(totalSpent - totalValue))
	
	#displays just Total ROI
	#print('ROI:  %s' % totalROI + '%.2f' % abs(totalSpent - totalValue))
def main():
	read()
	parse()
	getPrices()
	roi()

main()
