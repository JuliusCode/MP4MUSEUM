#!/bin/sh

setterm -cursor off
sh -c "TERM=linux setterm -foreground black -clear all >/dev/tty0"
clear
python /home/pi/mp4museum.py > /dev/null 2>&1
