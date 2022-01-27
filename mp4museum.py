# mp4museum v5 - jan 2022

# (c) julius schmiedel - http://mp4museum.org

import time, vlc, os, sys, glob

from subprocess import Popen, PIPE
import RPi.GPIO as GPIO

FNULL = open(os.devnull, "w")

# read audio device config
audiodevice = "0"

if os.path.isfile('/boot/alsa.txt'):
    f = open('/boot/alsa.txt', 'r')
    audiodevice = f.read(1)

# setup GPIO pin
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

# functions to be called by event listener
def buttonPause(channel):
    player.pause()

def buttonNext(channel):
    player.stop()

# play media
def vlc_play(source):
    if("loop.mp4" in source):
        vlc_instance = vlc.Instance('--input-repeat=999999999 -q -A alsa --alsa-audio-device hw:' + audiodevice)
    else:
        vlc_instance = vlc.Instance('-q -A alsa --alsa-audio-device hw:'+ audiodevice)
    global player
    player = vlc_instance.media_player_new()
    media = vlc_instance.media_new(source)
    player.set_media(media)
    player.play()
    time.sleep(1)
    current_state = player.get_state()
    while current_state == 3 or current_state == 4:
        time.sleep(.1)
        current_state = player.get_state()
    media.release()
    player.release()

# start player twice to make sure it is working
# seems weird but works
vlc_play("/home/pi/mp4museum-boot.mp4")
vlc_play("/home/pi/mp4museum-boot.mp4")

# please do not remove my logo screen
vlc_play("/home/pi/mp4museum.mp4")

# add event listener
GPIO.add_event_detect(11, GPIO.FALLING, callback = buttonPause, bouncetime = 234)
GPIO.add_event_detect(13, GPIO.FALLING, callback = buttonNext, bouncetime = 1234)

# the loop
while(1):
    for files in sorted(glob.glob(r'/media/*/*.*')):
        vlc_play(files)
