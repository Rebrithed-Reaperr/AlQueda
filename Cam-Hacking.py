import os, sys, time
from time import sleep as timeout
def restart_program():
  os.system(' clear ')
print
print " [01]> Cam-Hackers "
print " [02]> CamHack     "
print " [03]> CamPhish    "
print " [04]> Installing  "
print
print " [00]> EXIT 					  "
print
Cam = raw_input(" Cam Hacking ==>> ")
if Cam == '01' or Cam == '1':
	os.system(' clear ')
	os.system(' cd Cam-Hackers && python3 cam-hackers.py ')
elif Cam == '02' or Cam == '2':
	os.system(' clear ')
	os.system(' cd CamHack && chmod +x * && bash CamHack.sh ')
elif Cam == '03' or Cam == '3':
	os.system(' clear ')
	os.system(' cd CanPhish && bash camphish.sh ')
elif Cam == '04' or Cam == '4':
	os.system(' clear ')
	os.system(' pip3 install requests colorama && git clone https://github.com/aktechunt3r/CamPhish && git clone https://github.com/Devil-Tigers/CamHack && git clone https://github.com/AngelSecurityTeam/Cam-Hackers ')
elif Cam == '00' or Cam == '0':
	os.system(' clear ')
	print " Goodbye "
	time.sleep(2)
