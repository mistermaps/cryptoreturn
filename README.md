# cryptoreturn
simple python scripts for calculating ROI in crypto, with interactive main program, as well a status bar format

![Screenshot](https://raw.githubusercontent.com/mistermaps/cryptoreturn/master/images/crTitle.png)
![Screenshot](https://raw.githubusercontent.com/mistermaps/cryptoreturn/master/images/crDemo3.png)

repo also includes scripts (intended for status bars) for monitoring four major currencies (BTC, ETH, GNT, ANS)

program by maps, feel free to modify

product released under the GPL 3.0 or later versions license

coins supported as of version 2.0 7/24/17:
Bitcoin, Ethereum, Litecoin, Golem, Neo, Stratis, Ripple, OmiseGO, Syndicate

note: coinbar implementation still needing update; currently only supports Bitcoin, Ethereum, Golem, and NEO
### running the program
run cryptoreturn.py and follow the onscreen prompts

both cryptoreturn and coinbar require coins.py and values.csv in the same directory to function

comes shipped with a zeroed values.csv

![Screenshot](https://raw.githubusercontent.com/mistermaps/cryptoreturn/master/images/crDemo2.png)

use cryptoreturn's 'enter' function for first time use - to fill out values.csv for later/coinbar use - and 'update' for any additional purchases/sales
use 'check' function to check on ROI

###### for coinBar.py implementation in i3 blocks:
easiest use is to point i3blocks.conf (or equivalent) to /cryptoreturn/ directory; see attached example i3blocks.conf

alternatively, once the .csv file has been filled out, copy the files to the .i3 directory and uncomment that path in source

###### for other status bars
as of yet untested, but should work with any python friendly status bar along similar lines

example of various bar i3bocks formats, with coinscripts included:
![Screenshot](https://raw.githubusercontent.com/mistermaps/cryptoreturn/master/images/crBarCoinROI.png)
![Screenshot](https://raw.githubusercontent.com/mistermaps/cryptoreturn/master/images/crBarAll.png)
![Screenshot](https://raw.githubusercontent.com/mistermaps/cryptoreturn/master/images/crBarAmountValue.png)
![Screenshot](https://raw.githubusercontent.com/mistermaps/cryptoreturn/master/images/crBarPerCoinValue.png)
![Screenshot](https://raw.githubusercontent.com/mistermaps/cryptoreturn/master/images/crBarPerCoinROI.png)
![Screenshot](https://raw.githubusercontent.com/mistermaps/cryptoreturn/master/images/crBarEverything.png)
![Screenshot](https://raw.githubusercontent.com/mistermaps/cryptoreturn/master/images/crBarTotalROI.png)

### to do:
as of v2.0:
- rewrite coinBar to 
- add more currencies and exchanges
- create configuration menu: allow user to pick from preferred exchange, set path manually, toggle display options
- add argument parser to run program from command line
- continue beautifying, streamlining, and improving; ensure conventionality in source
- continuing rewriting program to be more Pythonic as knowledge grows
### if you find this useful and are feeling generous:

btc: 12uqmJYWVUFQXB3kvKRRd69mVPK9mC8qJa

eth: 0x3dB53F7A2fb714A2Df4E94c3E8e00342DB79aec0


