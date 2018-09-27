# Fixed earlier problem with long comments & no time import.
# Thanks Taco Wijnsma for pointing out that I'd posted the wrong code.

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
from adafruit_circuitplayground.express import cpx
cpx.play_file("I_am_groot_1.wav")
soundNumber = 1
cpx.adjust_touch_threshold(200)
 
while True:
    if cpx.touch_A1:
        print("Touched A1!")
        cpx.play_file("I_am_groot_" + str(soundNumber) + ".wav")
        if soundNumber < 4:
            soundNumber = soundNumber + 1
        else:
            soundNumber = 1
    time.sleep(0.1)
