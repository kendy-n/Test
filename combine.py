import ffmpeg

def combine():
    video_stream = ffmpeg.input('video.mp4')
    audio_stream = ffmpeg.input('audio.mp4')
    ffmpeg.output(audio_stream, video_stream, 'out.mp4').run()

combine()