import os
import glob
import time
from simpleaudio import WaveObject

for file in glob.glob('./downloaded/*.mp4'): #get all mp4 files in downloaded/
    print(file)
    os.system(f'./ffmpeg -i "{file}" "{file[:-4]}.wav" ') # call function to convert file type
    os.remove(file)

for file in glob.glob('./downloaded/*.wav'): #play all music in file
    wave = WaveObject.from_wave_file(file)
    play = wave.play()
    play.wait_done()
