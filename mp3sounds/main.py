from __future__ import unicode_literals
import youtube_dlc as youtube_dl
from youtubesearchpython import VideosSearch

# Lista de nomes de músicas
music_list = []

# Pesquisar no YouTube e obter a primeira URL de cada música
urls = []
for music in music_list:
    results = VideosSearch(music, limit=1).result()
    if results['result']:
        url_suffix = results['result'][0]['link']
        urls.append(url_suffix)

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '/your/repository/output/%(title)s.%(ext)s', 
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    for url in urls:
        ydl.download([url])
