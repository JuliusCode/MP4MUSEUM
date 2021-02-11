# mp4museum v5 beta 2 - feb 2021

import time, vlc, os, sys, glob

from subprocess import Popen, PIPE
import RPi.GPIO as GPIO

FNULL = open(os.devnull, "w")

# setup GPIO pin
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

# functions to be called by event listener
def buttonPause(channel):
    player.pause()

def buttonNext(channel):
    player.stop()

# play a video
def video(source):
    vlc_instance = vlc.Instance()
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

# please do not remove my logo screen
video("/home/pi/mp4museum5beta.mp4")

# add event listener
GPIO.add_event_detect(11, GPIO.FALLING, callback = buttonPause, bouncetime = 234)
GPIO.add_event_detect(13, GPIO.FALLING, callback = buttonNext, bouncetime = 1234)

# the loop
while(1):
    for files in sorted(glob.glob(r'/media/*/*.*')):
        video(files)
