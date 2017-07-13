#!/usr/bin/env python3

#bitcoin & ethereum ROI calculator
#author: maps
#feel free to modify

import urllib.request
import json
import csv
import os
import itertools
import threading
import time
import sys
from coins import Coins

done = False
coinOpt = ['Bitcoin','Ether','Golem','Antshares']
coinSel = []
coinInvest = [False for i in range(len(coinOpt))]
USER = os.path.expanduser('~')
prompt = '>>\t'

class spinner(threading.Thread):

    def run(self):
            global stop
            print ('Calculating ROI:')
            #sys.stdout.flush()
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
                    #sys.stdout.write('\033[F')
stop = False




#function for keeping the screen clear
def clear():
	os.system('cls' if os.name == 'nt' else 'clear')
def load(func):
	s = spinner()
	s.start()
	try:
		func()
		stop = True
	except KeyboardInterrupt or EOFError:
         stop = True

def intro():
	print("	               _                 _                    ")
	print("  ___ _ __ _   _ _ __ | |_ ___  _ __ ___| |_ _   _ _ __ _ __  ")
	print(" / __| '__| | | | '_ \| __/ _ \| '__/ _ \ __| | | | '__| '_ \ ")
	print("| (__| |  | |_| | |_) | || (_) | | |  __/ |_| |_| | |  | | | |")
	print(" \___|_|   \__, | .__/ \__\___/|_|  \___|\__|\__,_|_|  |_| |_|")
	print("           |___/|_|  											")
	print('\n Welcome to CryptoReturn, the cryptocurrency ROI calculator.')
	print('\t\t\tWritten by MAPS.\n\n')
	print("\tUse 'Enter' to enter in initial values.")
	print("\tUse 'Update' to add or subtract investments.")
	print("\tSelect 'Check' to calculate ROI.")
	print('\nAfter any of these options, the program will calculate your ROI.\n')
	#sel = input('Please select:'\n\t(E)nter\n\t(U)pdate\n\t(C)heck\n').lower()
	print('Please select:')
	time.sleep(.1)
	print('\t(E)nter')
	time.sleep(.1)
	print('\t(U)pdate')
	time.sleep(.1)
	print('\t(C)heck')
	sel = input(prompt)
	return sel
#function that reads from file an populates array with contents
def parse():
	global values
	csv.register_dialect('crypto', delimiter=',')
	#regular config is for Linux, uncomment below for windows; if the program breaks, update the path to reflect where the repo is

	#for windows (untested)
	#with open(USER + '\cryptoreturn\\values.csv')

	#for all Linux distros, assuming you the repo is in your home directory
	with open(USER + '/cryptoreturn/values.csv','r+') as f:
		reader = csv.reader(f, dialect='crypto')
		values = []
		for row in reader:
			values = str(row).split(":")
			values = str(values).split(',')

