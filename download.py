from importlib.metadata import metadata
from pytube import YouTube
import ffmpeg
import os
 
## path to download video to
download_path = 'C:/Users/Kendy Nguyen/Videos/YouTube Videos'

## audio only
def download_audio():
    print("TO DO")

## download at SD quality (progressive stream)
def download_low(yt):
    yd = yt.streams.get_highest_resolution()
    yd.download(download_path)

## Adaptive splits audio & video for higher quality
## progressive combines the two but limits it to low quality
def download_video(yt, quality = "1080p"):
    vid = yt.streams.filter(adaptive=True, res=quality).first()
    aud = yt.streams.filter(only_audio=True).first()

    a = vid.download(filename = 'temo_video.mp4');
    b = aud.download(filename = 'temp_audio.mp4')

    video_stream = ffmpeg.input(a)
    audio_stream = ffmpeg.input(b)
    
    ffmpeg.output(audio_stream, video_stream, 'C:/Users/Kendy Nguyen/Videos/YouTube Videos/out.mp4').run()

    ## need to find any characters that will break and apply following logic. Move this into separate function
    vid.tit = yt.title
    if "|" in yt.title:
        vid.tit = yt.title.replace("|", "")
        print("Title: ", vid.tit)
    
    elif "\\" in yt.title:
        vid.tit = yt.title.replace("\\", "")
        print("Title: ", vid.tit)

    elif "/" in yt.title:
        vid.tit = yt.title.replace("/", "")
        print("Title: ", vid.tit)

    os.rename('C:/Users/Kendy Nguyen/Videos/YouTube Videos/out.mp4', 'C:/Users/Kendy Nguyen/Videos/YouTube Videos/' + vid.tit +'.mp4') 
    print("Re-named")

