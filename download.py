from pytube import YouTube
from sys import argv
import ffmpeg

## path to download video to
download_path = 'C:/Users/Kendy Nguyen/Videos/YouTube Videos'
link = argv[1]
yt = YouTube(link)

## downloads video at 360p 
def download_progressive_video():
    print("Title:", yt.title)
    print("View:", yt.views)
    yd = yt.streams.get_highest_resolution()
    yd.download(download_path)


## Adaptive splits audio & video for higher quality
## progressive combines the two but limits it to low quality
## will need to do logic for quality to be 360, 720, 1080 or 4000 then throw error.
def download_video(quality = "1080p"):
    vid = yt.streams.filter(adaptive=True, res=quality).first()
    aud = yt.streams.filter(only_audio=True).first()

    vid.download(download_path)
    aud.download(download_path, filename = "audio.mp4")
    

