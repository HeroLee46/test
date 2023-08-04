#!/bin/bash

loop=0
pass=0
fail=0

timedatectl set-timezone "Asia/Taipei"

# mkdir -p /var/log/MFG/
# mkdir -p /var/log/MFG/pi_ping_wlan0_gw/
# file=/var/log/MFG/pi_ping_wlan0_gw/pi_ping_wlan0_gw_$(date +"%Y%m%d_%H%M%S").log
# touch $file

while [ $loop -lt 5 ]
do
    echo "*****************"
	echo "*****************" >> $file
	((loop++ ))
	echo "loop: $loop"
	echo "loop: $loop" >> $file
    currenttime=$(date)
	echo "$currenttime"
	echo "$currenttime" >> $file
    gw=$(ip route show | grep default | grep wlan0 | cut -d' ' -f 3)
    echo "wlan0 gateway: $gw"
	echo "wlan0 gateway: $gw" >> $file
    printf "\n"
    ping -c 1 -w 1 $gw && result=0 || result=1
    printf "\n"
    if [ "$result" -eq "0" ]; then
         echo "** PASS, Machine is UP!"
		 (( pass++ ))
		 echo "** PASS, Machine is UP!" >> $file
    else
         echo "** FAIL, Machine is DOWN!"
		 (( fail++ ))
		 echo "** FAIL, Machine is DOWN!" >> $file
    fi

	echo "** total PASS: $pass" >> $file
	echo "** total FAIL: $fail" >> $file
	echo "*****************"
	echo "*****************" >> $file
    sleep 3

done
