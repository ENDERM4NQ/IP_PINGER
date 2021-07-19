import colorama
from colorama import Fore
import os
import time

print('Please enter your username')
username = input()
if username == 'root':
    print('Welcome back! ' + username + ' Please enter your password')
    password = input()
    if password == 'root':
        print('ACCESS GRANTED')
    else:
        print('Incorrect Password!')
        print('ACCESS DENIED')
        exit()
else:
    print('Username not found')
    print('ACCESS DENIED')
    exit()

online = f"""
{Fore.GREEN}/\  ___\   /\ \/ /    /\ \   /\  __-.     /\  __ \   /\ "-.\ \   /\ \       /\ \   /\ "-.\ \   /\  ___\   
{Fore.GREEN}\ \___  \  \ \  _"-.  \ \ \  \ \ \/\ \    \ \ \/\ \  \ \ \-.  \  \ \ \____  \ \ \  \ \ \-.  \  \ \  __\   
{Fore.GREEN} \/\_____\  \ \_\ \_\  \ \_\  \ \____-     \ \_____\  \ \_\\"\_\  \ \_____\  \ \_\  \ \_\\"\_\  \ \_____\ 
{Fore.GREEN}  \/_____/   \/_/\/_/   \/_/   \/____/      \/_____/   \/_/ \/_/   \/_____/   \/_/   \/_/ \/_/   \/_____/ 
"""

offline = f"""
{Fore.RED}/\  ___\   /\ \/ /    /\ \   /\  __-.     /\  ___\   /\  __ \   /\__  _\    /\ \_\ \   /\ \   /\__  _\ 
{Fore.RED}\ \___  \  \ \  _"-.  \ \ \  \ \ \/\ \    \ \ \__ \  \ \ \/\ \  \/_/\ \/    \ \  __ \  \ \ \  \/_/\ \/ 
{Fore.RED} \/\_____\  \ \_\ \_\  \ \_\  \ \____-     \ \_____\  \ \_____\    \ \_\     \ \_\ \_\  \ \_\    \ \_\ 
{Fore.RED}  \/_____/   \/_/\/_/   \/_/   \/____/      \/_____/   \/_____/     \/_/      \/_/\/_/   \/_/     \/_/ 
"""
logo = f"""
{Fore.RED}        ) (         (      *              )        
{Fore.RED}     ( /( )\ )      )\ ) (  `    (     ( /(   (    
{Fore.RED} (   )\()|()/(  (  (()/( )\))(   )\    )\())( )\   
{Fore.RED} )\ ((_)\ /(_)) )\  /(_)|(_)()((((_)( ((_)\ )((_)  
{Fore.RED}((_) _((_|_))_ ((_)(_)) (_()((_)\ _ )\ _((_|(_)_   
{Fore.RED}| __| \| ||   \| __| _ \|  \/  (_)_\(_) \| |/ _ \  
{Fore.RED}| _|| .` || |) | _||   /| |\/| |/ _ \ | .` | (_) | 
{Fore.RED}|___|_|\_||___/|___|_|_\|_|  |_/_/ \_\|_|\_|\__\_\ 
"""

os.system('cls')

def ping():
    while True:
        ping_response = os.system(f'ping -n 1 {IP} >null')
        if ping_response == 0:
            os.system('cls')
            print(logo)
            print(online)
            time.sleep(0.1)
        else:
            os.system('cls')
            print(logo)
            print(offline)
            time.sleep(0.1)

os.system('title Skid Online Checker by ENDERMANQ')

print(logo)
IP = input('Enter skids IP : ')
ping()