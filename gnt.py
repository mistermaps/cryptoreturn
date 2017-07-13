import urllib.request
import json

def gnt():
	with urllib.request.urlopen("https://api.coinmarketcap.com/v1/ticker/golem-network-tokens/") as url:
		data = json.loads(url.read().decode())
		data = str(data).split()
		gntPrice = float(str(data[9]).replace("'","").replace(',',''))
		return gntPrice
gntPrice = gnt()
print("%.2f" % gntPrice)
