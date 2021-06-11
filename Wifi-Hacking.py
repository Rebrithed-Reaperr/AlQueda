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
Wifi = raw_input(" WiFi-Hacking ==>> ")

if WiFi == '01' or WiFi == '1':
	os.system(' clear ')
	os.system(' cd wifi-hacker && chmod +x wifi-hacker && ./wifi-hacker ')
elif WiFi == '02' or WiFi == '2':
	os.system(' clear ')
	os.system(' cd Wifi-Hacking && python3 Wifi-Hacking.py ')
elif WiFi == '03' or WiFi == '3':
	os.system(' clear ')
	os.system(' git clone https://github.com/esc0rtd3w/wifi-hacker && git clone https://github.com/ankit0183/Wifi-Hacking ')
elif WiFi == '00' or WiFi == '0':
	os.system(' clear ')
	print " Adios come back sometime "
 time.sleep(2)
 sys.exit()
	os.system(' python2 alqueda.py ')
