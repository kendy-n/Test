from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title:", yt.title)
print("View:", yt.views)

# Doing it the below way caps resolution at 360p
yd = yt.streams.get_highest_resolution()
yd.download('C:/Users/Kendy Nguyen/Videos/YouTube Videos')
# yt = YouTube('https://www.youtube.com/watch?v=GfsLT7W80AE');

