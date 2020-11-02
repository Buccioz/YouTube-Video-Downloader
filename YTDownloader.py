import pytube
import os

from pytube import YouTube
from pytube.cli import on_progress

url = input('Insert video URL: ')
yt = pytube.YouTube(url, on_progress_callback=on_progress)

print(yt.title)
try:
     video = yt.streams.get_highest_resolution()
     video.download()

except EOFError as err:
     print(err)

else:
     print("Download completed successfully")
