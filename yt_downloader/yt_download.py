from pytube import Playlist, YouTube

# playlist=Playlist("https://www.youtube.com/playlist?list=PLs5b-5fM-hDIQxorUOcjXe3NHdb8mQ1gF")
# for video in playlist:
#     video.streams.get_highest_resolution().download()# # YouTube('https://youtu.be/9bZkp7q19f0').streams.get_highest_resolution().download()
yt = YouTube('http://youtube.com/watch?v=9bZkp7q19f0')
print(yt)
# yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download()