#!/usr/bin/env python3

#Cryptocurrency ROI calculator
#v 2 7/24/17
#author: maps
#feel free to modify

import csv
import json
import os
import threading
import sys
import time
import urllib.request
from coins import Coins

done = False

#list of coin otions
coinOpt = ['Bitcoin','Ethereum','Litecoin','Golem',
'Antshares','Stratis','Ripple','Omisego',
'Syndicate']

#update this to be more conventional
Abbreviations = ['btc','eth','ltc','gnt','ans','strat','xrp','omg','synx']
coinSel = []
coinInvest = [False for i in range(len(coinOpt))]
USER = os.path.expanduser('~')
prompt = '>>\t'
stop = False

#create spinning animation
class spinner(threading.Thread):

    def run(self):
            print ('Calculating ROI:')
            i = 0
            while stop != True:
                    if (i%4) == 0:
                    	sys.stdout.write('\b/')
                    elif (i%4) == 1:
                    	sys.stdout.write('\b-')
                    elif (i%4) == 2:
                    	sys.stdout.write('\b\\')
                    elif (i%4) == 3:
                    	sys.stdout.write('\b|')

                    sys.stdout.flush()
                    time.sleep(0.1)
                    i+=1

#replacing entire coin functionality
def coin(name, abbv, invest):
	total = 0
	f = open(USER + '/cryptoreturn/values.csv','a')
	if invest == True:
		amount = float(input('Please enter the exact amount of ' 
			+ name + ' held:\n' + prompt))
		if amount > 0:
			f.write(str(abbv) + ':' + str(amount) + ',')
			total = float(input('Please enter the total amount spent on ' 
				+ abbv + ':\n$'))
			f.write(str(abbv) + ' cost:' + str(total) + ',')
		elif total == 0:
			f.write(str(abbv) + ':' + str(0) + ',')
			f.write(str(abbv) + ' cost:' + str(0) + ',')
	elif invest == False:
		f.write(str(abbv) + ':' + str(0) + ',')
		f.write(str(abbv) + ' cost:' + str(0) + ',')
		return name, abbv, invest

#function for determining the value of coins
def CoinValue(amount, price):
	coinValue = amount * price
	return coinValue

#function for keeping the screen clear
def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

#function for user to enter amount and cost of BTC, ETH, GNT, and ANS
def enter():
	print('Warning! This will overwrite the file.')
	print('This option intended for first-time use of this program.')
	sel = input('Are you sure you want to continue? (Y)es/(N)o\n').lower()
	if sel == 'yes' or sel == 'y':
		clear()
		#erases the file
		with open(USER + '/cryptoreturn/values.csv','w'): pass

		#list coins currently built into program	
		print("This program currently supports: ")
		for i in range(len(coinOpt)):
			print(str(i+1) + ")\t" + str(coinOpt[i]))

		print(
			"\nIf you have holdings in the listed coin, please enter '(Y)es' when prompted.\nHit any other key, otherwise.\n\n")

		for i in range(len(coinOpt)):
			#prompt user for coin investments
			coinSel.insert(i, input("Do you have holdings in " + coinOpt[i] + "?\n" + prompt).lower())
			if coinSel[i] == 'y' or coinSel[i] == 'yes':
				coinInvest[i] = True
		i = 0
		while i < len(coinOpt):
			coin(coinOpt[i],Abbreviations[i].upper(),coinInvest[i])
			i = i + 1
		clear()
	elif sel == 'no' or sel == 'n':
		clear()

#function to get current price from API
def getPrices():
	#requires coins.py file included with repo
	#currently uses CoinMarketCap
	#see coins.py
	coinDict = {
	'btcPrice':0,'ethPrice':0,'ltcPrice':0,'gntPrice':0,'ansPrice':0,'stratPrice':0,
	'xrpPrice':0,'omgPrice':0,'synxPrice':0}
	coins = Coins()
	coinPrice = []
	for i in range(len(coinOpt)):
		price = str(coins.getPrice(Abbreviations[i]))
		coinPrice.append(float(price))
	i = 0
	for k, v in coinDict.copy().items():
		if v is 0:
			coinDict[k] = coinPrice[i]
			i += 1		
	return coinPrice

