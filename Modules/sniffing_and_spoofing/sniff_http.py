#import scapy.all as scapy
from scapy.layers import http
from Core.colors import *
from scapy.all import *
import netifaces
#   interface = name WI-FI like ( wlna0 )


def interfaces():
    x = netifaces.interfaces() # all interface

    print(f'[{Cyan}?{White}] Choose :')
    print('\n')
    for i in x:
        if i != 'lo': # we want interface without lo

            print(f' - {Green}{i}{White}')

    print('\n')
interfaces()

def sniffer(interface):
    print('--------------------')
    print(f'---{Red}Sniffing HTTP start{White}---')
    print('--------------------')
    # sniffing_and_spoofing | iface = interface | store = do you want save result ? answer no ( false ) | prn = if i see packet .. do you want Transfer to ? = proc is name def we want seve in
    sniff(iface=interface, store=False, prn=proc)


def proc(packet):
    # if packet http print the packet
    # haslayer = OSI layer طبقه الشبكه
    # http.HTTPRequest = http request
    if packet.haslayer(http.HTTPRequest):
                      # print host url   |          print path url
        print(f'{Cyan}[{Green}+{Cyan}]{Red}[FROM : {packet[IP].src}]{White}',packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path )

        # if packet in input like ( login & singup & etc ...)
        if packet.haslayer(Raw):
            # save in file name requset
            request = packet[Raw].load
            # and print the request
            print(f'{Cyan}[{Green}+{Cyan}]{Red} [FROM : {packet[IP].src}]{White}  ', request)


WLAN = str(input(f'[{Cyan}?{White}] Enter name interface :'))

sniffer(WLAN)