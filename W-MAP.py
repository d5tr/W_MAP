from banners import ban
from sniffing_and_spoofing.Sniffing import *
from rest_of_tools.network_scan import *
from rest_of_tools.port_scanner import *
from ETC.wlan import interfaces
from ETC.auto_complete import *
from banners.ban_wmap import *
ban_wmap()

Con = input('\nPress [ Enter ] to continue ...')

# if root or not :
root = os.getuid()

time.sleep(1)

if root == 0:
    pass

else:
    print(f'[{Fore.RED}!!{Fore.WHITE}] Error : you must be root !! \n use " sudo " and type password next step run tool ')
    exit()

os.system('clear')

ban.bans()

def d5tr(): # Tools



    # for choose 
    CommandComplete()
    what = input(f'\n\n{Fore.CYAN}W-MAP3{Fore.WHITE} > ')

# -----------------------------------------------------------------------------#

    if what == 'use handshake/encryption/all' :
        interfaces()

        os.system('bash Handshake/handshake_all.sh ')
        if KeyboardInterrupt :
            print('\n')
            d5tr()

    elif what == 'use handshake/encryption/wep' :
        interfaces()

        os.system('bash Handshake/handshake_wep.sh')

        if KeyboardInterrupt :
            print('\n')
            d5tr()

    elif what == 'use handshake/encryption/wpa' :
        interfaces()


        os.system('bash Handshake/handshake_wpa.sh')
        if KeyboardInterrupt :
            print('\n')
            d5tr()

#-----------------------------------------------------------------------------#

    elif what == 'use sniff/my/device' :  # sniffing_and_spoofing wifi
        interfaces()

        wlans = input(f'[{Fore.CYAN}?{Fore.WHITE}] Enter name interface :')

        SNIFFING(wlans)

# -----------------------------------------------------------------------------#

        if KeyboardInterrupt:
            print('\n')
            d5tr()  # back

    elif what == 'use network/scan/devices' : # Network scan

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        the_ip = s.getsockname()[0]+'/24'
        Network_Scan(the_ip)
        s.close()

        if KeyboardInterrupt:
            print('\n')
            d5tr()

# -----------------------------------------------------------------------------#

    elif what == 'use port/scan':  # port scan
        HOST = input(f'\n[{Fore.CYAN}?{Fore.WHITE}] Enter IP target : ')

        Port_scan(HOST)

        if KeyboardInterrupt:
            print('\n')
            d5tr()

# -----------------------------------------------------------------------------#

    elif what == 'use fake/wifi': # fake WI-FI

        interfaces()

        try:
            print('\n')
            os.system('bash Fake_WIFI/Fake_wifi.sh')

            if KeyboardInterrupt :
                print('\n')
                interfaces()
                Monitor = input(f'\n[{Fore.CYAN}?{Fore.WHITE}] Enter name interface to disable Monitor mode : ')
                os.system(f'airmon-ng stop {Monitor}')
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

        interfaces()


        try:
            print('\n')
            os.system('bash Fake_WIFI/Fake_wifi_random.sh')

            if KeyboardInterrupt :
                print('\n')
                interfaces()
                Monitor = input(f'\n[{Fore.CYAN}?{Fore.WHITE}] Enter name interface to disable Monitor mode : ')
                os.system(f'airmon-ng stop {Monitor}')
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
        os.system('bash rest_of_tools/password_wifi.sh')
        if KeyboardInterrupt:
            print('\n')
            d5tr()
#------------------------------------------------------------------------------#



    if what == 'use deauth/attack/wifi/aireplay-ng' :
        interfaces()

        os.system('bash Deauth_attack/Deauth_attack_WIFI_aireplay.sh')

        if KeyboardInterrupt:
            print('\n')
            interfaces()
            Monitor = input(f'\n[{Fore.CYAN}?{Fore.WHITE}] Enter name interface to disable Monitor mode : ')
            os.system(f'airmon-ng stop {Monitor}')
            print('\n')
            d5tr()

    elif what == 'use deauth/attack/wifi/mdk3' :
        interfaces()

        os.system('bash Deauth_attack/Deauth_attack_WIFI_mdk3.sh')

        if KeyboardInterrupt:
            print('\n')
            interfaces()
            Monitor = input(f'\n[{Fore.CYAN}?{Fore.WHITE}] Enter name interface to disable Monitor mode : ')
            os.system(f'airmon-ng stop {Monitor}')
            print('\n')
            d5tr()

    elif what == 'use deauth/attack/wifi/one/device/aireplay-ng' :
        interfaces()

        os.system('bash Deauth_attack/Deauth_one_device_aireplay.sh')
        if KeyboardInterrupt:
            print('\n')
            interfaces()
            Monitor = input(f'\n[{Fore.CYAN}?{Fore.WHITE}] Enter name interface to disable Monitor mode : ')
            os.system(f'airmon-ng stop {Monitor}')
            print('\n')
            d5tr()

