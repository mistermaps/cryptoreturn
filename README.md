# cryptoreturn
simple python script for calculating ROI in crypto, with bar and interactive format

comes in two formats: coin.py, the interactive program, and coinBar.py, for use with i3blocks or any status bar that can implement python scripts

### running the program
the interactive version, coin.py, requires a values.csv file in the same directory

use the (e)nter function to provide values - intended for first launch only
use the (u)pdate function to update values such as currency purchased (sell feature not yet implemented)
use the (c)heck function to calculate ROI at current market prices

#### to do:
program does not presently loop so must be launched to update values: update so program loops through main function and quits on user command

program currently only accepts BTC and ETH and uses the Kraken API: long term, implement popular currencies and exchanges (antshares are next.)

program currently only allows you to aggregate coin & cost: implement ability to lower currency amount and add profit

bar version runs off of values hardcoded into source: fork bar to run off of .csv

program by maps, feel free to modify
product released under the GPL 3.0 or later versions license


if you find this useful and are feeling generous:

btc: 12uqmJYWVUFQXB3kvKRRd69mVPK9mC8qJa

eth: 0x3dB53F7A2fb714A2Df4E94c3E8e00342DB79aec0

example of the coin.py program:
![Screenshot](https://github.com/mistermaps/cryptoreturn/blob/master/coinDemo.png)


example in i3bar:
![Screenshot](https://raw.githubusercontent.com/mistermaps/cryptoreturn/master/barExample.png)
