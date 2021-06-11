import os, sys, time
from time import sleep as timeouut
def restart_program():
	os.system(' clear ')
print
print " [01]> Wifi-Hacker   "
print " [02]> Wifi-Hacking  "
print " [03]> Installing 		 "   
print
print " [00]> EXIT "
print
WifiF = raw_input(" WiFi-Hacking ==>> ")

if WiFiF == '01' or WiFiF == '1':
	os.system(' clear ')
	os.system(' cd wifi-hacker && chmod +x wifi-hacker && ./wifi-hacker ')
elif WiFiF == '02' or WiFiF == '2':
	os.system(' clear ')
	os.system(' cd Wifi-Hacking && python3 Wifi-Hacking.py ')
elif WiFiF == '03' or WiFiF == '3':
	os.system(' clear ')
	os.system(' git clone https://github.com/esc0rtd3w/wifi-hacker && git clone https://github.com/ankit0183/Wifi-Hacking ')
elif WiFiF == '00' or WiFiF == '0':
	os.system(' python2 alqueda.py ')
