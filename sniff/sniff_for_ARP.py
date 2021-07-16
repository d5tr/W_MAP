from scapy.all import *  # for sniff wifi ...
from colorama import Fore  # for color ...
from time import sleep
from scapy.all import ARP , Ether, srp

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

print(f"*********{Fore.RED}START{Fore.WHITE}*********")
sniff(iface=wlan_is, prn=analyzer)