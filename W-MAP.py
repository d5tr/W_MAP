from banners import ban, ban_handshake , ban_deauth_attack
from sniff.Sniffing import *
from rest_of_tools.network_scan import *
from rest_of_tools.port_scanner import *
import sys
from wlan import interfaces
from banners.ban_wmap import *
ban_wmap()
# if root or not :
root = os.getuid()

time.sleep(1)

if root == 0:
    pass

else:
    print(f'[{Fore.RED}!!{Fore.WHITE}] Error : you must be root !! \n use " sudo " and type password next step run tool ')
    exit()

os.system('clear')

def zero_one(): # banner ...
    ban_handshake.BH()

def d5tr(): # banaer ...
    ban.bans()



    # for choose 

    what = int(input(f'\n\n{Fore.WHITE}[{Fore.CYAN}?{Fore.WHITE}] Choose number : '))

    if what == 1 :
        os.system('clear')
        zero_one()

        what_hand = int(input(f'[{Fore.CYAN}?{Fore.WHITE}] Choose number : '))

        if what_hand == 1 :
            interfaces()

            os.system('bash Handshake/handshake_all.sh ')


            if KeyboardInterrupt :
                interfaces()
                Monitor = input(f'[{Fore.CYAN}?{Fore.WHITE}] Enter name interface to disable Monitor mode : ')
                os.system(f'airmon-ng stop {Monitor}')
                print('\nclear now ...')
                time.sleep(0.5)
                os.system('clear')
                d5tr()


        elif what_hand == 2 :
            interfaces()


            try:

                os.system('bash Handshake/handshake_wep.sh')

                if KeyboardInterrupt:
                    interfaces()
                    Monitor = input(f'[{Fore.CYAN}?{Fore.WHITE}] Enter name interface to disable Monitor mode : ')
                    os.system(f'airmon-ng stop {Monitor}')
                    print('\nclear now ...')
                    time.sleep(0.5)
                    os.system('clear')
                    d5tr()

            except:
                print('Error can"t do it ...')
                time.sleep(1)
                d5tr()

        elif what_hand == 3 :
            interfaces()

            try:
                os.system('bash Handshake/handshake_wpa.sh')
                if KeyboardInterrupt:
                    interfaces()
                    Monitor = input(f'[{Fore.CYAN}?{Fore.WHITE}] Enter name interface to disable Monitor mode : ')
                    os.system(f'airmon-ng stop {Monitor}')
                    print('\nclear now ...')
                    time.sleep(0.5)
                    os.system('clear')
                    d5tr()
            except:
                print('Erorr can"t do it ...')
                time.sleep(1)
                d5tr()

        elif what_hand == 99:
            os.system('clear')
            d5tr()




#-----------------------------------------------------------------------------#

    elif what == 2:  # sniff wifi
        interfaces()

        wlans = input(f'[{Fore.CYAN}?{Fore.WHITE}] Enter name interface :')

        SNIFFING(wlans)

# -----------------------------------------------------------------------------#

        if KeyboardInterrupt:
            print('clear now ...')
            time.sleep(0.5)
            os.system('clear')
            d5tr()  # back

    elif what == 3: # Network scan

        IP_network = input(f'[{Fore.CYAN}?{Fore.WHITE}] Enter IP network :')
        the_ip = IP_network+'/24'
        Network_Scan(the_ip)

        if KeyboardInterrupt:

            print('\nclear now ...')
            time.sleep(0.5)
            os.system('clear')
            d5tr()

# -----------------------------------------------------------------------------#

    elif what == 4:  # port scan
        HOST = input(f'[{Fore.CYAN}?{Fore.WHITE}] Enter IP target : ')

        try:
            Port_scan(HOST)
        except:
            print("Error : can't scan ip or wifi can't scan !!")
            time.sleep(1)
            d5tr()

        if KeyboardInterrupt:

            print('\nclear now ...')
            time.sleep(0.5)
            os.system('clear')
            d5tr()

# -----------------------------------------------------------------------------#

    elif what == 5: # fake WI-FI

        interfaces()

        try:
            print('\n')
            os.system('bash rest_of_tools/Fake_wifi.sh')

            if KeyboardInterrupt :
                interfaces()
                Monitor = input(f'[{Fore.CYAN}?{Fore.WHITE}] Enter name interface to disable Monitor mode : ')
                os.system(f'airmon-ng stop {Monitor}')
                print('\nclear now ...')
                time.sleep(0.5)
                os.system('clear')
                d5tr()

        except:
            print('Error can"t do it ...')
            time.sleep(1)
            os.system('clear')
            d5tr()


# -----------------------------------------------------------------------------#


    elif what == 6:  # password wifi
        os.system('bash rest_of_tools/password_wifi.sh')
        if KeyboardInterrupt:
            print('clear now ...')
            time.sleep(0.5)
            os.system('clear')
            d5tr()

    elif what == 7: # Death attack one device
        os.system('clear')
        ban_deauth_attack.ban_death_attack()

        choose_daeuth = int(input(f'[{Fore.CYAN}?{Fore.WHITE}] Choose number : '))

        if choose_daeuth == 1 :
            interfaces()

            os.system('bash Deauth_attack/Deauth_attack_WIFI_aireplay.sh')

            if KeyboardInterrupt:
                interfaces()
                Monitor = input(f'[{Fore.CYAN}?{Fore.WHITE}] Enter name interface to disable Monitor mode : ')
                os.system(f'airmon-ng stop {Monitor}')
                print('clear now ...')
                time.sleep(0.5)
                os.system('clear')
                d5tr()

        elif choose_daeuth == 2 :
            interfaces()

            os.system('bash Deauth_attack/Deauth_attack_WIFI_mdk3.sh')

            if KeyboardInterrupt:
                interfaces()
                Monitor = input(f'[{Fore.CYAN}?{Fore.WHITE}] Enter name interface to disable Monitor mode : ')
                os.system(f'airmon-ng stop {Monitor}')
                print('clear now ...')
                time.sleep(0.5)
                os.system('clear')
                d5tr()

        elif choose_daeuth == 3 :
            interfaces()

            os.system('bash Deauth_attack/Deauth_one_device_aireplay.sh')
            if KeyboardInterrupt:
                interfaces()
                Monitor = input(f'[{Fore.CYAN}?{Fore.WHITE}] Enter name interface to disable Monitor mode : ')
                os.system(f'airmon-ng stop {Monitor}')
                print('clear now ...')
                time.sleep(0.5)
                os.system('clear')
                d5tr()

        elif choose_daeuth == 99 :
            d5tr()

    elif what == 8: # ARP spoofing

        os.system('xterm -hold -e python3 ARP_attack.py & xterm -hold -e python3 sniff/sniff_http.py & xterm -hold -e python3 sniff/sniff_for_ARP.py')
        if KeyboardInterrupt :
            print('clear now ...')
            time.sleep(0.5)
            os.system('clear')
            d5tr()

    elif what == 9 :
        os.system('clear')
        d5tr()


    elif KeyboardInterrupt :
        print('\nExit ...')
        sys.exit()

    elif what == 99:  # exit !!
        print('\nGOOD BAY ...')
        sys.exit()



# start the tool ...
d5tr()
