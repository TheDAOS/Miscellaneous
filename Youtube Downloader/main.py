# import youtube_dl # client to many multimedia portalss
import yt_dlp as youtube_dl  # Replace youtube_dl with yt_dlp

# downloads yt_url to the same directory from which the script runs
def download_audio(yt_url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    # with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    #     ydl.download([yt_url])

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

    for url in yt_urls:
        download_audio(url)

main()
