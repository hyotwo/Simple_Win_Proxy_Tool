from pynput.keyboard import Listener, Key, KeyCode
import win32api
import os
import sys
from itertools import cycle

class color:
    d='\033[00m'
    black='\033[30m'
    red='\033[31m'
    green='\033[32m'
    yellow='\033[33m'
    magenta='\033[35m'
    white='\033[37m'
    bred='\033[91m'
    bgreen='\033[92m'
    byellow='\033[93m'
    bblue='\033[94m'
    cyan='\033[96m'
 
store = set()
text=['Proxy on', 'Proxy off']
lc = cycle(text)
os.system('color')

print (" ####                                       #                    ##")
print (" #   #  # ##    ###   #  #   #   #         ####    ###    ###     #")
print (" ####   ##     #   #   ##    #   #          #     #   #  #   #    #")
print (" #      #      #   #   ##     ####          #     #   #  #   #    #")
print (" #      #       ###   #  #       #           ##    ###    ###    ###")
print ("                              ###  ")



qs = input("Do you want to use Proxy on/off as"+color.byellow+" one key?"+color.d+"(Y/N)")

if qs == "y" or qs == "Y":

    k1 = input("Proxy on Key Set : Alt + ")
    k2 = "NULL"
    
elif qs == "n" or qs == "N":
  while True:

    

    k1 = input("Proxy on Key Set : Alt + ")
    k2 = input("Proxy off Key Set : Alt + ")  

    if k1 == k2 or k1 == "0" or k2 == "0":
  
     print(color.red+"The same key is not possible."+color.d)
  
    else:
    
     break
    
else:
    print("Error")
    sys.exit()
    


HOT_KEYS = {
    
      'proxy': set([ Key.alt_l, KeyCode(char=k1)] )
    , 'proxy_off': set([ Key.alt_l, KeyCode(char=k2)] )
    , 'proxy_status': set([ Key.alt_l, KeyCode(char='0')] )
    , 'exit': set([Key.alt_l, Key.esc] )
}


print ("\033[91m"+"------------------------control------------------------"+color.d)
print (color.bgreen+"○ Proxy on-Alt+"+k1+color.d+" ::::::: "+color.magenta+"○ Proxy off-Alt+"+k2+color.d+" ::::::: "+color.yellow+"○ Proxy Status-Alt+0"+color.d+" ::::::: "+color.red+"○ Exit-Alt+esc"+color.d)
 
def proxy():
    nex = next(lc)
    if nex == 'Proxy on':
     print(color.bgreen+nex+color.d)
     os.system("winproxy on")
    else:
     print(color.bred+nex+color.d)
     os.system("winproxy off")
     
def proxy_off():
    print(color.bred+'proxy off'+color.d)
    os.system("winproxy off")

def proxy_status():
    print(color.byellow+'proxy status'+color.cyan)
    os.system("winproxy view")
    print(color.white+"-------------------------------"+color.d)

def exit():
    print("Exit")
    sys.exit()    

def handleKeyPress( key ):
    store.add( key )
 
    for action, trigger in HOT_KEYS.items():
        CHECK = all([ True if triggerKey in store else False for triggerKey in trigger ])
 
        if CHECK:
            try:
                action = eval( action )
                if callable( action ):
                    action()
                    store.clear()
            except NameError as err:
                print( err )
 
def handleKeyRelease( key ):
    if key in store:
        store.clear()

with Listener(on_press=handleKeyPress, on_release=handleKeyRelease) as listener:
    listener.join()
