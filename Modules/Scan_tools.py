from scapy.all import *
import requests
import time
import socket
from Core.colors import *
from wifi import Cell
import os

class Scan_tools :

    

    # Port Scanner  
    @classmethod
    def Port_scanner(self, Host, Ports):

        if Ports == '':

            Ports = 65535 
        else:
            pass


        numberx = 0
        print('\n')
        
        for port in range(1, int(Ports)):
            # we want use IPV4
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # time to wait response 
            socket.setdefaulttimeout(1)

            # connect with host and port 
            result = s.connect_ex((Host, port))
            numberx = numberx + 1
            print(f'\r ports scan : {numberx}', end="")
            if result == 0:

                name_port = socket.getservbyport(port)  # get name port
                print(f"[{Green}+{White}] Port {port} / {name_port} Open ")
                print(f'{Cyan}------------------------------{White}')

    # Network scanner 
    @classmethod
    def Network_Scanner(self, ip):
        exitx = []

        print('\n')
        print(f'{Cyan}IP\t\t\t\t\tMAC\t\t\t\t\tDEVICE{White}')
        print(f'{Red}-----------------------------------------------------------------------------------------{White}')
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
                    URL = 'https://api.macvendors.com/{}'.format(i['mac'])
                    time.sleep(2)
                    REQ = requests.get(URL).text
                    Clan = REQ.replace('{"errors":{"detail":"', '')
                    Clan_Plus = Clan.replace('"}}', '')
                    RENAME = Clan_Plus.replace('Not Found', 'Unknown')
                    print('{}\t\t\t{}\t\t\t{}'.format(i['ip'], i['mac'], RENAME))
                    exitx.append(i['mac'])

    @classmethod
    def Scan_WIFI(self, Interface):
        
        print(f'''
====================================================================
    {Cyan}BSSID{White}       |   {Cyan}PWD{White}   |   {Cyan}Encryption{White}   |   {Cyan}Ch{White}   |    {Cyan}SSID{White}                    
====================================================================
        ''')
        # Make file
        with open('Ss.txt', 'a') as hack :
                hack.write('none'+'\n')

        
        while True:
            # Use this interface
            net = Cell.all(Interface)


            for x in net :
                # read file
                READ = open('Ss.txt', 'r').read().strip()




                if x.ssid in READ :
                        pass

                elif x.ssid not in READ :

                        print(f'''
{Green}{x.address}    {x.signal}         {x.encryption_type}           {x.channel}       {x.ssid}{White}
====================================================================
                                ''')

                elif KeyboardInterrupt :
                    os.system('rm Ss.txt')
                with open('Ss.txt', 'a') as Save :
                    Save.write(x.ssid+'\n')

