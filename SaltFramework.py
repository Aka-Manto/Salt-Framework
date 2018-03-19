#!/usr/bin/python
#############################################
#                                  ___  __  #
# /\  |__/  /\      |\/|  /\  |\ |  |  /  \ #
#/~~\ |  \ /~~\     |  | /~~\ | \|  |  \__/ #
#                                           #                                                                               
#############################################
# Import Needed Modules##
########################

import os
from colorama import Fore, Back, Style

####################
### Create Menu ###
##################
os.system('clear')
print (Fore.CYAN + """     ___                _,         ___        
,=--\___\ ___          (_   /\  |   |  /      
    /   \/   \         ,_) /--\ |__ | .       
   |   O    O |__                             
    \___/\___/||||     Oh, good God, the      
       ,-___-.``'`      pain! It burns!       
       |(___)|                                
       `-----'      - Salt Framework v1.0 -   
          /                                   """)
print (Style.RESET_ALL + "-MITM")
print (Fore.GREEN + "   -MITMf")
print (Style.RESET_ALL + "-Passwords")
print (Fore.BLUE + "   -Cupp")
print (Style.RESET_ALL + "-Powershell")
print (Fore.MAGENTA + "   -Empire   -Unicorn")
print (Style.RESET_ALL + "-BruteForce	")
print (Fore.YELLOW + "   -ProxyGram")
print (Style.RESET_ALL + "-RATS")
print (Fore.RED + "   -TheFatRat   -PupyGen   -PupyShell   -Spyrat")
print (Style.RESET_ALL + "-Phishing")
print (Fore.CYAN + "   -SocialFish")
print (Style.RESET_ALL + "Type -Test- for an example")
print (Style.RESET_ALL + 17 * '-')

###########################
### Gather user input ####
#########################

choice = raw_input('Select your Tool : ')

##########################################
### Set specific Arguements for Tools ###
#######################################

AKAMANTO = raw_input("Enter Any Desired Options: ")

######################################
### Set specific Command formulas ###
####################################

TEST="python test.py "+AKAMANTO

UNICORN="python unicorn.py "+AKAMANTO

EMPIRE="python empire.py "+AKAMANTO

PROXYGRAM="python instagram.py "+AKAMANTO

CUPP="python cupp.py "+AKAMANTO

MITMF="python mitmf.py "+AKAMANTO

TFR="./fatrat "+AKAMANTO

PUPYGEN="python pupygen.py "+AKAMANTO

PUPYSHELL="python pupysh.py "+AKAMANTO

SPYRAT="python spyrat.py "+AKAMANTO

SOCIALFISH="python SocialFish.py "+AKAMANTO

####################################################
### Uses action as per selected ###
##################################################

if choice == "Test":
	os.chdir("./Libraries/ExampleFolder")
	os.system('clear')
	os.system(TEST)
elif choice == "Unicorn":
	os.chdir("./Libraries/Powershell/unicorn")
	os.system(UNICORN)
elif choice == "Empire":
	os.chdir("./Libraries/Powershell/Empire")
	os.system(EMPIRE)
elif choice == "Proxygram":
	os.chdir("./Libraries/BruteForce/Proxygram")
	os.system(PROXYGRAM)
elif choice == "Cupp":
	os.chdir("./Libraries/Passwords/cupp")
	os.system(CUPP)
elif choice == "MITMf":
	os.chdir("./Libraries/MITM/MITMf")
	os.system(MITMF)
elif choice == "TheFatRat":
	os.chdir("./Libraries/RATS/TheFatRat")
	os.system(TFR)
elif choice == "PupyGen":
	os.chdir("./Libraries/RATS/pupy/pupy")
	os.system(PUPYGEN)
elif choice == "PupyShell":
	os.chdir("./Libraries/RATS/pupy/pupy")
	os.system('clear')
	os.system(PUPYSHELL)
elif choice == "Spyrat":
	os.chdir("./Libraries/RATS/spyrat")
	os.system('clear')
	os.system(SPYRAT)
elif choice == "SocialFish":
	os.chdir("./Libraries/Phishing/SocialFish")
	os.system('clear')
	os.system(SOCIALFISH)
elif choice == "Help":
        print ("Make Sure You Capitalize Your Selection.")
elif choice == "help":
        print ("Make Sure You Capitalize Your Selection.")
elif choice == "Exit":
        print ("Save a Snail, Say no to SALT")
elif choice == "":
        print ("Try Entering Something Next Time, Bubby")
else:    ## default ##
        print ("Invalid response. Try again...")