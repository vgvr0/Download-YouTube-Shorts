# YouTube Shorts Downloader

This Python script allows you to download YouTube Shorts videos using the pytube library.

## Installation

Make sure you have Python installed on your machine. You can install the required library using pip:

```
pip install pytube
```

## Usage

1. Import the `YouTube` class from the `pytube` library and define the `download_shorts` function in your Python script.

```python
from pytube import YouTube

def download_shorts(url):
    try:
        video = YouTube(url)
        stream = video.streams.filter(file_extension='mp4', only_video=True).first()
        if stream is not None:
            stream.download()
            print("Download complete.")
        else:
            print("No compatible video found.")
    except Exception as e:
        print("An error occurred during download:", str(e))

# URL of the YouTube Shorts you want to download
shorts_url = "https://www.youtube.com/shorts/XXXXXXXXXXX"

# Call the download function
download_shorts(shorts_url)
```

2. Replace `'https://www.youtube.com/shorts/XXXXXXXXXXX'` with the URL of the YouTube Shorts you want to download.

3. Run the script and the Shorts video will be downloaded to your current directory.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request to suggest improvements or report bugs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
