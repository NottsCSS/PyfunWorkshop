import os
import glob
import time
from sys import platform

if platform == "linux" or platform == "linux2"or platform == "darwin":
    try:
        from simpleaudio import WaveObject
    except ImportError:
        exit(1)
    for file in glob.glob('./downloaded/*.wav'):  # play all wav music in file
        wave = WaveObject.from_wave_file(file)
        play = wave.play()
        play.wait_done()
elif platform == "win32" or platform == "cygwin":
    try:
        import winsound
    except ImportError:
        exit(1)
    for file in glob.glob('./downloaded/*.wav'):
        winsound.PlaySound(file, winsound.SND_FILENAME)
