#!/bin/bash

WHO=$(whoami)

if [ $WHO == root ]
then

cd /root && rm -rf W_MAP
cd /bin && rm W-MAP

echo 'Done uninstall ...'

else
then

echo 'you must be root'
echo 'use sudo '

fi
