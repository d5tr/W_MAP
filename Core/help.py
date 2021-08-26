from Core.colors import *

def Help():
    print(f'''
    
    {Red}
    ==============================================================================================
    |    {Cyan}Name                                                Description{Red}                         |       
    ==============================================================================================
                                                   |                                          
    [#] {Cyan}handshake/encryption/all{Red}                   | [#] {Cyan}for handshake capture all encryption you can capture{Red}
    [#] {Cyan}handshake/encryption/wep{Red}                   | [#] {Cyan}for handshake capture WEP encryption you can capture{Red}
    [#] {Cyan}handshake/encryption/wpa{Red}                   | [#] {Cyan}for handshake capture WPA encryption you can capture{Red}
    [#] {Cyan}sniff/my/device{Red}                            | [#] {Cyan}for sniff your device{Red} 
    [#] {Cyan}network/scan/devices{Red}                       | [#] {Cyan}to see all device in your network ( IP, MAC, name Device ){Red}
    [#] {Cyan}port/scan{Red}                                  | [#] {Cyan}port scan any IP{Red}
    [#] {Cyan}scan/wifi{Red}                                  | [#] {Cyan}this for scan WI-FI around you{Red}
    [#] {Cyan}fake/wifi{Red}                                  | [#] {Cyan}to make fake wifi{Red} 
    [#] {Cyan}fake/wifi/random{Red}                           | [#] {Cyan}to make fakes wifi random name{Red}
    [#] {Cyan}password/wifi{Red}                              | [#] {Cyan}to see password your network{Red}
    [#] {Cyan}deauth/attack/wifi/aireplay-ng{Red}             | [#] {Cyan}deauth attack using aireplay-ng{Red}
    [#] {Cyan}deauth/attack/wifi/mdk3{Red}                    | [#] {Cyan}deauth attack using mdk3{Red}
    [#] {Cyan}deauth/attack/wifi/one/device/aireplay-ng{Red}  | [#] {Cyan}deauth attack for one device{Red} 
    [#] {Cyan}arp/spoofing/attack{Red}                        | [#] {Cyan}arp spoofing attack in your network with xterm to see attack{Red}
    [#] {Cyan}arp/spoofing/attack/wireshark{Red}              | [#] {Cyan}arp spoofing attack in your network ( see packet in wireshark ){Red}  
    [#] {Cyan}mac/spoofing/attack{Red}                        | [#] {Cyan}mac spoofing attack for any device{Red} 
    [#] {Cyan}banner{Red}                                     | [#] {Cyan}change banner{Red}
    [#] {Cyan}exit{Red}                                       | [#] {Cyan}exit from tool{Red} 
    [#] {Cyan}clear{Red}                                      | [#] {Cyan}clear screen{Red} 

    {Red}Ex :{Cyan} use port/scan

    {Red}to run shell command :{Cyan} prepend the command with " ! " 

    {Red}info :{Cyan} 

    this tool for network penetration test ..
    it"s esay to use ..
    Do not use the tool for anything illegal ..

    Make by --> d5tr
    Team --> zero one         

''')