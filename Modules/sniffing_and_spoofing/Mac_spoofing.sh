#!/bin/bash

echo ' '
Interface=$1

read -p '[?] Enter MAC to spoofing : ' MAC

echo ' '
ifconfig $Interface down

macchanger -m $MAC $Interface

ifconfig $Interface up

echo ' '
read -p 'press Enter to continue ... ' CON

