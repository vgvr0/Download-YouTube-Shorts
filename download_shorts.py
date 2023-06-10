from pytube import YouTube

def download_shorts(url):
    try:
        video = YouTube(url)
        stream = video.streams.filter(file_extension='mp4', only_video=True).first()
        if stream is not None:
            stream.download()
            print("Descarga completa.")
        else:
            print("No se encontró ningún vídeo compatible.")
    except Exception as e:
        print("Se produjo un error durante la descarga:", str(e))

# URL del YouTube Shorts que deseas descargar
shorts_url = "https://www.youtube.com/shorts/XXXXXXXXXXX"

# Llama a la función de descarga
download_shorts(shorts_url)
