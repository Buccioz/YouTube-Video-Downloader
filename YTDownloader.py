import pytube
import os
import pyfiglet
import termcolor

from termcolor import colored
from pytube import YouTube
from pytube.cli import on_progress

banner = pyfiglet.figlet_format("YouTube Downloader", font="Slant")
print(colored(banner, 'magenta'))
print(colored(':::::::::::::::Developed By Buccioz:::::::::::::::', 'magenta'))

url = input('\n\nInsert video URL: ')  # Input URL

print(colored('\n720p IS THE ONLY RESOLUTION SUPPORTED', 'red'))
print("\n")


yt = pytube.YouTube(url, on_progress_callback=on_progress)

print(yt.title)

try:
     video = yt.streams.get_highest_resolution()
     video.download()

except EOFError as err:
     print(err)

else:
     print (colored('\n\nDownload completed successfully !', 'green'))
