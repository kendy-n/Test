from download import *
from pytube import YouTube

## Array containing possible video qualities
video_qualities_list = ["360p", "480p", "720p", "1080p", "1440p", "4000p"]

def main():
    print("Input Youtube Link: ")
    link = input()
    yt = YouTube(link)
    vid_q = get_quality()

    print("Video name is: ", yt.title)
    print("Video Quality will be: ", vid_q)

    if vid_q == "360p":
        download_low(yt)
    elif vid_q == "480p":
        download_low(yt)
    else:
        download_video(yt, vid_q)

def get_quality():
    print("What Quality")
    quality = input()
    in_list = False
    while in_list == False: 
        if check_quality(quality, in_list) == True:
            break
        print("Please choose a suitable quality (360p, 480p, 720p, 1080p)")
        quality = input()
    return quality

def check_quality(quality, in_list):
    for i in video_qualities_list:
        if i == quality:
            in_list = True
    return in_list
    
if __name__ == "__main__":
    main()