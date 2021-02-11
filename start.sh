#!/bin/sh

sleep 7
setterm -cursor off
sh -c "TERM=linux setterm -foreground black -clear all >/dev/tty0"

python /home/pi/mp4museum.py
