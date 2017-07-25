#!/usr/bin/env python3
import urllib.request
import json

class Coins():

	Abbreviations = ['btc','eth','ltc','gnt','ans','strat','xrp','omg','synx']
	
	def getPrice(self, func):
		func = getattr(Coins, func)
		price = func(self)
		return price

	def ans(self):
		with urllib.request.urlopen(
			"https://api.coinmarketcap.com/v1/ticker/neo/") as url:
			data = json.loads(url.read().decode())
			data = str(data).split()
			ansPrice = float(str(data[9][1:-2:]))
		return ansPrice

	def btc(self):
		with urllib.request.urlopen(
			"https://api.coinmarketcap.com/v1/ticker/bitcoin/") as url:
			data = str(json.loads(url.read().decode())).split()
			btcPrice = float(str(data[9][1:-2:]))
		return btcPrice

	def eth(self):
		with urllib.request.urlopen(
			"https://api.coinmarketcap.com/v1/ticker/ethereum/") as url:
			data = str(json.loads(url.read().decode())).split()
			ethPrice = float(str(data[9][1:-2:]))
		return ethPrice

	def gnt(self):
		with urllib.request.urlopen(
			"https://api.coinmarketcap.com/v1/ticker/golem-network-tokens/") as url:
			data = str(json.loads(url.read().decode())).split()
			gntPrice = float(str(data[9][1:-2:]))
		return gntPrice

	def ltc(self):
		with urllib.request.urlopen(
			"https://api.coinmarketcap.com/v1/ticker/litecoin/") as url:
			data = str(json.loads(url.read().decode())).split()
			ltcPrice = float(str(data[9][1:-2:]))
		return ltcPrice

	def omg(self):
		with urllib.request.urlopen(
			"https://api.coinmarketcap.com/v1/ticker/omisego/") as url:
			data = str(json.loads(url.read().decode())).split()
			omgPrice = float(str(data[9][1:-2:]))
		return omgPrice

	def synx(self):
		with urllib.request.urlopen(
			"https://api.coinmarketcap.com/v1/ticker/syndicate/") as url:
			data = str(json.loads(url.read().decode())).split()
			snyxPrice = float(str(data[9][1:-2:]))
		return snyxPrice

	def strat(self):
		with urllib.request.urlopen(
			"https://api.coinmarketcap.com/v1/ticker/stratis/") as url:
			data = str(json.loads(url.read().decode())).split()
			stratPrice = float(str(data[9][1:-2:]))
		return stratPrice

	def xrp(self):
		with urllib.request.urlopen(
			"https://api.coinmarketcap.com/v1/ticker/ripple/") as url:
			data = str(json.loads(url.read().decode())).split()
			xrpPrice = float(str(data[9][1:-2:]))
		return xrpPrice


