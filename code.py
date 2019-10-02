# Fixed earlier problem with long comments & no time import.
# Thanks Taco Wijnsma for pointing out that I'd posted the wrong code.

# Press A to make it less touch sensitive (increasing threshold)
# Press B to make it more touch sensitive (decreasing threshold)

# For this code to work, your CPX must have four files on it, each named:
# I_am_groot_1.wav, I_am_groot_2.wav, I_am_groot_3.wav, and I_am_groot_4.wav
# The code cycles through these four sounds, each time a capacitive touch on
# CPX is registered (e.g. when you touch Groot's leaves).
# You can easily save different files and use those, but...
# files must be 22,050 kHz, 16-bit, mono (or less) WAV files
# I simply recorded YouTube videos of Baby Groot using a ScreenFlow
# screencast, edited out video, cropped the sound, then exported the audio.
# I then downloaded Audacity and used this product to lower the sound
# quality to 22,050 kHz and 16 bit. If you search online you can find several
# good Audacity tutorials. You can likely also record sound from video
# playing on your phone or computer using iOS video capture or QuickTime for
# the Mac.

#   More detail on using sound files with CPX can be found at:
#   https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/play-file
#   Info on this project is at:

import time
import touchio
from adafruit_circuitplayground.express import cpx
cpx.play_file("I_am_groot_1.wav")
soundNumber = 1
# Plugged into USB, higher # below is better.
# Battery = less power, so 200 workded well for me.
# 500 was what I had been using.
touch_threshold = 750
cpx.adjust_touch_threshold(touch_threshold)

while True:
    if cpx.touch_A1:
        print("Touched A1!")
        cpx.play_file("I_am_groot_" + str(soundNumber) + ".wav")
        if soundNumber < 4:
            soundNumber = soundNumber + 1
        else:
            soundNumber = 1
    elif cpx.button_a:
        touch_threshold = touch_threshold + 50
        print("touch_threshold is:", touch_threshold)
    elif cpx.button_b:
        touch_threshold = touch_threshold - 50
        print("touch_threshold is:", touch_threshold)

    time.sleep(0.1)
