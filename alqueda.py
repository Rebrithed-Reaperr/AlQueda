import os, sys, time
from time import sleep as timeout
def restart_program():
  os.system(' clear ')
print
print " Created By: Rebrithed-Reaperr "
print " YouTube: BiggyGh0st           "
print " Github: Rebrithed-Reaperr     "
print " Instagram: pwn.doxgod         "
print
print " [1]> DDoS-Attacks            "
print " [2]> Website-Attacks         "
print " [3]> Tracking Skiddos        "
print " [4]> Instagrams              "
print
print " [0]> Exit                    "
A = raw_input(" AlQueda ==>> ")

if A == '1' or A == '01':
  os.system(' clear ')
  os.system(' python2 DDoS-Attacks.py ')

elif A == '2' or A == '02':
  os.system(' clear ')
  os.system(' python2 Website-Attacks.py ')

elif A == '3' or A == '03':
  os.system(' clear ')
  os.system(' python2 Tracking-Skiddos.py ')

elif A == '4' or A == '04':
 os.system(' clear ')
 print " @pwn.doxgod @no_enough_data @re43p3r @cryp70n1cf4c3 @rxquestnomad @l_sinnxr_l @cybersploiitz @tjtechpro2cybersecurity "

elif A == '0' or A == '00':
  sys.exit()
  print " Sorry to see you leave so soon :( "
else:
      print "\nERROR: Wrong Input"
      timeout(3)
      restart_program()
