import time
import vlc
import os
import keyboard

# install notes:
# connect to mp4museum via ssh user pi password mp4museum 
# "sudo raspi-config" -> disable overlay filesystem, reboot
# "sudo pip3 install keyboard"
# put this file and your videos in /home/pi folder
# edit /home/pi/.bashrc:
## # mp4museum autostart
## setterm -cursor off
## tput setaf 0
## clear
## sudo python3 /home/pi/mp4m-keyboard.py > /tmp/mp4museum.log 2>&1
## setterm -cursor on
## tput setaf 7

# then reboot and press some buttons!

# Press 'ESC' to stop playback, 'SPACE' to toggle pause/play.
# Press 'A', 'S', 'D', etc. to play corresponding videos.
# Press 'Q' to exit the program.


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
        handle_key_event(None)  # Pass None as the event object
        time.sleep(0.1)
    
    media.release()
    player.release()

# Universal function to handle key presses
def handle_key_event(event):
    global player
    if keyboard.is_pressed('esc'):
        if player.is_playing() or player.is_paused():
            player.stop()
    elif keyboard.is_pressed('space'):
        if player.is_playing():
            player.pause()
        else:
            player.play()
            print("Playback resumed.")
    elif keyboard.is_pressed('q'):  # Use 'q' to exit the program
        global running
        running = False
    else:
        # Check if the key pressed is in the keys array
        for key, video in key_map.items():
            if keyboard.is_pressed(key):
                vlc_play(video)

# Map keys to video files
key_map = {
    'a': 'video1.mp4',
    's': 'video2.mp4',
    'd': 'video3.mp4',
    # Add more key-video mappings as needed
    # The files shall be in the same directory as the script: /home/pi
}

# Set up keyboard listener
keyboard.on_press(handle_key_event)

# Main loop
running = True
while running:
    time.sleep(0.1)  # Keep the loop running without consuming too much CPU

# Clean up
if player.is_playing():
    player.stop()
print("Program exited.")