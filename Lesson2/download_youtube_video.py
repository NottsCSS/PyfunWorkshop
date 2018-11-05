from pytube import YouTube, Playlist
import os

yt = YouTube("https://www.youtube.com/watch?v=0dYlvdLdK9w")
print(yt.streams.filter(only_audio=True).filter(subtype="mp4").first())
music = yt.streams.filter(only_audio=True).filter(subtype="mp4").first()
print(yt.streams.filter(only_audio=True).filter(subtype="mp4").first().default_filename)
music.download("./downloaded")
