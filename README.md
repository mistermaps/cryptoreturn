# cryptoreturn
simple python scripts for calculating ROI in crypto, with interactive main program, as well a status bar format

![Screenshot](https://raw.githubusercontent.com/mistermaps/cryptoreturn/master/images/crDemo1.png)
![Screenshot](https://raw.githubusercontent.com/mistermaps/cryptoreturn/master/images/crDemo3.png)

repo also includes scripts (intended for status bars) for monitoring four major currencies (BTC, ETH, GNT, ANS)

program by maps, feel free to modify
product released under the GPL 3.0 or later versions license
### running the program
run cryptoreturn.py and follow the onscreen prompts
both cryptoreturn and coinbar require coins.py and values.csv in the same directory to function
comes shipped with a zeroed values.csv

![Screenshot](https://raw.githubusercontent.com/mistermaps/cryptoreturn/master/images/crDemo2.png)

use cryptoreturn's 'enter' function for first time use - to fill out values.csv for later/coinbar use - and 'update' for any additional purchases/sales
use 'check' function to check on ROI


###### for coinBar.py implementation in i3 blocks:
easiest use is to point i3blocks.conf (or equivalent) to /cryptoreturn/ directory; see attached example i3blocks.conf

alternatively, once the .csv file has been filled out, one could copy the files to the .i3 directory
###### for other status bars
as of yet untested, but should work with any python friendly status bar along similar lines

### dependencies:
requires python 3 with the following installed:
	urllib
	json
	csv

(most of these should be stock)
if not, run ****pip3 install urllib json csv sys* (may need root access)

### to do:
1) add more currencies and exchanges
	- potentially allow user to pick from multiple exchanges
2) improve update function
3) continue beautifying, streamlining, and improving

### if you find this useful and are feeling generous:

btc: 12uqmJYWVUFQXB3kvKRRd69mVPK9mC8qJa

eth: 0x3dB53F7A2fb714A2Df4E94c3E8e00342DB79aec0

example of various bar i3bocks formats, with coinscripts included:
![Screenshot](https://raw.githubusercontent.com/mistermaps/cryptoreturn/master/images/crBarCoinROI.png)
![Screenshot](https://raw.githubusercontent.com/mistermaps/cryptoreturn/master/images/crBarAll.png)
![Screenshot](https://raw.githubusercontent.com/mistermaps/cryptoreturn/master/images/crBarAmountValue.png)
![Screenshot](https://raw.githubusercontent.com/mistermaps/cryptoreturn/master/images/crBarPerCoinValue.png)
![Screenshot](https://raw.githubusercontent.com/mistermaps/cryptoreturn/master/images/crBarPerCoinROI.png)
![Screenshot](https://raw.githubusercontent.com/mistermaps/cryptoreturn/master/images/crBarEverything.png)
![Screenshot](https://raw.githubusercontent.com/mistermaps/cryptoreturn/master/images/crBarTotalROI.png)
