#!/bin/bash

if [[ $(/usr/bin/id -u) -ne 0 ]]; then
    echo "Please run as root"
    exit
fi

DIR="/home/pi/ledcubes/services"
services=("ledcubes.service", "wifi_setup.service")

for s in ${services[@]}; do
    FILE="$DIR/$s"

    echo "Copying" $FILE "to /etc/systemd/system"
    sudo cp $FILE /etc/systemd/system

    echo "Enabling" $s
    systemctl enable $s
done


echo "Reloading Daemon"
systemctl daemon-reload

for s in ${services[@]}; do
    echo "Restarting" $s 
    systemctl restart $s
done
