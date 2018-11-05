import os
import glob
import time
from simpleaudio import WaveObject

# os.chdir("./songs")
for file in glob.glob('./downloaded/*.mp4'):
    print(file)
    os.system(f'ffmpeg -i "{file}" "{file[:-4]}.wav" ')
    os.remove(file)

for file in glob.glob('./downloaded/*.wav'):
    wave = WaveObject.from_wave_file(file)
    play = wave.play()
    play.wait_done()


