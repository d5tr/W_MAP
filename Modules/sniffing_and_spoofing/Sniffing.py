from scapy.all import *
from Core.colors import *


def SNIFFING(wlan):  # for TCP ...
    def analyzer(pkt):
        if pkt.haslayer(TCP):
            print("===============================")
            print(f"{Cyan}<<<  TCP  >>>")
            src_ip = pkt[IP].src  # IP sender
            dst_ip = pkt[IP].dst  # IP server
            mac_src = pkt.src  # MAC sender
            mac_dst = pkt.dst  # MAC server
            src_port = pkt.sport  # PORT sender
            dst_port = pkt.dport  # PORT server

            print(f"{Green}[MAC SRC FROM] = " + mac_src)
            print(f"{Green}[MAC DST TO] = " + mac_dst)
            print("                      ")
            print(f"{Green}[SRC IP FROM] = " + src_ip)
            print(f"{Green}[DST IP TO] = " + dst_ip)
            print("                       ")
            print(f"{Green}[SRC PORT FROM = " + str(src_port))
            print(f"{Green}[DST PORT FROM] = " + str(dst_port))

            if pkt.haslayer(Raw):
                print(pkt[Raw].load)  # for print the pkt !!
            print(f"{White}packet_size = " + str(len(pkt[TCP])))
            print("================================")
        elif pkt.haslayer(UDP):  # for UDP ...
            print("================================")
            print(f"{Cyan}<<<  UDP  >>>")
            src_ip = pkt[IP].src
            dst_ip = pkt[IP].dst
            mac_src = pkt.src
            mac_dst = pkt.dst
            src_port = pkt.sport  # like TCP in up
            dst_port = pkt.dport
            print(f"{Red}[MAC SRC FROM] = " + mac_src)
            print(f"{Red}[MAC DST TO] =" + mac_dst)
            print("                   ")
            print(f"{Red}[SRC IP FROM] = " + src_ip)
            print(f"{Red}[DST IP TO] = " + dst_ip)
            print("                     ")
            print(f"{Red}[SRC PORT FROM] = " + str(src_port))
            print(f"{Red}[DST PORT TO] = " + str(dst_port))
            if pkt.haslayer(Raw):
                print(pkt[Raw].load)
            print(f"{White}packet_size = " + str(len(pkt[UDP])))
            print("===============================")


    print("*********START*********")
    sniff(iface=wlan, prn=analyzer)