#function to display user menu
def intro():
	print("	               _                 _                    ")
	print("  ___ _ __ _   _ _ __ | |_ ___  _ __ ___| |_ _   _ _ __ _ __  ")
	print(" / __| '__| | | | '_ \| __/ _ \| '__/ _ \ __| | | | '__| '_ \ ")
	print("| (__| |  | |_| | |_) | || (_) | | |  __/ |_| |_| | |  | | | |")
	print(" \___|_|   \__, | .__/ \__\___/|_|  \___|\__|\__,_|_|  |_| |_|")
	print("           |___/|_|  											")
	print('\t\t\t\t\tVersion 2.0')
	#time.sleep(1.5)
	print('\n Welcome to CryptoReturn, the cryptocurrency ROI calculator.')
	#time.sleep(.5)
	print('\t\t\t  By:')
	#time.sleep(.5)
	print('\t\t      ┏┳┓┏━┓┏━┓┏━┓\n'
		  '\t\t      ┃┃┃┣━┫┣━┛┗━┓\n'
		  '\t\t      ╹ ╹╹ ╹╹  ┗━┛')
	#time.sleep(1)	
	print('_______________________________________________________________\n')
	print("\tUse 'Enter' to enter in initial values.")
	print("\tUse 'Update' to add or subtract investments.")
	print("\tSelect 'Check' to calculate ROI.")
	print('\nAfter any of these options, the program will calculate your ROI.\n')
	#time.sleep(1)
	print('Please select:')
	time.sleep(.1)
	print('\t(E)nter')
	time.sleep(.1)
	print('\t(U)pdate')
	time.sleep(.1)
	print('\t(C)heck')
	sel = input(prompt)
	return sel

#function to display loading animation 
def load(func):
	s = spinner()
	s.start()
	try:
		func()
		stop = True
	except KeyboardInterrupt or EOFError:
         stop = True

#function that reads from file an populates array with contents
def parse():
	global values
	csv.register_dialect('crypto', delimiter=',')
	#regular config is for Linux, uncomment below for windows; if the program breaks, update the path to reflect where the repo is

	#for windows (untested)
	#with open(USER + '\cryptoreturn\\values.csv')

	#for all Linux distros, assuming the repo is in your home directory
	with open(USER + '/cryptoreturn/values.csv','r+') as f:
		reader = csv.reader(f, dialect='crypto')
		values = []
		for row in reader:
			values = str(row).split(":")
			values = str(values).split(',')

#function that reads from values.csv to populate lists			
def read():
	parse()
	amountDict = {
	'btcAmount':0,'ethAmount':0,'ltcAmount':0,'gntAmount':0,'ansAmount':0,'stratAmount':0,
	'xrpAmount':0,'omgAmount':0,'synxAmount':0}
	totalDict = {
	'btcTotal':0,'ethTotal':0,'ltcTotal':0,'gntTotal':0,'ansTotal':0,'stratTotal':0,
	'xrpTotal':0,'omgTotal':0,'snyxTotal':0}
	coinAmount = []
	coinTotal = []
	amount = []
	total = []

	i = 0
	j = 0
	
	for value in values:
		amount = value[2:-1:]
		try:			
			coinAmount.append(float(amount))
		except ValueError:
			continue
		
	for k, v in amountDict.copy().items():
		if v is 0:
			amountDict[k] = coinAmount[j]
			j += 2
		
	k = 0
	j = 1
	for value in values:	
		total = value[2:-1:]
		try:			
			coinTotal.append(float(total))
		except ValueError:
			continue

	for k, v in totalDict.copy().items():
		if v is 0:
			totalDict[k] = coinTotal[j]
			j += 2
		

	return amountDict, totalDict

#function for determining positive or negative ROI
def returns(a, b):
	global sym
	if a > b:
		return '+'
	elif a < b:
		return '-'
	if not a:
		return ''

