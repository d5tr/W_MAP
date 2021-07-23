from scapy.all import *
from colorama import Fore
import requests
import time

def Network_Scan(ip):
    exitx = []

    print('\n')
    print(f'{Fore.CYAN}IP\t\t\t\t\tMAC\t\t\t\t\tDEVICE{Fore.WHITE}')
    print(f'{Fore.RED}-----------------------------------------------------------------------------------------{Fore.WHITE}')
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

