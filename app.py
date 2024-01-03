import flet as ft
import os
from pytube import YouTube
from pydub import AudioSegment

# Proporciona la URL del video de YouTube
video_url = 'https://www.youtube.com/watch?v=t7xHamn5inQ'
yt = YouTube(video_url)

# Obtiene información sobre el video
print(f'Título: {yt.title}')
print(f'Duración: {yt.length} segundos')

# Obtiene la corriente de audio en formato MP4 (si está disponible)
audio_stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()

# Descarga el audio en formato MP4
download_path = 'C:/Users/Ismael/Desktop/FastMp3/pruebaV'
audio_path = os.path.join(download_path, f'{yt.title}.mp4')
audio_stream.download(download_path)



# Ruta del archivo MP4
mp4_path = 'C:/Users/Ismael/Desktop/FastMp3/pruebaV/One Piece - Opening 21 | Super Powers.mp4'

# Ruta de salida para el archivo MP3
mp3_path = 'C:/Users/Ismael/Desktop/FastMp3/pruebaV/One Piece - Opening 21 | Super Powers.mp3'

# Carga el archivo MP4
audio = AudioSegment.from_file(mp4_path, format="mp4")

# Exporta el audio a formato MP3
audio.export(mp3_path, format="mp3")