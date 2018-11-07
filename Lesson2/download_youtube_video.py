import youtube_dl
import os

# from pytube import YouTube
# yt = YouTube("https://www.youtube.com/watch?v=rOU4YiuaxAM")
# print(yt.streams.filter(only_audio=True).filter(subtype="mp4").first())
# music = yt.streams.filter(only_audio=True).filter(subtype="mp4").first()
# print(yt.streams.filter(only_audio=True).filter(
#     subtype="mp4").first().default_filename)
# music.download("./downloaded")

ydl_opts = {
    'outtmpl': './downloaded/%(title)s.%(ext)s',
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192',
    }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=rOU4YiuaxAM'])

# switch to youtube_dl since pytube stopped working.