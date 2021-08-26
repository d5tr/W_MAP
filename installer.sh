#!/bin/bash


chmod +x rest_of_tools/password_wifi.sh

chmod +x Deauth_attack/Deauth_attack_WIFI_aireplay.sh

chmod +x Deauth_attack/Deauth_attack_WIFI_mdk3.sh

chmod +x Deauth_attack/Deauth_one_device_aireplay.sh

chmod +x Handshake/handshake_all.sh

chmod +x Handshake/handshake_wep.sh

chmod +x Handshake/handshake_wpa.sh

chmod +x sniffing_and_spoofing/Mac_spoofing.sh

chmod +x uninstall.sh

chmod +x W-MAP.sh

python3 setup.py

apt-get install xterm

apt-get install macchanger

pip3 install time

pip3 install socket

python3 -m pip install scapy

pip3 install subprocess

pip3 install colorama

pip3 install inquirer

python3 -m pip install scapy

pip3 install netifaces

pip3 install requests

python3 -m pip install wifi

pip3 install wifi


echo "Done download ..."

sleep 2
clear

echo 'type > W-MAP < to start tool'
