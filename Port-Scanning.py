import os, sys, time
from time import sleep
def restart_program():
  os.system(' clear ')                                                                                                                                   
print ("    _/_/_/                          _/                    _/_/_/                                          _/                     ")
print ("   _/    _/    _/_/    _/  _/_/  _/_/_/_/              _/          _/_/_/    _/_/_/  _/_/_/    _/_/_/        _/_/_/      _/_/_/  ") 
print ("  _/_/_/    _/    _/  _/_/        _/      _/_/_/_/_/    _/_/    _/        _/    _/  _/    _/  _/    _/  _/  _/    _/  _/    _/   ")  
print (" _/        _/    _/  _/          _/                        _/  _/        _/    _/  _/    _/  _/    _/  _/  _/    _/  _/    _/    ")   
print ("_/          _/_/    _/            _/_/              _/_/_/      _/_/_/    _/_/_/  _/    _/  _/    _/  _/  _/    _/    _/_/_/     ")   
print ("                                                                                                                         _/      ")    
print ("                                                                                                                      _/_/       ")       
os.system(' clear ')
time.sleep(2) 
print (" .d8888.  .o88b.  .d8b.  d8b   db      d888888b db   db d88888b .d8888. d88888b      .d8888. db   dD d888888b d8888b. .d8888. ") 
print (" 88'  YP d8P  Y8 d8' `8b 888o  88      `~~88~~' 88   88 88'     88'  YP 88'          88'  YP 88 ,8P'   `88'   88  `8D 88'  YP ") 
print (" `8bo.   8P      88ooo88 88V8o 88         88    88ooo88 88ooooo `8bo.   88ooooo      `8bo.   88,8P      88    88   88 `8bo.   ") 
print ("   `Y8b. 8b      88~~~88 88 V8o88         88    88~~~88 88~~~~~   `Y8b. 88~~~~~        `Y8b. 88`8b      88    88   88   `Y8b. ")
print (" db   8D Y8b  d8 88   88 88  V888         88    88   88 88.     db   8D 88.          db   8D 88 `88.   .88.   88  .8D db   8D ")
print (" `8888Y'  `Y88P' YP   YP VP   V8P         YP    YP   YP Y88888P `8888Y' Y88888P      `8888Y' YP   YD Y888888P Y8888D' `8888Y' ")
time.sleep(1.5)
print (" [01]> sandmap  ")
print (" [02]> furious  ")
print (" [03]> silver   ")
print (" [04]> easynmap ")
print (" [05]> Install  ")
      
print (" [00]> Exit     ")
Scan = input(" Port Scanning ==>> ")
if Scan == '01' or Scan == '1':
       time.sleep(2)
       os.system(' clear ')
       os.system(' cd sandmap && chmod +x * && bash setup.sh ')
elif Scan == '02' or Scan == '2':
       time.sleep(2)
       os.system(' clear ')
       os.system(' pip3 install libpcap && cd furious && go get -u github.com/liamg/furious ')
elif Scan == '03' or Scan == '3':
       time.sleep(2)
       os.system(' clear ')
       os.system(' cd Silver && pip3 install -r requirements.txt && python3 silver.py ')
elif Scan == '04' or Scan == '4':
       time.sleep(2)
       os.system(' clear ')
       os.system(' cd easynmap && pip3 install -r requirements.txt && python3 easynmap.py ')
elif Scan == '05' or Scan == '5':
       time.sleep(2)
       os.system(' clear ')
       os.system(' git clone https://github.com/trimstray/sandmap && git clone https://github.com/liamg/furious && git clone https://github.com/s0md3v/Silver && git clone https://github.com/noenoughdata/easynmap ')
elif Scan == '00' or Scan == '0':
       time.sleep(2)
       print (" Why Leave SO Soon? ")
       os.system(' python3 alqueda.py ')
