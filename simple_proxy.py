#Made by Hyotwo - https://github.com/hyotwo

from pynput.keyboard import Listener, Key, KeyCode
from plyer import notification
import os
import sys
import win32api
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
text = ['Proxy on', 'Proxy off']
lc = cycle(text)
os.system('color')

print (" ####                                       #                    ##")
print (" #   #  # ##    ###   #  #   #   #         ####    ###    ###     #")
print (" ####   ##     #   #   ##    #   #          #     #   #  #   #    #")
print (" #      #      #   #   ##     ####          #     #   #  #   #    #")
print (" #      #       ###   #  #       #           ##    ###    ###    ###")
print ("                              ###  ")

while True:
    qs = input("Do you want to use Proxy on/off as"+color.byellow+" One Key?"+color.d+"(Y/N)")

    if qs == "y" or qs == "Y":
        k3 = input("Proxy on/off Key Set : Alt + ")
        k1 = "NULL"
        k2 = "NULL"

        if k3 == "0":
            print(color.red+"Don't set it to 0 key"+color.d)
        else:
            break
    elif qs == "n" or qs == "N":
        while True:
            k1 = input("Proxy on Key Set : Alt + ")
            k2 = input("Proxy off Key Set : Alt + ")
            k3 = "NULL"

            if k1 == k2:
                print(color.red+"The same key is not possible."+color.d)
            elif k1 == "0" or k2 == "0":
                print(color.red+"Don't set it to 0 key"+color.d)
            else:
                break
        break
    else:
        print(color.red+"Y or N only"+color.d)

HOT_KEYS = {
    
      'onekey': set([ Key.alt_l, KeyCode(char=k3)] )
    ,  'proxy_on': set([ Key.alt_l, KeyCode(char=k1)] )
    , 'proxy_off': set([ Key.alt_l, KeyCode(char=k2)] )
    , 'proxy_status': set([ Key.alt_l, KeyCode(char='0')] )
    , 'exit': set([Key.alt_l, Key.esc] )
}
print("\033[91m"+"------------------------control------------------------"+color.d)

if qs == "n" or qs == "N":
    print (color.bgreen+"○ Proxy on-Alt+"+k1+color.d+" ::::::: "+color.magenta+"○ Proxy off-Alt+"+k2+color.d+" ::::::: "+color.yellow+"○ Proxy Status-Alt+0"+color.d+" ::::::: "+color.red+"○ Exit-Alt+esc"+color.d)
else:
    print(color.bgreen+"○ Proxy on/off-Alt+"+k3+color.d+" ::::::: "+color.yellow+"○ Proxy Status-Alt+0"+color.d+" ::::::: "+color.red+"○ Exit-Alt+esc"+color.d)

def onekey():
    nex = next(lc)
    if nex == 'Proxy on':
        print(color.bgreen+nex+color.d)
        os.system("winproxy on")
        notification.notify(title="Proxy_Tool", message="Proxy On", app_name="Proxy_Tool", timeout=3)
    else:
        print(color.bred+nex+color.d)
        os.system("winproxy off")
        notification.notify(title="Proxy_Tool", message="Proxy Off", app_name="Proxy_Tool", timeout=3)

def proxy_on():
    print(color.bgreen+'proxy on'+color.d)
    os.system("winproxy on")
    notification.notify(title="Proxy_Tool", message="Proxy On", app_name="Proxy_Tool", timeout=3)

def proxy_off():
    print(color.bred+'proxy off'+color.d)
    os.system("winproxy off")
    notification.notify(title="Proxy_Tool", message="Proxy off", app_name="Proxy_Tool", timeout=3)

def proxy_status():
    print(color.byellow+'proxy status'+color.d)
    try:
        output = os.popen("winproxy view").read()
        win32api.MessageBox(0, output, 'Proxy Status', 0x40)
    except Exception as e:
        win32api.MessageBox(0, 'Error while getting status', 'Proxy Status Error', 0x10)  
    
def exit():
    print("Exit")
    sys.exit()

def handleKeyPress(key):
    store.add(key)
    for action, trigger in HOT_KEYS.items():
        CHECK = all([True if triggerKey in store else False for triggerKey in trigger])
        if CHECK:
            try:
                action = eval(action)
                if callable(action):
                    action()
                    store.clear()
            except NameError as err:
                print(err)

def handleKeyRelease(key):
    if key in store:
        store.clear()

with Listener(on_press=handleKeyPress, on_release=handleKeyRelease) as listener:
    listener.join()