#function for user to enter amount and cost of BTC, ETH, GNT, and ANS
def enter():
	print('Warning! This will overwrite the file.')
	print('This option intended for first-time use of this program.')
	sel = input('Are you sure you want to continue? (Y)es/(N)o\n').lower()
	if sel == 'yes' or sel == 'y':
		clear()
		#erases the file
		with open(USER + '/cryptoreturn/values.csv','w'): pass

		f = open(USER + '/cryptoreturn/values.csv','r+')
		print("This program currently supports: ")
		#list coins currently built into program
		for i in range(len(coinOpt)):
			print(str(i+1) + ")\t" + str(coinOpt[i]))
		print("\nIf you have holdings in the listed coin, please enter '(Y)es' when prompted.\nHit any other key, otherwise.\n\n")
		for i in range(len(coinOpt)):
			#prompt user for coin investments
			coinSel.insert(i, input("Do you have holdings in " + coinOpt[i] + "?\n").lower())
			print(prompt)
			if coinSel[i] == 'y' or coinSel[i] == 'yes':
				coinInvest[i] = True
		i = 0
		while i < len(coinOpt):
			#bitcoin
			if i == 0:
				if coinInvest[i] == True:
					btcAmount = float(input('Please enter the exact amount of BTC held:\n' + prompt))
					if btcAmount > 0:
						f.write('BTC:' + str(btcAmount) + ',')
						btcTotal = float(input('Please enter the total amount spent on BTC:\n$'))
						f.write('BTC cost:' + str(btcTotal) + ',')
					elif btcAmount == 0:
						f.write('BTC:' + str(0) + ',')
						f.write('BTC cost:' + str(0) + ',')
				elif coinInvest[i] == False:
					f.write('BTC:' + str(0) + ',')
					f.write('BTC cost:' + str(0) + ',')
			#ethereum
			if i == 1:
				if coinInvest[i] == True:
					ethAmount = float(input('Please enter the exact amount of ETH held:\n' + prompt))
					if ethAmount > 0:
						f.write('ETH:' + str(ethAmount) + ',')
						ethTotal = float(input('Please enter the total amount spent on ETH:\n$'))
						f.write('ETH cost:' + str(ethTotal) + ',')
					elif ethAmount == 0:
						f.write('ETH:' + str(0) + ',')
						f.write('ETH cost:' + str(0) + ',')
				elif coinInvest[i] == False:
					f.write('ETH:' + str(0.00) + ',')
					f.write('ETH cost:' + str(0) + ',')
			#Golem
			if i == 2:
				if coinInvest[i] == True:
					gntAmount = float(input('Please enter the exact amount of GNT held:\n' + prompt))
					if gntAmount > 0:
						f.write('GNT:' + str(gntAmount) + ',')
						gntTotal = float(input('Please enter the total amount spent on GNT:\n$'))
						f.write('GNT cost:' + str(gntTotal) + ',')
					elif gntAmount == 0:
						f.write('GNT:' + str(0) + ',')
						f.write('GNT cost:' + str(0) + ',')
				elif coinInvest[i] == False:
					f.write('GNT:' + str(0) + ',')
					f.write('GNT cost:' + str(0) + ',')
			#Antshares
			if i == 3:
				if coinInvest[i] == True:
					ansAmount = float(input('Please enter the exact amount of ANS held:\n' + prompt))
					if ansAmount > 0:
						f.write('ANS:' + str(ansAmount) + ',')
						ansTotal = float(input('Please enter the total amount spent on ANS:\n$'))
						f.write('ANS cost:' + str(ansTotal) + ',')
					elif ansAmount == 0:
						f.write('ANS:' + str(0) + ',')
						f.write('ANS cost:' + str(0) + ',')
				elif coinInvest[i] == False:
						f.write('ANS:' + str(0) + ',')
						f.write('ANS cost:' + str(0) + ',')
			i = i + 1
		clear()
	elif sel == 'no' or sel == 'n':
		clear()

#function for determining positive or negative ROI
def eval(a, b):
	global sym
	if a > b:
		return '+'
	elif a < b:
		return '-'
	if not a:
		return ''

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

