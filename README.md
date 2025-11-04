YouTube Video Downloader (Max 720p)
This Python script allows you to download YouTube videos (including Shorts) using the pytubefix library.

It is designed to download the best progressive stream (max 720p), which includes both video and audio in a single file, avoiding the need for external tools like FFmpeg.

Why pytubefix?
This project uses pytubefix instead of the standard pytube because YouTube frequently updates its site, which often breaks download scripts. pytubefix is a community-maintained fork that is updated more frequently to patch these breaking changes (like the common HTTP Error 400).

Installation
Make sure you have Python installed. You can install the required library using pip:

Bash

pip install pytubefix
Usage
Save the code below as a Python file (e.g., download.py).

Run the script from your terminal.

Python

from pytubefix import YouTube
from pytubefix.exceptions import VideoUnavailable, AgeRestrictedError
import os

def download_video_max_720p(url, download_path="My_Downloads"):
    """
    Downloads a video, searching only for progressive streams
    (audio+video together), which have a maximum quality of 720p.
    
    It ignores 1080p, 4K, and adaptive streams.
    """
    try:
        # 1. Ensure the download directory exists
        if not os.path.exists(download_path):
            os.makedirs(download_path)
            print(f"Directory created: {download_path}")

        # 2. Get the YouTube object
        video = YouTube(url)
        print(f"\nSearching (max 720p): {video.title}")

        # 3. SELECTION LOGIC (ONLY UP TO 720p)
        # We filter by progressive=True (audio+video) and mp4.
        # Then, we order by 'resolution' in descending order
        # and take the first one (.first()).
        stream = video.streams.filter(
            progressive=True, 
            file_extension='mp4'
        ).order_by('resolution').desc().first()

        if stream:
            print(f"Stream found: {stream.resolution} (Progressive, with audio)")
            print("Starting download...")
            
            # 4. Download to the specified path
            stream.download(output_path=download_path)
            print(f"Download complete! Saved in '{download_path}'")
        else:
            print("Error: No progressive stream found (mp4 with audio and video).")

    # 5. Error handling
    except AgeRestrictedError:
        print(f"Error: The video is age-restricted and cannot be downloaded.")
    except VideoUnavailable:
        print(f"Error: The video is unavailable, private, or has been deleted.")
    except Exception as e:
        print(f"An unexpected error occurred: {type(e).__name__} - {e}")

# --- Main block to run the script ---
if __name__ == "__main__":
    
    # URL of the video you want to download
    video_url = "https://www.youtube.com/shorts/YYnst9xW15U"
    
    # You can also test with a high-quality video to confirm it only gets 720p
    # video_url = "https://www.youtube.com/watch?v=aqz-KE-bpKQ"

    # Call the function
    download_video_max_720p(video_url, download_path="My_Video_Downloads")
Change the video_url variable inside the if __name__ == "__main__": block to the URL you want to download.

Run the script. The video will be downloaded to the folder specified in download_path.

Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request to suggest improvements or report bugs.

License
This project is licensed under the MIT License - see the LICENSE file for details.
