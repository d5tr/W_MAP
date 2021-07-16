#!/bin/bash

red="\e[0;91m"
blue="\e[0;94m"
reset="\e[0m"


read -p "[?] Enter name interface : " INTERFACE
MON=mon
airmon-ng start $INTERFACE

echo -e "$red Plz make sure you have file like [ wifi.lst ] ... ! $reset"
sleep 3

read -p "[?] Enter name file is in it name WI-FI : " FILE

echo -e "$blue ----------START-FAKE-WI-FI----------- $reset"

mdk3 $INTERFACE$MON b -c 1 -f $FILE

airmon-ng stop $INTERFACE$MON