#function for updating .csv file
def update():
	clear()
	read()
	btcAmount = read.btcAmount
	btcTotal = read.btcTotal
	ethAmount = read.ethAmount
	ethTotal = read.ethTotal
	gntAmount = read.gntAmount
	gntTotal = read.gntTotal
	ansAmount = read.ansAmount
	ansTotal = read.ansTotal
	f = open(USER + '/cryptoreturn/values.csv','r+')
	print('Please type (y)es or (n)o. Hitting enter or any other key defaults to no.')
	for i in range(len(coinOpt)):
			coinSel.insert(i, input("Update: " + coinOpt[i] + "?\n" + prompt).lower())
			if coinSel[i] == 'y' or coinSel[i] == 'yes':
				coinInvest[i] = True
	i = 0
	while i < len(coinOpt):
		#bitcoin
		if i == 0:
			if coinInvest[i] == True:
				sel = input('(B)uy or (s)ell BTC?\n' + prompt).lower()
				if sel == 'buy' or sel == 'b':
					addBtcAmount = float(input('How much BTC are you adding?\n' + prompt))
					if addBtcAmount > 0:
						btcAmount += addBtcAmount
						f.write('BTC:' + str(btcAmount) + ',')
						addBtcTotal = float(input('How much did you spend to add this amount?\n$'))
						btcTotal += addBtcTotal
						f.write('BTC cost:' + str(btcTotal) + ',')
				elif sel == 'sell' or 's':
					addBtcAmount = float(input('How much BTC did you sell?\n' + prompt))
					if addBtcAmount > 0:
						btcAmount -= addBtcAmount
						f.write('BTC:' + str(btcAmount) + ',')
						addBtcTotal = float(input('At what price did you sell?\n$'))
						btcTotal -= addBtcTotal
						f.write('BTC cost:' + str(btcTotal) + ',')
			elif coinInvest[i] == False:
				f.write('BTC:' + str(btcAmount) + ',')
				f.write('BTC cost:' + str(btcTotal) + ',')
		#ethereum
		if i == 1:
			if coinInvest[i] == True:
				sel = input('(B)uy or (s)ell ETH?\n' + prompt).lower()
				if sel == 'buy' or sel == 'b':
					addEthAmount = float(input('How much ETH are you adding?\n' + prompt))
					if addEthAmount > 0:
						ethAmount += addEthAmount
						f.write('ETH:' + str(ethAmount) + ',')
						addEthTotal = float(input('How much did you spend to add this amount?\n$'))
						ethTotal += addEthTotal
						f.write('ETH cost:' + str(ethTotal) + ',')
				elif sel == 'sell' or 's':
					addEthAmount = float(input('How much ETH did you sell?\n' + prompt))
					if addEthAmount > 0:
						ethAmount -= addEthAmount
						f.write('ETH:' + str(ethAmount) + ',')
						addEthTotal = float(input('At what price did you sell?\n$'))
						ethTotal -= addEthTotal
						f.write('ETH cost:' + str(ethTotal) + ',')
			elif coinInvest[i] == False:
				f.write('ETH:' + str(ethAmount) + ',')
				f.write('ETH cost:' + str(ethTotal) + ',')
			#Golem
		if i == 2:
			if coinInvest[i] == True:
				sel = input('(B)uy or (s)ell GNT?\n' + prompt).lower()
				if sel == 'buy' or sel == 'b':
					addGNTAmount = float(input('How much GNT are you adding?\n' + prompt))
					if addGNTAmount > 0:
						gntAmount += addGNTAmount
						f.write('GNT:' + str(gntAmount) + ',')
						addGNTTotal = float(input('How much did you spend to add this amount?\n$'))
						gntTotal += addGNTTotal
						f.write('GNT Cost:' + str(gntTotal) + ',')
				elif sel == 'sell' or 's':
					addGNTAmount = float(input('How much GNT did you sell?\n' + prompt))
					if addGNTAmount > 0:
						gntAmount -= addGNTAmount
						f.write('GNT:' + str(gntAmount) + ',')
						addGNTTotal = float(input('At what price did you sell?\n$'))
						gntTotal -= addGNTTotal
						f.write('GNT cost:' + str(gntTotal) + ',')
			elif coinInvest[i] == False:
				f.write('GNT:' + str(gntAmount) + ',')
				f.write('GNT cost:' + str(gntTotal) + ',')
			#Antshares
		if i == 3:
			if coinInvest[i] == True:
				sel = input('(B)uy or (s)ell ANS?\n' + prompt).lower()
				if sel == 'buy' or sel == 'b':
					addANSAmount = float(input('How much ANS are you adding?\n' + prompt))
					if addANSAmount > 0:
						ansAmount += addANSAmount
						f.write('ANS:' + str(ansAmount) + ',')
						addANSTotal = float(input('How much did you spend to add this amount?\n$'))
						ansTotal += addANSTotal
						f.write('ANS cost:' + str(ansTotal) + ',')
				elif sel == 'sell' or 's':
					addANSAmount = float(input('How much ANS did you sell?\n' + prompt))
					if addANSAmount > 0:
						ansAmount -= addANSAmount
						f.write('ANS:' + str(ansAmount) + ',')
						addANSTotal = float(input('At what price did you sell?\n$'))
						ansTotal -= addANSTotal
						f.write('ANS cost:' + str(ansTotal) + ',')
				elif coinInvest[i] == False:
						f.write('ANS:' + str(ansAmount) + ',')
						f.write('ANS cost:' + str(ansTotal) + ',')
		i = i + 1
	clear()
#function to get current price from API
def getPrices():
	#requires coins.py file included with repo
	#currently uses kraken for bitcoin & eth
	#uses CoinMarketCap for NEO/ANS and GNT
	coins = Coins()
	global btcPrice
	global ethPrice
	global gntPrice
	global ansPrice
	btcPrice = coins.btc()
	ethPrice = coins.eth()
	gntPrice = coins.gnt()
	ansPrice = coins.ans()

