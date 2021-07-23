#!/bin/bash

red="\e[0;91m"
blue="\e[0;94m"
reset="\e[0m"

echo  ' '
read -p "[$(echo -e $blue"?"$reset)] Enter name interface : " INTERFACE
MON=mon
airmon-ng start $INTERFACE

read -p "[$(echo -e $blue"?"$reset)] Enter name file is in it name WI-FI : " FILE

echo -e "$blue ----------START-FAKE-WI-FI----------- $reset"

mdk3 $INTERFACE$MON b -c 1 -f $FILE

airmon-ng stop $INTERFACE$MON

