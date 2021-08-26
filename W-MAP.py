import os
import time
from Modules.Scan_tools import *
from Core.help import *
from Core.banners import *
from Core.auto_complete import *
from Core.wlan import *
from Modules.sniffing_and_spoofing import Sniffing
from Core.colors import *
import socket
import sys

Bans.ban_wmap('')

Con = input('\nPress [ Enter ] to continue ...')

# if root or not :
root = os.getuid()

time.sleep(1)

if root == 0:
    pass

else:
    print(f'[{Red}!!{White}] Error : you must be root !! \n use " sudo " and type password next step run tool ')
    exit()

os.system('clear')

interfaces()
Interface = input(f'\n\n[{Cyan}?{White}] Enter name Interface : ')
Stop = Interface+'mon'
os.system('clear')
Bans.bans('', Interface)
def d5tr(): # Tools



    # for choose 
    CommandComplete()
    what = input(f'\n\n{Cyan}W-MAP3{White} > ')

# -----------------------------------------------------------------------------#

    if what == 'use handshake/encryption/all' :
        interfaces()

        os.system(f'bash Modules/handshake.sh 1 {Interface}')
        if KeyboardInterrupt :
            print('\n')
            d5tr()

    elif what == 'use handshake/encryption/wep' :
        interfaces()

        os.system(f'bash Modules/handshake.sh 2 {Interface}')

        if KeyboardInterrupt :
            print('\n')
            d5tr()

    elif what == 'use handshake/encryption/wpa' :
        interfaces()


        os.system(f'bash Modiles/handshake.sh 3 {Interface}')
        if KeyboardInterrupt :
            print('\n')
            d5tr()

#-----------------------------------------------------------------------------#

    elif what == 'use sniff/my/device' :  # sniffing_and_spoofing wifi

        Sniffing.SNIFFING(Interface)

# -----------------------------------------------------------------------------#

        if KeyboardInterrupt:
            print('\n')
            d5tr()  # back

    elif what == 'use network/scan/devices' : # Network scan

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        the_ip = s.getsockname()[0]+'/24'
        Scan_tools.Network_Scanner(the_ip)
        s.close()

        if KeyboardInterrupt:
            print('\n')
            d5tr()

# -----------------------------------------------------------------------------#

    elif what == 'use port/scan':  # port scan
        HOST = input(f'\n[{Cyan}?{White}] Enter IP target : ')
        PORTS = input(f'[{Cyan}?{White}] How many port you want scan (default:65535) :')

        Scan_tools.Port_scanner(HOST, PORTS)

        if KeyboardInterrupt:
            print('\n')
            d5tr()

    
#------------------------------------------------------------------------------#

    elif what == 'use scan/wifi':
        try:
            os.system('rm Ss.txt')
        except:
            pass

        Start_Scan = Scan_tools()
        Start_Scan.Scan_WIFI(Interface)
        
        if KeyboardInterrupt :
            os.system('rm Ss.txt')
            d5tr()
# -----------------------------------------------------------------------------#

    elif what == 'use fake/wifi': # fake WI-FI

        try:
            print('\n')
            os.system(f'bash Modules/Fake_wifi.sh 2 {Interface}')

            if KeyboardInterrupt :
                print('\n')
                
                os.system(f'airmon-ng stop {Stop}')
                print('\n')
                d5tr()

        except:
            print('Error .. !')
            print('\n')
            d5tr()
        if KeyboardInterrupt:
            print('\n')
            d5tr()

#######################

    elif what == 'use fake/wifi/random':

        try:
            print('\n')
            os.system(f'bash Modules/Fake_wifi.sh 1 {Interface}')

            if KeyboardInterrupt :

                print('\n')
                os.system(f'airmon-ng stop {Stop}')
                print('\n')
                d5tr()

        except:
            print('Error .. !')
            print('\n')
            d5tr()
        if KeyboardInterrupt:
            print('\n')
            d5tr()



# -----------------------------------------------------------------------------#


    elif what == 'use password/wifi':  # password wifi
        os.system('bash Modules/password_wifi.sh')
        if KeyboardInterrupt:
            print('\n')
            d5tr()
#------------------------------------------------------------------------------#



    if what == 'use deauth/attack/wifi/aireplay-ng' :

        os.system(f'bash Modules/Deauth_attack.sh 1 {Interface}')

        if KeyboardInterrupt:
            print('\n')
            os.system(f'airmon-ng stop {Stop}')
            print('\n')
            d5tr()

    elif what == 'use deauth/attack/wifi/mdk3' :
        interfaces()

        os.system(f'bash Modules/Deauth_attack.sh 2 {Interface}')

        if KeyboardInterrupt:
            print('\n')
            os.system(f'airmon-ng stop {Stop}')
            print('\n')
            d5tr()

    elif what == 'use deauth/attack/wifi/one/device/aireplay-ng' :
        interfaces()

        os.system(f'bash Modules/Deauth_attack.sh 3 {Interface}')
        if KeyboardInterrupt:
            print('\n')
            os.system(f'airmon-ng stop {Stop}')
            print('\n')
            d5tr()

#-----------------------------------------------------------------------------#

    elif what == 'use arp/spoofing/attack': # ARP spoofing

        os.system('xterm -hold -e python3 Modules/sniffing_and_spoofing/ARP_attack.py & xterm -hold -e python3 Modules/sniffing_and_spoofing/sniff_http.py & xterm -hold -e python3 Modules/sniffing_and_spoofing/sniff_for_ARP.py')
        if KeyboardInterrupt :
            print('\n')
            d5tr()

    elif what == 'use arp/spoofing/attack/wireshark' :
        print('\n')
        print(f'{Red} Use wireshrk to see packets ...{White}')
        print('\n')
        os.system('xterm -hold -e python3 Modules/sniffing_and_spoofing/ARP_attack.py & xterm -hold -e wireshark')
        d5tr()
        if KeyboardInterrupt :
            print('\n')
            d5tr()


#-----------------------------------------------------------------------------#

    elif what == 'use mac/spoofing/attack':
        interfaces()
        os.system(f'bash Modules/sniffing_and_spoofing/Mac_spoofing.sh {Interface}')

        d5tr()
        if KeyboardInterrupt:
            d5tr()

    elif what == 'banner' :
        Bans.bans('', Interface)
        print('\n')
        d5tr()

    elif what == 'clear':
        os.system('clear')
        d5tr()

    elif what == 'help' :
        
        Help()
        d5tr()
    

    elif what == '':
        d5tr()

    elif what[0] == '!':
        try:
            Claners = what.replace('!', '')
            COMMANDS = os.system(f'{Claners}')
            d5tr()
        except:

            d5tr()

    elif what == 'exit':  # exit !!
        print('\nGOOD BAY ...')
        sys.exit()

    else:
        print(f'{Red}Unknow Command !{White}')
        d5tr()
# start the tool ...
d5tr()
