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
        "https://youtu.be/fdubeMFwuGs?si=Tl5B2mAPWRilTGAv",
        "https://youtu.be/A66TYFdz8YA?si=uRq-vaLFf9ZqWmRM",
        "https://youtu.be/6mr4cYJ7yew?si=CWpisIMJ_aUfQW2d",
        "https://youtu.be/5Eqb_-j3FDA?si=kXCVaV3FTFqE01A1",

        "https://youtu.be/4tYktXxNspo?si=aNP2QVDbl-FrMcwO",
        "https://youtu.be/ofTxceS4wLI?si=KDI7DKx80ZAXC7H6",
        "https://youtu.be/9JDSGhhiOwI?si=EkXXCMO_59wuiUrq",
        "https://youtu.be/vr8RaNuWjWc?si=b366ediLX-l9ms3P",

        "",
        "",
        "",
        "",

    ]
    
    download_folder = 'audio_files'  # Specify the folder where files will be saved

    for url in yt_urls:
        download_audio(url, download_folder)

main()
