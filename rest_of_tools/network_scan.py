from scapy.all import *
from colorama import Fore


def Network_Scan(ip):
    exitx = []


    print(f'{Fore.CYAN}IP\t\t\t\t\tMAC{Fore.WHITE}')
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