import time
import vlc
import os
import RPi.GPIO as GPIO

# install notes:
# connect to mp4museum via ssh user pi password mp4museum 
# "sudo raspi-config" -> disable overlay filesystem, reboot
# put this file and your videos in /home/pi folder
# edit in the last parts of /home/pi/.bashrc:
# python3 /home/pi/mp4m-gpio.py > /tmp/mp4museum.log 2>&1

# then reboot and press some buttons!

# Press GPIO pin 22 to stop playback, GPIO pin 23 to toggle pause/play.
# Press GPIO pins 13, 14... to play corresponding videos.
# change pins as needed, both in the event handler and the pin setup


# Read audio device config
audiodevice = "0"

if os.path.isfile('/boot/alsa.txt'):
    with open('/boot/alsa.txt', 'r') as f:
        audiodevice = f.read(1)

# Play media
def vlc_play(source):
    if ".loop." in source:
        vlc_instance = vlc.Instance('--input-repeat=999999999 -q -A alsa --alsa-audio-device hw:' + audiodevice)
    else:
        vlc_instance = vlc.Instance('-q -A alsa --alsa-audio-device hw:' + audiodevice)
    
    global player
    player = vlc_instance.media_player_new()
    media = vlc_instance.media_new(source)
    player.set_media(media)
    player.play()
    time.sleep(1)
    
    # Wait for the media to finish playing
    while player.get_state() in (vlc.State.Playing, vlc.State.Paused):
        handle_gpio_event()
        time.sleep(0.1)
    
    media.release()
    player.release()

# Universal function to handle GPIO events
def handle_gpio_event():
    global player
    if GPIO.input(22):
        if player.is_playing() or player.is_paused():
            player.stop()
    elif GPIO.input(23):
        if player.is_playing():
            player.pause()
        else:
            player.play()
            print("Playback resumed.")
    else:
        # Check if the GPIO pin is in the gpio_map
        for pin, video in gpio_map.items():
            if GPIO.input(pin):
                vlc_play(video)

# Map GPIO pins to video files
gpio_map = {
    13: 'video1.mp4',
    14: 'video2.mp4',
    # Add more pin-video mappings as needed
    # The files shall be in the same directory as the script: /home/pi
}

# Set up GPIO
GPIO.setmode(GPIO.BOARD)
try:
    for pin in gpio_map.keys():
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    # Main loop
    running = True
    while running:
        handle_gpio_event()
        time.sleep(0.1)  # Keep the loop running without consuming too much CPU

except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()  # Clean up GPIO settings
