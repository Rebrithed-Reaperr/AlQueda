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
print " [4]> Instagrams              "
print
print " [0]> Exit                    "
A = raw_input(" AlQueda ==>> ")

if A == '1' or A == '01':
  os.system(' python2 DDoS-Attacks.py ')

elif A == '2' or A == '02':
  os.system(' python2 Website-Attacks.py ')

elif A == '3' or A == '03':
  os.system(' python2 Tracking-Skiddos.py ')

elif A == '4' or A == '04':
  os.system(' python2 Instagrams.py ')

elif A == '0' or A == '00':
  sys.exit()
  
else:
      print "\nERROR: Wrong Input"
      timeout(3)
      restart_program()
