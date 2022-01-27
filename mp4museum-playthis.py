#!/usr/bin/python

# mp4museum.org by julius schmiedel
# playthis version
#
# all files looped, GPIO triggered playback
#
# http://mp4museum.org/mp4museum-v4.20.img.zip
# take a v4 image and replace its python script with this
# does not work with v5 or newer!
#
# files must be located in /playthis directory
# files must be named 1.mp4, 2.mp4 etc 
# all files and the directory must be in lowercase
#
# supports only one stick
# (or at least insert playthis stick first)

import os
import sys
import glob
from subprocess import Popen, PIPE
import RPi.GPIO as GPIO

FNULL = open(os.devnull, "w")

playthis = 0

# setup GPIO pin
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(11, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(12, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(15, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(19, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(21, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

# functions to be called by event listener
def playN1(channel):
	global playthis
	if ( playthis == 1 ):
		playthis = 0
		poll = player.poll()
		if ( poll == None ):
			player.stdin.write("q")
	else:
		playthis = 1
		poll = player.poll()
		if ( poll == None ):
			player.stdin.write("q")

def playN2(channel):
	global playthis
	if ( playthis == 2 ):
		playthis = 0
		poll = player.poll()
		if ( poll == None ):
			player.stdin.write("q")
	else:
		playthis = 2
		poll = player.poll()
		if ( poll == None ):
			player.stdin.write("q")

def playN3(channel):
	global playthis
	if ( playthis == 3 ):
		playthis = 0
		poll = player.poll()
		if ( poll == None ):
			player.stdin.write("q")
	else:
		playthis = 3
		poll = player.poll()
		if ( poll == None ):
			player.stdin.write("q")

def playN4(channel):
	global playthis
	if ( playthis == 4 ):
		playthis = 0
		poll = player.poll()
		if ( poll == None ):
			player.stdin.write("q")
	else:
		playthis = 4
		poll = player.poll()
		if ( poll == None ):
			player.stdin.write("q")

def playN5(channel):
	global playthis
	if ( playthis == 5 ):
		playthis = 0
		poll = player.poll()
		if ( poll == None ):
			player.stdin.write("q")
	else:
		playthis = 5
		poll = player.poll()
		if ( poll == None ):
			player.stdin.write("q")

def playN6(channel):
	global playthis
	if ( playthis == 6 ):
		playthis = 0
		poll = player.poll()
		if ( poll == None ):
			player.stdin.write("q")
	else:
		playthis = 6
		poll = player.poll()
		if ( poll == None ):
			player.stdin.write("q")

def playN7(channel):
	global playthis
	if ( playthis == 7 ):
		playthis = 0
		poll = player.poll()
		if ( poll == None ):
			player.stdin.write("q")
	else:
		playthis = 7
		poll = player.poll()
		if ( poll == None ):
			player.stdin.write("q")

def playN8(channel):
	global playthis
	if ( playthis == 8 ):
		playthis = 0
		poll = player.poll()
		if ( poll == None ):
			player.stdin.write("q")
	else:
		playthis = 8
		poll = player.poll()
		if ( poll == None ):
			player.stdin.write("q")

def playN9(channel):
	global playthis
	if ( playthis == 9 ):
		playthis = 0
		poll = player.poll()
		if ( poll == None ):
			player.stdin.write("q")
	else:
		playthis = 9
		poll = player.poll()
		if ( poll == None ):
			player.stdin.write("q")

def playN10(channel):
	global playthis
	if ( playthis == 10 ):
		playthis = 0
		poll = player.poll()
		if ( poll == None ):
			player.stdin.write("q")
	else:
		playthis = 10
		poll = player.poll()
		if ( poll == None ):
			player.stdin.write("q")

# add event listener

GPIO.add_event_detect(7, GPIO.FALLING, callback=playN1, bouncetime=1234)
GPIO.add_event_detect(11, GPIO.FALLING, callback=playN2, bouncetime=1234)
GPIO.add_event_detect(12, GPIO.FALLING, callback=playN3, bouncetime=1234)
GPIO.add_event_detect(13, GPIO.FALLING, callback=playN4, bouncetime=1234)
GPIO.add_event_detect(15, GPIO.FALLING, callback=playN5, bouncetime=1234)
GPIO.add_event_detect(16, GPIO.FALLING, callback=playN6, bouncetime=1234)
GPIO.add_event_detect(18, GPIO.FALLING, callback=playN7, bouncetime=1234)
GPIO.add_event_detect(19, GPIO.FALLING, callback=playN8, bouncetime=1234)
GPIO.add_event_detect(21, GPIO.FALLING, callback=playN9, bouncetime=1234)
GPIO.add_event_detect(22, GPIO.FALLING, callback=playN10, bouncetime=1234)


# please do not remove my logo screen
player = Popen(['omxplayer', '--adev', 'both', '/home/pi/mp4museum.mp4'],stdin=PIPE,stdout=FNULL)
player.wait()

# the loop
while(1):
	for files in sorted(glob.glob(r'/media/*/*.mp4')):

		if ( playthis == 1 ):
			player = Popen(['omxplayer','--adev', 'both','/media/usb/playthis/1.mp4'],stdin=PIPE,stdout=FNULL)
			player.wait()
			if ( playthis == 1 ):
				 playthis = 0

		if ( playthis == 2 ):
			player = Popen(['omxplayer','--adev', 'both','/media/usb/playthis/2.mp4'],stdin=PIPE,stdout=FNULL)
			player.wait()
			if ( playthis == 2 ):
				playthis = 0

		if ( playthis == 3 ):
			player = Popen(['omxplayer','--adev', 'both','/media/usb/playthis/3.mp4'],stdin=PIPE,stdout=FNULL)
			player.wait()
			if ( playthis == 3 ):
				playthis = 0

		if ( playthis == 4 ):
			player = Popen(['omxplayer','--adev', 'both','/media/usb/playthis/4.mp4'],stdin=PIPE,stdout=FNULL)
			player.wait()
			if ( playthis == 4 ):
				playthis = 0

		if ( playthis == 5 ):
			player = Popen(['omxplayer','--adev', 'both','/media/usb/playthis/5.mp4'],stdin=PIPE,stdout=FNULL)
			player.wait()
			if ( playthis == 5 ):
				playthis = 0

		if ( playthis == 6 ):
			player = Popen(['omxplayer','--adev', 'both','/media/usb/playthis/6.mp4'],stdin=PIPE,stdout=FNULL)
			player.wait()
			if ( playthis == 6 ):
				playthis = 0

		if ( playthis == 7 ):
			player = Popen(['omxplayer','--adev', 'both','/media/usb/playthis/7.mp4'],stdin=PIPE,stdout=FNULL)
			player.wait()
			if ( playthis == 7 ):
				playthis = 0

		if ( playthis == 8 ):
			player = Popen(['omxplayer','--adev', 'both','/media/usb/playthis/8.mp4'],stdin=PIPE,stdout=FNULL)
			player.wait()
			if ( playthis == 8 ):
				playthis = 0

		if ( playthis == 9 ):
			player = Popen(['omxplayer','--adev', 'both','/media/usb/playthis/9.mp4'],stdin=PIPE,stdout=FNULL)
			player.wait()
			if ( playthis == 9 ):
				playthis = 0

		if ( playthis == 10 ):
			player = Popen(['omxplayer','--adev', 'both','/media/usb/playthis/10.mp4'],stdin=PIPE,stdout=FNULL)
			player.wait()
			if ( playthis == 10 ):
				playthis = 0
# etc.
		if ( playthis == 0 ):
			player = Popen(['omxplayer','--adev', 'both',files],stdin=PIPE,stdout=FNULL)
			player.wait()
