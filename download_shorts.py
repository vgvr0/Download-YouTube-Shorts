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
        # This guarantees we get the best available quality
        # WITH audio, which will be 720p at most.
        
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
    
    # URL of your Short
    shorts_url = "https://www.youtube.com/shorts/YYnst9xW15U"
    
    # URL of 4K video (to test that it ONLY downloads 720p)
    # video_4k = "https://www.youtube.com/watch?v=aqz-KE-bpKQ"

    # Call the function with your Short
    download_video_max_720p(shorts_url, download_path="My_Shorts_720p")
    
    # Call the function with the 4K video
    # You'll see that even though it's 4K, it will only download the 720p version
    # download_video_max_720p(video_4k, download_path="My_Videos_720p")