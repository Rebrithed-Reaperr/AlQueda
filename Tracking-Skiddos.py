import os, sys, time
from time import sleep as timeout
def restart_program():
	os.system(' clear ')
print " [01]> track-ip		"
print " [02]> ip-tracer 	"
print " [03]> install 		"
print " [04]> Sigit 		"
print
print " [00]> Exit		"
print
rebirthed = raw_input(" Tracking-Skiddos ==>> ")
if rebirthed == '01' or rebirthed == '1':
	os.system(' clear ')
	os.system(' cd track-ip && chmod +x * && ./trackip ')

elif rebirthed == '02' or rebirthed == '2':
	os.system(' clear ')
	os.system(' cd IP-Tracer && chmod +x * && ./install ')

elif rebirthed == '03' or rebirthed == '3':
	os.system(' clear ')
        os.system(' git clone https://github.com/termuxhackers-id/SIGIT && git clone https://github.com/htr-tech/track-ip && git clone https://github.com/anonymousproo/IP-Tracker && git clone https://github.com/rajkumardusad/IP-Tracer && python2 Tracking-Skiddos.py ')

elif rebirthed == '00' or rebirthed == '0':
	sys.exit()
elif rebirthed == '04' or rebirthed == '4':
	os.system(' clear ')
	os.system(' cd SIGIT && bash install.sh && python3 sigit.py ')
	
else:
      print "\nERROR: Wrong Input"
      restart_program()
