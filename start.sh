#!/bin/sh

setterm -cursor off
sh -c "TERM=linux setterm -foreground black -clear all >/dev/tty0"
clear
while true
do
	python /home/pi/mp4museum.py > /tmp/mp4museum.log 2>&1
	clear
done
