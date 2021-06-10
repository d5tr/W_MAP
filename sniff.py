#import scapy.all as scapy
from scapy.layers import http
from colorama import Fore
from scapy.all import *
#   interface = name WI-FI like ( wlna0 )
def sniffer(interface):
    print('--------------------')
    print(f'---{Fore.RED}Sniffing HTTP start{Fore.WHITE}---')
    print('--------------------')
    # sniff | iface = interface | store = do you want save result ? answer no ( false ) | prn = if i see packet .. do you want Transfer to ? = proc is name def we want seve in
    sniff(iface=interface, store=False, prn=proc)


def proc(packet):
    # if packet http print the packet
    # haslayer = OSI layer طبقه الشبكه
    # http.HTTPRequest = http request
    if packet.haslayer(http.HTTPRequest):
                      # print host url   |          print path url
        print(f'{Fore.BLUE}[{Fore.GREEN}+{Fore.BLUE}]{Fore.RED}[FROM : {packet[IP].src}]{Fore.WHITE}',packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path )

        # if packet in input like ( login & singup & etc ...)
        if packet.haslayer(Raw):
            # save in file name requset
            request = packet[Raw].load
            # and print the request
            print(f'{Fore.BLUE}[{Fore.GREEN}+{Fore.BLUE}]{Fore.RED} [FROM : {packet[IP].src}]{Fore.WHITE}  ', request)


sniffer('wlan0')