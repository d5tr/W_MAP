from scapy.all import *
from colorama import Fore


def SNIFFING(wlan):  # for TCP ...
    def analyzer(pkt):
        if pkt.haslayer(TCP):
            print("===============================")
            print(Fore.RED + "<<<  TCP  >>>")
            src_ip = pkt[IP].src  # IP sender
            dst_ip = pkt[IP].dst  # IP server
            mac_src = pkt.src  # MAC sender
            mac_dst = pkt.dst  # MAC server
            src_port = pkt.sport  # PORT sender
            dst_port = pkt.dport  # PORT server

            print(Fore.GREEN + "[MAC SRC FROM] = " + mac_src)
            print(Fore.GREEN + "[MAC DST TO] = " + mac_dst)
            print("                      ")
            print(Fore.GREEN + "[SRC IP FROM] = " + src_ip)
            print(Fore.GREEN + "[DST IP TO] = " + dst_ip)
            print("                       ")
            print(Fore.GREEN + "[SRC PORT FROM = " + str(src_port))
            print(Fore.GREEN + "[DST PORT FROM] = " + str(dst_port))

            if pkt.haslayer(Raw):
                print(pkt[Raw].load)  # for print the pkt !!
            print(Fore.WHITE + "packet_size = " + str(len(pkt[TCP])))
            print("================================")
        elif pkt.haslayer(UDP):  # for UDP ...
            print("================================")
            print(Fore.LIGHTBLUE_EX + "<<<  UDP  >>>")
            src_ip = pkt[IP].src
            dst_ip = pkt[IP].dst
            mac_src = pkt.src
            mac_dst = pkt.dst
            src_port = pkt.sport  # like TCP in up
            dst_port = pkt.dport
            print(Fore.RED + "[MAC SRC FROM] = " + mac_src)
            print(Fore.RED + "[MAC DST TO] =" + mac_dst)
            print("                   ")
            print(Fore.RED + "[SRC IP FROM] = " + src_ip)
            print(Fore.RED + "[DST IP TO] = " + dst_ip)
            print("                     ")
            print(Fore.RED + "[SRC PORT FROM] = " + str(src_port))
            print(Fore.RED + "[DST PORT TO] = " + str(dst_port))
            if pkt.haslayer(Raw):
                print(pkt[Raw].load)
            print(Fore.WHITE + "packet_size = " + str(len(pkt[UDP])))
            print("===============================")


    print("*********START*********")
    sniff(iface=wlan, prn=analyzer)