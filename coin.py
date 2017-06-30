#!/usr/bin/env python3

#bitcoin & ethereum ROI calculator
#author: maps
#feel free to modify

import urllib.request
import json
import csv
import sys
#import re #more like reeeeee

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

#function for user to enter amount and cost of BTC, ETH
def enter():
	print('Warning! This will overwrite the file.')
	print('This option intended for first-time use of this program.')
	sel = input('Are you sure you want to continue? (Y)es/(N)o\n').lower()
	if sel == 'yes' or sel == 'y':
		#erases the file
		with open('values.csv', 'w'): pass
		f = open('values.csv','w')
		btcAmount = float(input('Please enter the exact amount of BTC held:\n'))
		if btcAmount > 0:
			f.write('BTC:' + str(btcAmount) + ',')
			btcTotal = float(input('Please enter the total amount spent on BTC:\n$'))
			f.write('BTC Cost:' + str(btcTotal) + ',')
		ethAmount = float(input('Please enter the exact amount of ETH held:\n'))
		if ethAmount > 0:
			f.write('ETH:' + str(ethAmount) + ',')
			ethTotal = float(input('Please enter the total amount spent on ETH:\n$'))
			f.write('ETH cost:' + str(ethTotal) + ',')
		print('Loading...')
	elif sel == 'no' or sel == 'n':
		print('Loading...')

#function for determining positive or negative ROI
def eval(a, b):
	global sym 
	if a > b:
		return '+'
	elif a < b:
		return '-'

#reads from file (badly) and awkwardly converts them to useful fields
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

#function for updating .csv file
def update():
	read()
	global ethAmount
	global btcAmount
	global ethTotal
	global btcTotal
	f = open('values.csv', 'r+')
	sel = input('(B)uy or (s)ell BTC?\n').lower()
	if sel == 'buy' or sel == 'b':
		addBtcAmount = float(input('How much BTC are you adding?\n'))
		if addBtcAmount > 0:
			btcAmount += addBtcAmount
			f.write('BTC:' + str(btcAmount) + ',')
			addBtcTotal = float(input('How much did you spend to add this amount?\n'))
			btcTotal += addBtcTotal
			f.write('BTC:' + str(btcTotal) + ',')
	if sel == 'sell' or 's':
		addBtcAmount = float(input('How much BTC did you sell?\n'))
		if addBtcAmount > 0:
			btcAmount -= addBtcAmount
			f.write('BTC:' + str(btcAmount) + ',')
			addBtcTotal = float(input('At what price did you sell?\n'))
			btcTotal -= addBtcTotal
			f.write('BTC:' + str(btcTotal) + ',')
	sel = input('(B)uy or (s)ell ETH?\n').lower()
	if sel == 'buy' or sel == 'b':
		addEthAmount = float(input('How much ETH are you adding?\n'))
		if addEthAmount > 0:
			ethAmount += addEthAmount
			f.write('ETH:' + str(ethAmount) + ',')
			addEthTotal = float(input('How much did you spend to add this amount?\n'))
			ethTotal += addEthTotal
			f.write('ETH:' + str(ethTotal) + ',')
	if sel == 'sell' or 's':
		addEthAmount = float(input('How much ETH did you sell?\n'))
		if addEthAmount > 0:
			ethAmount -= addEthAmount
			f.write('ETH:' + str(ethAmount) + ',')
			addEthTotal = float(input('At what price did you sell?\n'))
			ethTotal -= addEthTotal
			f.write('ETH:' + str(ethTotal) + ',')	
#function to get current price from API
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

#calculate and display ROI and inputted values
def roi():
	btcValue = btcAmount * btcPrice
	ethValue = ethAmount * ethPrice
	totalValue = btcValue + ethValue
	totalSpent = ethTotal + btcTotal
	print('\n\nCurrent Bitcoin Price: \n\t\t\t$%.2f' % btcPrice)
	print('Current BTC holdings: \n\t\t\t%.7f' % btcAmount)
	print('Total Bitcoin Spending: \n\t\t\t$%.2f' % btcTotal)
	print('Current Value: \n\t\t\t$%.2f' % btcValue)
	change = eval(btcValue, btcTotal)
	print('Current BTC ROI: \n\t\t\t%s' % str(change) + '$%.2f' % abs(btcTotal - btcValue))
	print()
	print('Current Ether Price: \n\t\t\t$%.2f' % ethPrice)
	print('Current ETH holdings: \n\t\t\t%.7f' % ethAmount)
	print('Total Ether Spending : \n\t\t\t$%.2f' % ethTotal)
	print('Current Value: \n\t\t\t$%.2f' % ethValue)
	change = eval(ethValue, ethTotal)
	print('Current ETH ROI: \n\t\t\t%s' % str(change) + '$%.2f' % abs(ethTotal - ethValue))
	print()
	print('Total Spent minus profit: \n\t\t\t$%.2f' % totalSpent)
	print('Current Combined Value: \n\t\t\t$%.2f' % totalValue)
	change = eval(totalValue, totalSpent)
	print('Current total ROI: \n\t\t\t%s' % str(change) + '$%.2f' % abs(totalSpent - totalValue))		

#begin user interactions
def main():
	print('Welcome to CryptoReturn, the Crypto ROI calculator.')
	print('CryptoReturn uses the values.csv file for its calculations.')
	print("Use 'Enter' to enter in these values upon first use.")
	print("Use 'Update' to add any additional investments, if you've already entered initial holdings in.")
	print("Select 'Check' to calculate ROI.")
	print('After any of these options, the program will calculate your ROI.\n')
	sel = input('Please select:\n\t(E)nter\n\t(U)pdate\n\t(C)heck\n').lower()
	if sel == 'check' or sel == 'c':
		print('Loading...')
	elif sel == 'update' or sel == 'u':
		update()
		print('Loading...')
	elif sel == 'enter' or sel == 'e':
		enter()
	read()
	parse()
	getPrices()
	roi()
	
main()