#-----------------------------------------------------------------------------#

    elif what == 'use arp/spoofing/attack': # ARP spoofing

        os.system('xterm -hold -e python3 sniffing_and_spoofing/ARP_attack.py & xterm -hold -e python3 sniffing_and_spoofing/sniff_http.py & xterm -hold -e python3 sniffing_and_spoofing/sniff_for_ARP.py')
        if KeyboardInterrupt :
            print('clear now ...')
            time.sleep(0.5)
            os.system('clear')
            d5tr()

#-----------------------------------------------------------------------------#

    elif what == 'use mac/spoofing/attack':
        interfaces()
        os.system('bash sniffing_and_spoofing/Mac_spoofing.sh')

        d5tr()
        if KeyboardInterrupt:
            d5tr()

    elif what == 'banner' :
        ban.bans()
        print('\n')
        d5tr()

    elif what == 'clear':
        os.system('clear')
        d5tr()

    elif what == 'help' :
        print(f'''
{Fore.RED}
==============================================================================================
|    {Fore.CYAN}Name                                                Description{Fore.RED}                         |       
==============================================================================================
                                               |                                          
[#] {Fore.CYAN}handshake/encryption/all{Fore.RED}                   | [#] {Fore.CYAN}for handshake capture all encryption you can capture{Fore.RED}
[#] {Fore.CYAN}handshake/encryption/wep{Fore.RED}                   | [#] {Fore.CYAN}for handshake capture WEP encryption you can capture{Fore.RED}
[#] {Fore.CYAN}handshake/encryption/wpa{Fore.RED}                   | [#] {Fore.CYAN}for handshake capture WPA encryption you can capture{Fore.RED}
[#] {Fore.CYAN}sniff/my/device{Fore.RED}                            | [#] {Fore.CYAN}for sniff your device{Fore.RED} 
[#] {Fore.CYAN}network/scan/devices{Fore.RED}                       | [#] {Fore.CYAN}to see all device in your network ( IP, MAC, name Device ){Fore.RED}
[#] {Fore.CYAN}port/scan{Fore.RED}                                  | [#] {Fore.CYAN}port scan any IP{Fore.RED}
[#] {Fore.CYAN}fake/wifi{Fore.RED}                                  | [#] {Fore.CYAN}to make fake wifi{Fore.RED} 
[#] {Fore.CYAN}fake/wifi/random{Fore.RED}                           | [#] {Fore.CYAN}to make fakes wifi random name{Fore.RED}
[#] {Fore.CYAN}password/wifi{Fore.RED}                              | [#] {Fore.CYAN}to see password your network{Fore.RED}
[#] {Fore.CYAN}deauth/attack/wifi/aireplay-ng{Fore.RED}             | [#] {Fore.CYAN}deauth attack using aireplay-ng{Fore.RED}
[#] {Fore.CYAN}deauth/attack/wifi/mdk3{Fore.RED}                    | [#] {Fore.CYAN}deauth attack using mdk3{Fore.RED}
[#] {Fore.CYAN}deauth/attack/wifi/one/device/aireplay-ng{Fore.RED}  | [#] {Fore.CYAN}deauth attack for one device{Fore.RED} 
[#] {Fore.CYAN}arp/spoofing/attack{Fore.RED}                        | [#] {Fore.CYAN}arp spoofing attack in your network{Fore.RED} 
[#] {Fore.CYAN}mac/spoofing/attack{Fore.RED}                        | [#] {Fore.CYAN}mac spoofing attack for any device{Fore.RED} 
[#] {Fore.CYAN}banner{Fore.RED}                                     | [#] {Fore.CYAN}change banner{Fore.RED}
[#] {Fore.CYAN}exit{Fore.RED}                                       | [#] {Fore.CYAN}exit from tool{Fore.RED} 
[#] {Fore.CYAN}clear{Fore.RED}                                      | [#] {Fore.CYAN}clear screen{Fore.RED} 

{Fore.RED}Ex :{Fore.CYAN} use port/scan

{Fore.RED}to run shell command :{Fore.CYAN} prepend the command with " ! " 

{Fore.RED}info :{Fore.CYAN} 

    this tool for network penetration test ..
    it"s esay to use ..
    Do not use the tool for anything illegal ..
    
    Make by --> d5tr
    Team --> zero one         
   
        ''')
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
        print(f'{Fore.RED}Unknow Command !{Fore.WHITE}')
        d5tr()
# start the tool ...
d5tr()
