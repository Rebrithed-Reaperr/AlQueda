import os, sys, time
from time import sleep as timeout
def restart_program():
	os.system(' clear ')
print " [01]> Wifi-Hacker  "
print " [02]> Wifi-Hacking "
print " [03]> lazyaircrack "
print " [04]> Install 	   "
print
print " [00]> Exit 	   "
print
Wifi = raw_input(" Wifi Hacking ==>> ")
if Wifi == '[01]' or Wifi == '1':
	os.system(' clear ')
	os.system(' cd wifi-hacker && chmod +x wifi-hacker && ./wifi-hacker ')
elif Wifi == '[02]' or Wifi == '2':
	os.system(' clear ')
	os.system(' cd Wifi-Hacking && python3 Wifi-Hacking.py ')
elif Wifi == '[03]' or Wifi == '3':
	os.system(' clear ')
	os.system(' cd lazyaircrack && chmod +x lazyaircrack.sh && bash lazyaircrack.sh ')
elif Wifi == '[04]' or Wifi == '4':
	os.system(' clear ')
	os.system(' sudo apt install python3 aircrack-ng && git clone https://github.com/3xploitGuy/lazyaircrack && git clone https://github.com/ankit0183/Wifi-Hacking && git clone https://github.com/esc0rtd3w/wifi-hacker ')
elif Wifi == '[00]' or Wifi == '0':
	os.system(' clear ')
	os.system(' python2 alqueda.py ')
