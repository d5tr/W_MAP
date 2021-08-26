from scapy.all import *  # for sniffing_and_spoofing wifi ...
from Core.colors import *  # for color ...
from time import sleep
from scapy.all import ARP , Ether, srp
import netifaces

def interfaces():
    x = netifaces.interfaces() # all interface

    print(f'[{Cyan}?{White}] Choose :')
    print('\n')
    for i in x:
        if i != 'lo': # we want interface without lo

            print(f' - {Green}{i}{White}')

    print('\n')

interfaces()


wlan_is = str(input(f'[{Cyan}?{White}] Enter name interface :'))

def analyzer(pkt):  # for TCP ...
    if pkt.haslayer(TCP):
        print("===============================")
        print(f"{Red}<<<  TCP  >>>")
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
        print(f"{Cyan}<<<  UDP  >>>")
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

print(f"*********{Red}START{White}*********")
sniff(iface=wlan_is, prn=analyzer)