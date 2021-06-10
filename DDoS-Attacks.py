import os, sys, time
from time import sleep as timeout
def restart_program():
	os.system(' clear ')
	os.system(' figlet DDoS-Attacks ')
print
print " [01]> DDoS-Attack "
print " [02]> UFONet			   "
print " [03]> Raven-Storm "
print " [04]> CC-attack   "
print " [05]> Overload    "
print " [06]> Install DDOS"
print
print " [00]> Exit 						 "
print
bhydra = raw_input(" DDoS Console ==>> ")

if bhydra == '01' or bhydra == '1':
	os.system(' cd DDoS-Attack && python2 ddos-attack.py ')
elif bhydra == '02' or bhydra == '2':
	os.system(' sudo apt-get install python3-pycurl python3-geoip python3-whois python3-crypto python3-requests python3-scapy libgeoip1 libgeoip-dev python3 setup.py install ')
elif bhydra == '03' or bhydra == '3':
	os.system(' cd Raven-Storm && pip3 install -r requirements.txt && python3 main.py ')
elif bhydra == '04' or bhydra == '4':
	os.system(' cd CC-attack && python3 cc.py ')
elif bhydra == '05' or bhydra == '5':
	os.system(' sudo pip3 install colorama termcolor requests ')
	os.system(' cd Overload-DoS && chmod +x * && ./install-overload ')
elif bhydra == '06' or bhydra == '6':
	os.system(' git clone https://github.com/Ha3MrX/DDos-Attack && git clone https://github.com/epsylon/ufonet && git clone https://github.com/Taguar258/Raven-Storm && git clone https://github.com/Leeon123/CC-attack && git clone https://github.com/codingplanets/Overload-DoS ')
