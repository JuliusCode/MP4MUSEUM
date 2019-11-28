#!/usr/bin/python

# mp4museum.org by julius schmiedel 2019

import os
import sys
import glob
from subprocess import Popen, PIPE
import RPi.GPIO as GPIO

FNULL = open(os.devnull, "w")

# setup GPIO pin
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

# functions to be called by event listener
def buttonPause(channel):
	player.stdin.write("p")

def buttonNext(channel):
	player.stdin.write("q")

# add event listener
GPIO.add_event_detect(11, GPIO.FALLING, callback = buttonPause, bouncetime = 234)
GPIO.add_event_detect(13, GPIO.FALLING, callback = buttonNext, bouncetime = 1234)

# please do not remove my logo screen
player = Popen(['omxplayer', '--adev', 'both', '/home/pi/mp4museum.mp4'],stdin=PIPE,stdout=FNULL)
player.wait()

# the loop
while(1):
	for files in sorted(glob.glob(r'/media/*/*.mp4')):
		player = Popen(['omxplayer','--adev', 'both',files],stdin=PIPE,stdout=FNULL)
		player.wait()