#calculate and display ROI and inputted values
def roi():
	getPrices()
	read()
	#Assignments; not very pythonic - will be upgraded in later iteration
	btcAmount = read.btcAmount
	btcTotal = read.btcTotal
	ethAmount = read.ethAmount
	ethTotal = read.ethTotal
	gntAmount = read.gntAmount
	gntTotal = read.gntTotal
	ansAmount = read.ansAmount
	ansTotal = read.ansTotal
	#equations
	#calculate current market value
	btcValue = btcAmount * btcPrice
	ethValue = ethAmount * ethPrice
	gntValue = gntAmount * gntPrice
	ansValue = ansAmount * ansPrice
	#get total value, total spent
	totalValue = btcValue + ethValue + gntValue + ansValue
	totalSpent = ethTotal + btcTotal + gntTotal + ansTotal
	#individual ROI
	btcROI = eval(btcValue, btcTotal)
	ethROI = eval(ethValue, ethTotal)
	gntROI = eval(gntValue, gntTotal)
	ansROI = eval(ansValue, ansTotal)
	#total ROI
	totalROI = eval(totalValue, totalSpent)
	totalList = [btcAmount, ethAmount, gntAmount, ansAmount]
	l = 0
	for item in totalList:
		if item != 0.00:
			coinInvest[l] = True
		l = l + 1
	i = 0
	clear()
	done = True
	while i < len(coinOpt):
		if i == 0 and coinInvest[i] == True:
			print('Current Bitcoin Price: \n\t\t\t$%.2f' % btcPrice)
			print('Current BTC holdings: \n\t\t\t%.7f' % btcAmount)
			print('Total Bitcoin Spending: \n\t\t\t$%.2f' % btcTotal)
			print('Current Value: \n\t\t\t$%.2f' % btcValue)
			change = eval(btcValue, btcTotal)
			print('Current BTC ROI: \n\t\t\t%s' % str(change) + '$%.2f' % abs(btcTotal - btcValue))
			print()
		elif i == 0 and coinInvest[i] == False:
			print("\nNo " + coinOpt[i] + " holdings to display.\n")
		if i == 1 and coinInvest[i] == True:
			print('Current Ether Price: \n\t\t\t$%.2f' % ethPrice)
			print('Current ETH holdings: \n\t\t\t%.7f' % ethAmount)
			print('Total Ether Spending: \n\t\t\t$%.2f' % ethTotal)
			print('Current Value: \n\t\t\t$%.2f' % ethValue)
			change = eval(ethValue, ethTotal)
			print('Current ETH ROI: \n\t\t\t%s' % str(change) + '$%.2f' % abs(ethTotal - ethValue))
			print()
		elif i == 1 and coinInvest[i] == False:
			print("\nNo " + coinOpt[i] + " holdings to display.\n")
		if i == 2 and coinInvest[i] == True:
			print('Current Golem Price: \n\t\t\t$%.2f' % gntPrice)
			print('Current GNT holdings: \n\t\t\t%.7f' % gntAmount)
			print('Total Golem Spending: \n\t\t\t$%.2f' % gntTotal)
			print('Current Value: \n\t\t\t$%.2f' % gntValue)
			change = eval(gntValue, gntTotal)
			print('Current GNT ROI: \n\t\t\t%s' % str(change) + '$%.2f' % abs(gntTotal - gntValue))
			print()
		elif i == 2 and coinInvest[i] == False:
			print("\nNo " + coinOpt[i] + " holdings to display.\n")
		if i == 3 and coinInvest[i] == True:
			print('Current Antshares Price: \n\t\t\t$%.2f' % ansPrice)
			print('Current ANS holdings: \n\t\t\t%.7f' % ansAmount)
			print('Total Antshares Spending: \n\t\t\t$%.2f' % ansTotal)
			print('Current Value: \n\t\t\t$%.2f' % ansValue)
			change = eval(ansValue, ansTotal)
			print('Current ANS ROI: \n\t\t\t%s' % str(change) + '$%.2f' % abs(ansTotal - ansValue))
			print()
		elif i == 3 and coinInvest[i] == False:
			print("\nNo " + coinOpt[i] + " holdings to display.\n")
		i = i + 1
	print('Total Spent: \n\t\t\t$%.2f' % totalSpent)
	print('Current Combined Value: \n\t\t\t$%.2f' % totalValue)
	change = eval(totalValue, totalSpent)
	print('Current total ROI: \n\t\t\t%s' % str(change) + '$%.2f' % abs(totalSpent - totalValue))

#begin user interactions
def main():
	clear()
	sel = intro()
	if sel == 'check' or sel == 'c':
		clear()
	elif sel == 'update' or sel == 'u':
		update()
	elif sel == 'enter' or sel == 'e':
		enter()
	#roi()
	load(roi)
main()
stop = True
