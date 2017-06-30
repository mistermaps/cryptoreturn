#!/usr/bin/env python3

#bitcoin & ethereum ticker
#designed for status bar, i.e., i3blocks
#author: maps

import urllib.request
import json
import csv
import sys

#function that reads from file an populates array with contents
def parse():
	global values
	csv.register_dialect('crypto', delimiter=',')
	with open('values.csv', 'r+') as f:
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

def getPrices():
	#currently uses kraken
	#easily modified to have other exchanges, or other currencies
	global btcPrice
	global ethPrice
	with urllib.request.urlopen("https://api.kraken.com/0/public/Ticker?pair=XBTUSD") as url:
		data = json.loads(url.read().decode())
		btcPrice = data['result']['XXBTZUSD']['l'][0]
		btcPrice = float(btcPrice)
	with urllib.request.urlopen("https://api.kraken.com/0/public/Ticker?pair=ETHUSD") as url:
		data = json.loads(url.read().decode())
		ethPrice = data['result']['XETHZUSD']['l'][0]
		ethPrice = float(ethPrice)

def read():
	#This is super ugly and hacked together because I couldn't get regex to work
	global ethAmount
	global btcAmount
	global ethTotal
	global btcTotal
	parse()
	#pls no bulli
	btcAmount = float(values[1].replace("'","").replace('"','').strip())
	btcTotal = float(values[3].replace("'","").replace('"','').strip())
	ethAmount = float(values[5].replace("'","").replace('"','').strip())
	ethTotal = float(values[7].replace("'","").replace('"','').strip())

def roi():
	btcValue = btcAmount * btcPrice
	ethValue = ethAmount * ethPrice
	totalValue = btcValue + ethValue
	totalSpent = ethTotal + btcTotal
	change = eval(totalValue, totalSpent)
	#print value for status bar
	print('BTC:  %.2f' % btcValue + ' ETH: %.2f' % ethValue + ' ROI: %s' % change + '%.2f' % abs(totalSpent - totalValue))

def main():
	read()
	parse()
	getPrices()
	roi()

main()