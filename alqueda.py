import os, sys, time
from time import sleep as timeout
def restart_program():
  os.system(' clear ')
  os.system(' figlet Al Queda ')
print "Created By: Rebrithed-Reaperr "
print "YouTube: BiggyGh0st           "
print "Github: Rebrithed-Reaperr     "
print "Instagram: pwn.doxgod         "
print
print " [1]> DDoS-Attacks            "
print " [2]> Website-Attacks         "
print " [3]> Tracking Skiddos        "
print " [4]> Installing Tools        "
print " [5]> Instagrams              "
print
print " [0]> Exit                    "
A = raw_input(" AlQueda ==>> ")

elif A == '1' or A == '01':
  os.system(' python2 ddos-attacks.py ')

elif A == '2' or A == '02':
  os.system(' python2 website-attacks.py ')

elif A == '3' or A == '03':
  os.system(' python2 tracking-skiddos.py ')

elif A == '4' or A == '04':
  os.system(' python2 install.py ')

elif A == '5' or A == '05':
  os.system(' python2 instagrams.py ')

elif A == '0' or A == '00':
  sys.exit()
  
else:
      print "\nERROR: Wrong Input"
      timeout(3)
      restart_program()
