# groot.py
import board, touchio, digitalio
from audiopwmio import PWMAudioOut as AudioOut # for CPB & Pico
from audiocore import WaveFile # only needed for wav

# set up the speaker
speaker = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
speaker.direction = digitalio.Direction.OUTPUT
speaker.value = True
audio = AudioOut(board.SPEAKER)

# if you want to set up a single touchpad on A1 & refer to it as touchpad_A1
touchpad_A4 = touchio.TouchIn(board.A4)

# set path where sound files can be found CHANGE if different folder name
path = "groot-wavs/"

# play_sound function - pass in the FULL NAME of file to play
def play_sound(filename):
    with open(path + filename, "rb") as wave_file:
        wave = WaveFile(wave_file)
        audio.play(wave)
        while audio.playing:
            pass

file_number = 1

print("Groot running!")
while True:
    # detect single touchpad touch - statement below is True if touched
    if touchpad_A4.value:
        print(f"I_am_groot_{file_number}.wav")
        play_sound(f"I_am_groot_{file_number}.wav")
        # modulo operator
        file_number = (file_number % 4) + 1 # gets remainder & adds 1
        # terinary operator
        # file_number = file_number + 1 if file_number < 4 else 1 # do if true if true/false do if false
        # with if conditional
        # file_number += 1
        # if file_number > 4:
        #     file_number = 1