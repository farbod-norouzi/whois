# Start (Import libraries)

import os
from os import system
import socket
import time
import platform 
import sys
try:
    from colorama import Fore
    import random
    from tqdm import tqdm
except:
    print("Installing prerequisites")
    system("pip install random")
    system("pip install tqdm")
    system("pip install colorama")
    exit('\n',"Run script Again")

# Start (Import libraries)

# Start (Banner & Clearing)

def clear():
   result = platform.uname()[0]
   if result == "Windows":
      system("cls")
   elif result == "Linux":
      system("clear")
clear()

print(Fore.RED+ """
oooooo   oooooo     oooo oooo                        o8o           
 `888.    `888.     .8'  `888                        `"'           
  `888.   .8888.   .8'    888 .oo.    .ooooo.       oooo   .oooo.o 
   `888  .8'`888. .8'     888P"Y88b  d88' `88b      `888  d88(  "8 
    `888.8'  `888.8'      888   888  888   888       888  `"Y88b.  
     `888'    `888'       888   888  888   888       888  o.  )88b 
      `8'      `8'       o888o o888o `Y8bod8P'      o888o 8""888P' 
                                                                   
                                                                   
                                                                   """+Fore.RESET)
                                                                
# Start (Banner & Clearing)

# Start (APP & Get Input From User)

try:
    domain = input(Fore.CYAN+"Domain : "+Fore.GREEN).lower()
except:
    print(Fore.RED+ "You canceled the program!"+Fore.RESET)
    sys.exit()
   
domain = domain.replace("http://","")
domain = domain.replace("https://","")
domain = domain.replace("www.","")

# Start (APP & Get Input From User)

# Start (Search For URL On who.is Site)

if domain[-3:] == "org" or domain[-3:] == "com" or domain[-3:] == "net":
    whois_server = "whois.internic.net"
else:
    whois_server =  "whois.iana.org"

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

s.connect((whois_server,43))

s.send((domain+"\r\n").encode())

msg = s.recv(10000)

# Start (Progress bar)

print(Fore.YELLOW+"Please Wait...")
time.sleep(2)

print('\n',Fore.RESET+"Scanning URL...")
time.sleep(4)
for i in tqdm(range(10)):
    
    pass

time.sleep(5)
print(Fore.RESET+"Connect To Who.is Site...")
time.sleep(4)
for i in tqdm(range(10)):
    
    pass

time.sleep(5)
print(Fore.RESET+"Download Data From Who.is...")
time.sleep(4)
for i in tqdm(range(10)):
    
    pass
time.sleep(6)

# End (Progress bar)

print('\n',Fore.LIGHTMAGENTA_EX+"Result:",'\n')
print(Fore.RESET+msg.decode())

# End (Search For URL On who.is Site)