#function that determines the ROI after all other functions have been completed
def roi():
	coinPrice = getPrices()
	amountDict, totalDict = read()

	coinAmount = []
	coinTotal = []
	for value in amountDict.values():
		coinAmount.append(value)
	for value in totalDict.values():
		coinTotal.append(value)
	
	#get total value, total spent
	totalValue = 0
	totalSpent = 0
	#iterate through 
	for i in range(len(coinAmount)): totalValue += float(coinAmount[i]) * coinPrice[i]
	for i in range(len(coinTotal)): totalSpent += float(coinTotal[i])
	
	
	totalList = []
	for i in range(len(coinOpt)):
		totalList.append(coinAmount[i])
	l = 0
	for item in totalList:
		if item != 0.00:
			coinInvest[l] = True
		l += 1
	i = 0
	#clear()
	done = True

	while i < len(coinOpt):
		coinValue = CoinValue(coinAmount[i], coinPrice[i])
		if coinAmount[i] > 0:
			print('Current ' + coinOpt[i] + ' Price: \n\t\t\t$%.2f' % coinPrice[i])
			print('Current ' 
				+ str(Abbreviations[i]).upper() + ' holdings: \n\t\t\t%.2f' 
				% coinAmount[i])
			print('Total ' + coinOpt[i] + ' Spending: \n\t\t\t$%.2f' % coinTotal[i])
			print('Current Value: \n\t\t\t$%.2f' % coinValue)
			change = returns(coinValue, coinTotal[i])
			print('Current ' 
				+ str(Abbreviations[i]).upper() + ' ROI: \n\t\t\t%s' % str(change) 
				+ '$%.2f' % abs(coinTotal[i] - coinValue))
			print()
		elif coinAmount[i] == 0.00:
			print('\b')
			#uncomment this line if you'd like to remind yourself to invest
			#print("No " + coinOpt[i] + " holdings to display.\n")

		i += 1
		
	print('Total Spent: \n\t\t\t$%.2f' % totalSpent)
	print('Current Combined Value: \n\t\t\t$%.2f' % totalValue)
	change = returns(totalValue, totalSpent)
	print('Current total ROI: \n\t\t\t%s' % str(change) + '$%.2f' % abs(totalSpent - totalValue))


#function for updating .csv file
def update():
	clear()
	total = 0
	#reads from file and populates values
	parse()
	

	f = open(USER + '/cryptoreturn/values.csv','r+')
	#sets dictionary values from read
	amountDict, totalDict = read()

	coinAmount = []
	coinTotal = []
	newAmount = []
	newTotal = []

	
	for value in amountDict.values():
		coinAmount.append(value)
	for value in totalDict.values():
		coinTotal.append(value)

	name = coinOpt
	abbv = Abbreviations
	amount = coinAmount

	for i in range(len(coinOpt)):
		#prompt user for coin investments
		coinSel.insert(i, input("Update " + name[i] + "?\n" + prompt).lower())
		if coinSel[i] == 'y' or coinSel[i] == 'yes':
			coinInvest[i] = True
		

		if coinInvest[i] == True:
			sel = input('(B)uy or (s)ell ' + name[i] + '?\n' + prompt).lower()
			if sel == 'buy' or sel == 'b':
				amount = float(input('Please enter the exact amount of ' 
					+ name[i] + ' added:\n' + prompt))
				if amount > 0:
					total = float(input('Please enter the total amount spent on ' + str(abbv[i]).upper() + ':\n$'))
					total = coinTotal[i] + total
				elif total == 0:
					total = coinTotal[i]
					print("No change.")
				amount = coinAmount[i] + amount
				newAmount.append(amount)
				newTotal.append(total)
			elif sel == 'sell' or sel == 's':
				amount = float(input('Please enter the exact amount of ' 
					+ name[i] + ' sold:\n' + prompt))
				if amount > 0:
					total = float(input('Please enter the profit from sale of ' 
						+ str(abbv[i]).upper() + ':\n$'))
					total = coinTotal[i] + total
				elif total == 0:
					total = coinTotal[i]
					print("No change.")
				amount = coinAmount[i] - amount	
				newAmount.append(amount)
				newTotal.append(total)
		elif coinInvest[i] == False:
			amount = coinAmount[i]
			total = coinTotal[i]
			newAmount.append(amount)
			newTotal.append(total)
			print('No change.')

		i += 1
		
	for i in range(len(coinAmount)):	
		if newAmount[i] != coinAmount[i]:
			coinAmount[i] = newAmount[i]
		if newTotal[i] != coinTotal[i]:
			coinTotal[i] = newTotal[i]

		f.write(str(abbv[i]).upper() + ':' + str(coinAmount[i]) + ',')
		f.write(str(abbv[i]).upper() + ' cost:' + str(coinTotal[i]) + ',')

	
def main():
	clear()
	sel = intro()
	if sel == 'check' or sel == 'c':
		clear()
	elif sel == 'update' or sel == 'u':
		update()
	elif sel == 'enter' or sel == 'e':
		enter()

	load(roi)
	stop = True

main()
stop = True