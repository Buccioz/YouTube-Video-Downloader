import pytube
import os
import pyfiglet
import termcolor
import colorama

from termcolor import *
from pytube import YouTube
from pytube.cli import on_progress

colorama.init()

banner = pyfiglet.figlet_format("YouTube Downloader", font="Slant")
cprint(banner, 'magenta')
cprint('\n:::::::::::::::Developed By Buccioz:::::::::::::::', 'magenta')

url = input('\n\nInsert video URL: ')  # Input URL

cprint('\n720p IS THE ONLY RESOLUTION SUPPORTED', 'red')
print("\n")


yt = pytube.YouTube(url, on_progress_callback=on_progress)

print(yt.title)

try:
     video = yt.streams.get_highest_resolution()
     video.download()

except EOFError as err:
     print(err)

else:
     cprint('\n\nDownload completed successfully !', 'green')
