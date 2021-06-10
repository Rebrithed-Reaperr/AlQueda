import os, sys, time
from time import sleep as timeout
def restart_program():
	os.system(' clear ')
print " [01]> track-ip													"
print " [02]> ip-tracekr											"
print " [03]> ip-tracer 										 "
print " [04]> install 													"
print
print " [00]> Exit																	"
print
rebirthed = raw_input(" Tracking-Skiddos ==>> ")
if rebirthed == '01' or rebirthed == '1':
	os.system(' cd track-ip && chmod +x * && ./trackip ')

elif rebirthed == '02' or rebirthed == '2':
	os.system(' cd IP-Tracker && chmod +x * IP-Tracker.py && python3 IP-Tracker.py ')

elif rebirthed == '03' or rebirthed == '3':
	os.system(' cd IP-Tracer && chmod +x * && ./install ')

elif rebirthed == '04' or rebirthed == '4':
	os.system(' git clone https://github.com/htr-tech/track-ip && git clone https://github.com/anonymousproo/IP-Tracker && git clone https://github.com/rajkumardusad/IP-Tracer && python2 Tracking-Skiddos.py ')

elif rebirthed == '00' or rebirthed == '0':
	sys.exit()
	
else:
      print "\nERROR: Wrong Input"
      restart_program()
