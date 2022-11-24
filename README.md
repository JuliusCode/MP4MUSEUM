# MP4MUSEUM
MP4MUSEUM.org Media Player

Version 5.5 is out! 

- gpio input filter
- new loop trigger


__visit [mp4museum.org](http://mp4museum.org) for more information__

_Or an answer may reside in the [closed issues](https://github.com/JuliusCode/MP4MUSEUM/issues?q=is%3Aissue+is%3Aclosed)_



For the Python script to run on a fresh [Raspberry Pi OS Lite](https://www.raspberrypi.com/software/operating-systems/) you need to install some things

`sudo apt-get install vlc python3-pip`

`pip3 install python-vlc RPi.GPIO`

if you are using the distributed image, /etc/rc.local will run start.sh which will run mp4museum.py
