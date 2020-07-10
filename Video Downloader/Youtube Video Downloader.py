# install the module youtube_dl by "pip install youtube_dl"
import youtube_dl

# put as many links yu want in the list
links = ["link_1, link_2, link_N"]

# you can also put additional features.
# You can ignore them if you just want to download the video anyways.

# 1. 'format':'bestvideo+bestaudio' Dowloads the video in the best available video and audio format.
# 2. 'writethumbnail':'writethumbnail' Downloads the thumbnail image of the video.
# 3. 'writesubtitles':'writesubtitles' Downloads the subtitles, if any.
# 4. 'writedescription':'writedescription' Writes the video description to a .description file.

download_options = {
    'format': 'bestvideo+bestaudio',
    'writethumbnail': 'writethumbnail',
    'writesubtitles': 'writesubtitiles',
    'writedescription': 'writedescription'
}

# the download process
with youtube_dl.YoutubeDL(download_options) as ydl:
    ydl.download(links)
    

# It can also be used to download more things. 
# With this module, you can not only download videos, 
# but you can also download entire playlists, metadata, thumbnails, subtitles, annotations, descriptions, audio, 
# and much more quite easily.
