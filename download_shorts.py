import os
from pytube import YouTube
from pytube.exceptions import RegexMatchError, VideoUnavailable

def download_shorts(url, output_path=None):
    try:
        # Crear el objeto YouTube
        yt = YouTube(url)
        
        # Obtener el stream de mayor resolución
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        
        if stream is None:
            print("No se encontró ningún vídeo compatible.")
            return
        
        # Configurar la ruta de salida
        if output_path is None:
            output_path = os.getcwd()
        
        # Crear el directorio si no existe
        os.makedirs(output_path, exist_ok=True)
        
        # Descargar el vídeo
        print(f"Descargando: {yt.title}")
        file_path = stream.download(output_path=output_path)
        
        # Renombrar el archivo para incluir la resolución
        base, ext = os.path.splitext(file_path)
        new_file_path = f"{base}_{stream.resolution}{ext}"
        os.rename(file_path, new_file_path)
        
        print(f"Descarga completa. Archivo guardado en: {new_file_path}")
        print(f"Resolución: {stream.resolution}")
        print(f"Tamaño del archivo: {stream.filesize / (1024 * 1024):.2f} MB")
        
    except RegexMatchError:
        print("Error: La URL proporcionada no es válida.")
    except VideoUnavailable:
        print("Error: El vídeo no está disponible o es privado.")
    except Exception as e:
        print(f"Se produjo un error durante la descarga: {str(e)}")

def main():
    while True:
        shorts_url = input("Introduce la URL del YouTube Shorts (o 'q' para salir): ")
        if shorts_url.lower() == 'q':
            break
        
        output_path = input("Introduce la ruta de salida (opcional, presiona Enter para usar la carpeta actual): ")
        if not output_path:
            output_path = None
        
        download_shorts(shorts_url, output_path)
        print("\n")

if __name__ == "__main__":
    main()
