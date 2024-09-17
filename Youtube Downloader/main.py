import yt_dlp as youtube_dl
import os

def download_audio(yt_url, download_folder):
    # Ensure the download folder exists
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
    
    # Set up options for yt_dlp
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),  # Template for output file path
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([yt_url])
        print(f"Successfully downloaded: {yt_url}")
    except Exception as e:
        print(f"Failed to download {yt_url}. Error: {e}")

def main():
    yt_urls = [
        "https://www.youtube.com/watch?v=8OAPLk20epo",
    ]
    
    download_folder = 'audio_files'  # Specify the folder where files will be saved

    for url in yt_urls:
        download_audio(url, download_folder)

main()
